#Cambiar color cuando errores de labels, encriptar contra

import sys
from PyQt5 import QtWidgets
from v2_login import Ui_MainWindow as LoginUi
from v2_2_registrarse import Ui_MainWindow as CrearCuentaUi
from res import *
from PyQt5.QtWidgets import QMessageBox
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
  h = hashlib.new("sha265", contra.encode())
  # Convertimos la contraseña cifrada en hexadecimal
  contraCif = str(h.hexdigest()) 
  return contraCif

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
   
#POR IMPLEMENTAR (No van a saltar, va a salir en los label)
def showDialog(msg, title = "informacion"):
  msgBox = QMessageBox()
  msgBox.setIcon(QMessageBox.Information)
  msgBox.setText(msg)
  msgBox.setWindowTitle(title)
  msgBox.exec()

class Login(QtWidgets.QMainWindow):
    
  def __init__(self, parent=None):
    QtWidgets.QWidget.__init__(self,parent)
    self.ui = LoginUi()
    self.ui.setupUi(self)
    self.ui.boton_entrar.clicked.connect(self.funcionLogin)
    self.ui.botonl_crearCuentaNueva.clicked.connect(self.cambiarDePantalla)
    self.ui.botonlCerrar.clicked.connect(app.quit)
        


  def funcionLogin(self):
    email = self.ui.txtl_usuario.text().lower()
    password = self.ui.txtl_password.text()

    conexion = conectar()   
    usuarioOK = comprobarUsuario(conexion, email, password)
    if usuarioOK:
      showDialog("Login ok")
    else:
      showDialog("Datos incorrectos")
    desconectar(conexion)

    self.ui.txtl_usuario.clear()
    self.ui.txtl_password.clear()

  def cambiarDePantalla(self):
    crear_cuenta = CrearCuenta()
    stacked_widget.addWidget(crear_cuenta)
    stacked_widget.setCurrentIndex(1)

class CrearCuenta(QtWidgets.QMainWindow):
  def __init__(self, parent=None):
    QtWidgets.QWidget.__init__(self,parent)
    self.ui = CrearCuentaUi()
    self.ui.setupUi(self)
    self.ui.botonr_entrar.clicked.connect(self.funcionRegistro)
    self.ui.botonrCerrar.clicked.connect(app.quit)


  def funcionRegistro(self):
    if self.ui.txtr_password.text() == self.ui.txtr_confirmarPassword.text():
      usuario = self.ui.txtr_usuario.text()
      contra  = self.ui.txtr_password.text()
      email   = self.ui.txtr_email.text().lower()
      preSeg  = self.ui.txtr_preguntaSeguridad.text()
      resSeg  = self.ui.txtr_respuestaSeguridad.text()

      datos = (email, usuario, contra, preSeg, resSeg)
      vacio = camposVacios(datos)
      
      if vacio:
        showDialog("Debe rellenar todos los datos")
      elif len(contra) < 8:
        showDialog("La contraseña debe tener al menos 8 caracteres")
      elif not comprobarMail(email):
        showDialog("El mail no es valido")
      else:
        conexion = conectar()
        if existeUsu(conexion, email):
          showDialog("La cuenta ya existe")
        else:
          contraCif = cifrarContra(contra)
          resSegCif = cifrarContra(resSeg)

          datos = (email, usuario, contraCif, preSeg, resSegCif)
          crearUsuario(conexion, datos)
          stacked_widget.setCurrentIndex(0)  # Cambiar a la ventana de Login
        desconectar(conexion)

      self.ui.txtr_password.clear()
      self.ui.txtr_confirmarPassword.clear()
      self.ui.txtr_respuestaSeguridad.clear()


#MAIN
if __name__ == "__main__":
  app = QtWidgets.QApplication(sys.argv)

  stacked_widget = QtWidgets.QStackedWidget()  #Se crea un objeto stacked_widget 
  login = Login()
  # crear_cuenta = CrearCuenta()

  #Se agregan las ventanas al objeto stacked widget
  stacked_widget.addWidget(login)
  ### stacked_widget.addWidget(crear_cuenta) #La creo mejor arriba en CrearCuenta

  stacked_widget.resize(625, 565)
  stacked_widget.setCurrentIndex(0)  # Iniciar en la ventana de Login

  # Para esconder el marco principal en la ventana principal
  stacked_widget.setWindowFlags(QtCore.Qt.FramelessWindowHint)
  stacked_widget.setAttribute(QtCore.Qt.WA_TranslucentBackground)

  stacked_widget.show()
  # login.show()
  sys.exit(app.exec_())