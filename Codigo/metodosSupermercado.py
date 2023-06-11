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
    datosUsu = cur.fetchone()
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
    print(usu)
    if desc != "":
        desc = buscarDescuento(conn, desc)
        valores = (usu, desc, prec, fecha)
        query = f"INSERT INTO tickets (usuario, desc_id, precio, fecha) VALUES {valores} RETURNING tick_id;"
    else:
        valores = (usu, prec, fecha)
        query = f"INSERT INTO tickets (usuario, precio, fecha) VALUES {valores} RETURNING tick_id;"

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

def cargarCCAA(conn):
  query = f"SELECT * FROM CCAA;"
  try:
    cur = conn.cursor()
    cur.execute(query)
    comunidades = cur.fetchall()
  except (Exception, psycopg2.DatabaseError) as error:
    print(error)
  return comunidades

def cargarProvs(conn, ca):
  if ca != None:
    query = f"SELECT * FROM PROVINCIAS where idCCAA = '{ca}';"
    try:
      cur = conn.cursor()
      cur.execute(query)
      provincias = cur.fetchall()
    except (Exception, psycopg2.DatabaseError) as error:
      print(error)
    return provincias
  else: return []

def cargarMuns(conn, prov):
  if prov != None:
    query = f"SELECT * FROM MUNICIPIOS where idProvincia = '{prov}';"
    try:
      cur = conn.cursor()
      cur.execute(query)
      municipios = cur.fetchall()
    except (Exception, psycopg2.DatabaseError) as error:
      print(error)
    return municipios
  else: return []

def buscarCA(conn, ca):
  query = f"select Nombre from CCAA where idCCAA = '{ca}';"
  try:
    cur = conn.cursor()
    cur.execute(query)
    car = cur.fetchone()[0]
  except (Exception, psycopg2.DatabaseError) as error:
    print(error)
  return car

def buscarCANom(conn, ca):
  if ca != "":
    query = f"select idCCAA from CCAA where Nombre = '{ca}';"
    try:
      cur = conn.cursor()
      cur.execute(query)
      car = cur.fetchone()[0]
    except (Exception, psycopg2.DatabaseError) as error:
      print(error)
    return car

def buscarProv(conn, pro):
  query = f"select Provincia from PROVINCIAS where idProvincia = '{pro}';"
  try:
    cur = conn.cursor()
    cur.execute(query)
    prov = cur.fetchone()[0]
  except (Exception, psycopg2.DatabaseError) as error:
    print(error)
  return prov

def buscarProvNom(conn, pro):
  if pro != "":
    query = f"select idProvincia from PROVINCIAS where Provincia = '{pro}';"
    try:
      cur = conn.cursor()
      cur.execute(query)
      prov = cur.fetchone()[0]
    except (Exception, psycopg2.DatabaseError) as error:
      print(error)
    return prov

def buscarMun(conn, mu):
  query = f"select Municipio from MUNICIPIOS where idMunicipio = '{mu}';"
  try:
    cur = conn.cursor()
    cur.execute(query)
    mun = cur.fetchone()[0]
  except (Exception, psycopg2.DatabaseError) as error:
    print(error)
  return mun

def buscarMunNom(conn, mu):
  query = f"select idMunicipio from MUNICIPIOS where Municipio = '{mu}';"
  try:
    cur = conn.cursor()
    cur.execute(query)
    mun = cur.fetchone()[0]
  except (Exception, psycopg2.DatabaseError) as error:
    print(error)
  return mun

def actualizarUsu(conn, datos, email):
  query = f"update usuarios set nombre = %s, contrasena = %s, preg_seg = %s, resp_seg = %s, direccion = %s, cp = %s, id_ca = %s, id_provincia = %s, id_municipio = %s, telefono = %s, dni = %s, Apellidos = %s where correo = '{email}';"
  try:
    cur = conn.cursor()
    cur.execute(query, datos)
    conn.commit()
    showDialog("Los datos se han actualizado correctamente")
  except (Exception, psycopg2.DatabaseError) as error:
    print(error)


def camposVacios(campos):
  # Recorre una tupla para que ningun campo sea nulo
	vacio = False
	for campo in campos:
		if campo == "":
			vacio = True
			break
	return vacio

def camposNone(campos):
  # Recorre una tupla para que ningun campo sea nulo
	vacio = False
	for campo in campos:
		if campo == None:
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


def obtenerTickets(conn,usu):
  query = f"SELECT * FROM tickets where usuario = '{usu}';"
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



def obtenerLineaPedidosPorTickID(tick_id):
   
    consulta = '''
        SELECT lp.linea_id, lp.prod_id, lp.precio, lp.cantidad, lp.compra_id
        FROM lineapedidos lp
        JOIN tickets t ON lp.compra_id = t.tick_id
        WHERE t.tick_id = %s
    '''

    # Ejecutar la consulta
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute(consulta, (tick_id,))
    resultados = cursor.fetchall()

    # Cerrar la conexión con la base de datos
    cursor.close()
    conexion.close()

    # Devolver los resultados
    return resultados

###################################################### Kenia

def nombreProducto(prodID):
  consulta=(f"SELECT nombre from producto where prod_id='{prodID}'")
  try:
    conn=conectar()
    cur = conn.cursor()
    cur.execute(consulta)
    nombre = cur.fetchone()[0]
    
    # Cerrar la conexión con la base de datos
    cur.close()
    conn.close()
    return nombre
  except (Exception, psycopg2.DatabaseError) as error:
        print(error)

def buscarCompra(compraID):
  consulta=(f"SELECT t.fecha, t.precio, d.descuento, t.tick_id from tickets t left join descuentos d on t.desc_id=d.desc_id where t.tick_id={compraID}")
  try:
    conn=conectar()
    cur = conn.cursor()
    cur.execute(consulta)
    compra = cur.fetchall()
    
    # Cerrar la conexión con la base de datos
    cur.close()
    conn.close()
    return compra
  except (Exception, psycopg2.DatabaseError) as error:
        print(error)

def buscarUsuario(usuarioID):
  consulta=(f"SELECT u.nombre, u.apellidos, u.dni, u.direccion, c.nombre, u.cp, p.provincia, m.municipio from usuarios u join ccaa c on u.id_ca=c.idccaa join municipios m on u.id_municipio=m.idmunicipio join provincias p on u.id_provincia=p.idprovincia where correo='{usuarioID}'")
  try:
    conn=conectar()
    cur = conn.cursor()
    cur.execute(consulta)
    datosUsuario = cur.fetchall()
    
    # Cerrar la conexión con la base de datos
    cur.close()
    conn.close()
    return datosUsuario
  except (Exception, psycopg2.DatabaseError) as error:
        print(error)