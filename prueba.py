import hashlib
import psycopg2
# print("Hola, esto es una prueba")
# contraseña="vistaalegre"
# def cifrarContra(contra):
#    # Creamos el objeto de clase hash y le pasamos la contraseña en byte string a cifrar
#   h = hashlib.new("sha256", contra.encode())
#   # Convertimos la contraseña cifrada en hexadecimal
#   contraCif = str(h.hexdigest()) 
#   return contraCif
# print(cifrarContra(contraseña))

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

def comprobarCupon(conn,cupon):
  query = f"select descuento from descuentos where código = '{cupon}' and activo = true; "
  try:
    cur = conn.cursor()
    cur.execute(query)
    descuento = cur.fetchall()
    if len(descuento)==0:
      descuento="El código descuento no es válido"
    else:
      descuento=descuento[0]   
  except (Exception, psycopg2.DatabaseError) as error:
    print(error)
  return descuento
conn=conectar()
print(comprobarCupon(conn,'123'))