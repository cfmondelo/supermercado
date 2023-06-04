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

def mostrarCarrito(conn):
  query = f"select p.nombre, p.categoria, p.precio , c.cantidad, p.imagen  from carrito c join producto p on c.prod_id = p.prod_id;"
  try:
    cur = conn.cursor()
    cur.execute(query)
    prods = cur.fetchall()
  except (Exception, psycopg2.DatabaseError) as error:
    print(error)
  return prods

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
      valido=False
    else: 
      showDialog("Cupon ok")
      valido=True
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