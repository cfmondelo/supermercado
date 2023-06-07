from PyQt5.QtWidgets import QMessageBox
from PyQt5 import QtWidgets
import psycopg2
import hashlib
import bcrypt
import re

def conectar():
  try:
    conn = psycopg2.connect(
    host = "127.0.0.1",
    port = "5432",
    database = "organic",
    user = "admin",
    password = "vistaalegre")

    conn.autocommit = True

  except (Exception, psycopg2.DatabaseError) as error:
    print(error)

  return conn

def desconectar(conn):
  if conn is not None:
    conn.close()
    
def crearUsuario(conn, datos):
  query = f"INSERT INTO usuarios(correo, nombre, contrasena, preg_seg, resp_seg) VALUES {datos};"
  try:
    cur = conn.cursor()
    cur.execute(query)
    print('Datos insertados')
    conn.commit()
    cur.close()
  except (Exception, psycopg2.DatabaseError) as error:
    print(error)

def comprobarUsuario(conn, mail, contra):
  # Comprobar que el mail y contraseña son correctos para iniciar sesion
  contraCif = cifrarContra(contra)
  query = f"SELECT * FROM usuarios WHERE correo = '{mail}' AND contrasena = '{contraCif}';"
  try:
    cur = conn.cursor()
    cur.execute(query)
    datosUsu = cur.fetchall()
  except (Exception, psycopg2.DatabaseError) as error:
    print(error)
  return datosUsu

def existeUsu(conn, mail):
  #Comprueba si existe el correo al crear una cuenta
  query = f"SELECT * FROM usuarios WHERE correo = '{mail}';"
  try:
    cur = conn.cursor()
    cur.execute(query)
    datosUsu = cur.fetchall()
  except (Exception, psycopg2.DatabaseError) as error:
    print(error)
  return datosUsu

def cifrarContra(contra):
   # Creamos el objeto de clase hash y le pasamos la contraseña en byte string a cifrar
  h = hashlib.new("sha256", contra.encode())
  # Convertimos la contraseña cifrada en hexadecimal
  contraCif = str(h.hexdigest()) 
  return contraCif

def mostrarProductos(conn):
  query = f"SELECT * FROM producto;"
  try:
    cur = conn.cursor()
    cur.execute(query)
    prods = cur.fetchall()
  except (Exception, psycopg2.DatabaseError) as error:
    print(error)
  return prods

def buscarProd(conn, nom):
  query = f"select prod_id, precio from producto p where p.nombre = '{nom}';"
  try:
    cur = conn.cursor()
    cur.execute(query)
    prod = cur.fetchone()
  except (Exception, psycopg2.DatabaseError) as error:
    print(error)
  return prod

def insertarCarr(conn, prod, email):
  carr = (email, prod[0], prod[1], 1)
  query = f"insert into carrito (usuario, prod_id, precio, cantidad) values {carr}"
  try:
      cur = conn.cursor()
      cur.execute(query)
      conn.commit()
  except (Exception, psycopg2.DatabaseError) as error:
      print(error)

def actualizarCarr(conn, cant, id, email):
  query = f"update carrito set cantidad = '{cant+1}' where prod_id = '{id}' and usuario = '{email}';"
  try:
    cur = conn.cursor()
    cur.execute(query)
    conn.commit()
  except (Exception, psycopg2.DatabaseError) as error:
    print(error)

def buscarCarr(conn, id, email):
  query = f"select cantidad from carrito where prod_id = '{id}' and usuario = '{email}';"
  try:
    cur = conn.cursor()
    cur.execute(query)
    cant = cur.fetchone()
  except (Exception, psycopg2.DatabaseError) as error:
    print(error)
  return cant

def mostrarCarrito(conn, email):
  query = f"select p.nombre, p.categoria, p.precio , c.cantidad, p.imagen, p.prod_id from carrito c join producto p on c.prod_id = p.prod_id where usuario = '{email}';"
  try:
    cur = conn.cursor()
    cur.execute(query)
    prods = cur.fetchall()
  except (Exception, psycopg2.DatabaseError) as error:
    print(error)
  return prods

def borrarCarrito(conn, usu):
  query = f"delete from carrito where usuario = '{usu}';"
  try:
    cur = conn.cursor()
    cur.execute(query)
    conn.commit()
  except (Exception, psycopg2.DatabaseError) as error:
    print(error)

def insertarLineaPed(conn, usu, desc, prec, fecha):
  linea = []
  tick_id = insertarTicket(conn, usu, desc, prec, fecha)

  prods = mostrarCarrito(conn, usu)

  for prod in prods:
    valores = (prod[5], prod[2], prod[3], tick_id)

    query = f"insert into lineapedidos (prod_id, precio, cantidad, compra_id) values {valores};"
    try:
      cur = conn.cursor()
      cur.execute(query)
      conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
      print(error)
  borrarCarrito(conn, usu)
  showDialog("Compra realizada correctamente")

def insertarTicket(conn, usu, desc, prec, fecha):
  if desc != "":
    desc = buscarDescuento(conn, desc)
    valores = (usu, desc, prec, fecha)
    query = f"insert into tickets (usuario, desc_id, precio, fecha) values {valores} returning tick_id;"
  else:
    valores = (usu, prec, fecha)
    query = f"insert into tickets (usuario, precio, fecha) values {valores} returning tick_id;"

  try:
    cur = conn.cursor()
    cur.execute(query)
    conn.commit()
    serial = cur.fetchone()[0]
  except (Exception, psycopg2.DatabaseError) as error:
    print(error)
  
  return serial

def buscarDescuento(conn, desc):
  query = f"select desc_id from descuentos where código = '{desc}';"
  try:
    cur = conn.cursor()
    cur.execute(query)
    desc = cur.fetchone()[0]
  except (Exception, psycopg2.DatabaseError) as error:
    print(error)
  return desc

def camposVacios(campos):
  # Recorre una tupla para que ningun campo sea nulo
	vacio = False
	for campo in campos:
		if campo == "":
			vacio = True
			break
	return vacio
  
def comprobarMail(mail):
  patronCorreo = ("^\w+@[a-z]+\.[a-z]{2,3}$")
  return re.search(patronCorreo, mail)

def comprobarCupon(conn,cupon):
  query = f"select descuento from descuentos where código = '{cupon}' and activo = true; "
  try:
    cur = conn.cursor()
    cur.execute(query)
    descuento = cur.fetchall()
    if len(descuento)==0:      
      showDialog("El cupón no es válido")
      descuento=0
    else: 
      showDialog("Cupon ok")
      descuento=descuento[0][0]
  except (Exception, psycopg2.DatabaseError) as error:
    print(error)
  return descuento
   
#POR IMPLEMENTAR (No van a saltar, va a salir en los label)
def showDialog(msg, title = "informacion"):
  msgBox = QMessageBox()
  msgBox.setIcon(QMessageBox.Information)
  msgBox.setText(msg)
  msgBox.setWindowTitle(title)
  msgBox.exec()
#FIN POR IMPLEMENTAR




###################################################### Kenia


def obtenerTickets(conn, usu):
  query = f"SELECT * FROM tickets where usuario = '{usu};"
  try:
    cur = conn.cursor()
    cur.execute(query)
    tikets = cur.fetchall()
  except (Exception, psycopg2.DatabaseError) as error:
    print(error)
  return tikets

# conn = conectar()
# t = obtenerTickets(conn)
# print(t)

###################################################### Kenia
