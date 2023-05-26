import sys
from PyQt5 import QtWidgets
from PyQt5.QtCore import QPropertyAnimation, QEasingCurve 
from PyQt5.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget, QPushButton 
from v2_login import Ui_MainWindow as LoginUi
from v2_2_registrarse import Ui_MainWindow as CrearCuentaUi
from v3_menu import Ui_MainWindow as MenuPrincipalUi
from res import *




class Login(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self,parent)
        self.ui = LoginUi()
        self.ui.setupUi(self)
        self.ui.boton_entrar.clicked.connect(self.cambiarAVentanaPrincipal)
        self.ui.botonl_crearCuentaNueva.clicked.connect(self.cambiarDePantalla)
        self.ui.botonlCerrar.clicked.connect(app.quit)
        


    # def funcionLogin(self):
    #     email=self.ui.txtl_usuario.text()
    #     password=self.ui.txtl_password.text()
    #     print("Ha iniciado correctamente: ", email, password)
        

    def cambiarDePantalla(self):
        crear_cuenta = CrearCuenta()
        stacked_widget.addWidget(crear_cuenta)
        stacked_widget.setCurrentIndex(1)

    def cambiarAVentanaPrincipal(self):
        ventanaPrincipal = VentanaPrincipal()
        stacked_widget.addWidget(ventanaPrincipal)
        stacked_widget.setCurrentIndex(2)
        
        


        

class CrearCuenta(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self,parent)
        self.ui = CrearCuentaUi()
        self.ui.setupUi(self)
        # self.ui.botonr_entrar.clicked.connect(self.funcionRegistro)
        # self.ui.botonrCerrar.clicked.connect(app.quit)


    def funcionRegistro(self):
        email=self.ui.txtr_email.text()
        if self.ui.txtr_password.text()==self.ui.txtr_confirmarPassword.text():
            contraseña=self.ui.txtr_password.text()
            print(email,contraseña)
            stacked_widget.setCurrentIndex(0)  # Cambiar a la ventana de Login


###########################################################################################
# 21/05/23

class VentanaPrincipal(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self,parent)
        self.ui = MenuPrincipalUi()
        self.ui.setupUi(self)
        self.ui.botonI_menu.clicked.connect(self.mover_menu1)  # Conecta la señal del botón a la función mover_menu1()
        self.ui.botonm_cerrar.clicked.connect(app.quit)



        # # Conectar los botones de compra a la función mostrarEtiquetas ???? PRUEB>
        # for boton in self.findChildren(QPushButton, "botonComprar_*"):
        #     boton.clicked.connect(self.mostrarEtiquetas)



        # Crear un diccionario para mapear los botones con las páginas 
        self.page_mapping = {
            self.ui.botonpDesayunos: self.ui.page_desayunos,
            self.ui.botonpPowerWaters: self.ui.page_waters,
            self.ui.botonpZumos: self.ui.page_zumos,
            self.ui.botonpPlatosPreparados: self.ui.page_platos,
            self.ui.botonpCremas: self.ui.page_cremas,
            self.ui.botonpGummies: self.ui.page_gummies,
            self.ui.botonpFunctionalBars: self.ui.page_bars,
            self.ui.botonpTeaTox: self.ui.page_teatox,
            self.ui.botonpKombucha: self.ui.page_kombucha,
            self.ui.botonpShots: self.ui.page_shots
            
        }

        # Conectar clicked de cada botón a la función mostrarPage
        for boton, pagina in self.page_mapping.items():
            boton.clicked.connect(lambda _, p=pagina: self.mostrarPage(p))

    def mostrarPage(self, pagina):
        index = self.ui.frame_paginas.layout().itemAt(0).widget().indexOf(pagina)
        self.ui.frame_paginas.layout().itemAt(0).widget().setCurrentIndex(index)


    def mover_menu1(self):
        width = self.ui.frame_controlMenu.width()  # Obtener el ancho actual del frame_controlMenu
        normal = 0
        if width == 0:
            extender = 200  # Si el ancho es 0, establecer extender a 200
        else:
            extender = normal
        self.animacion = QPropertyAnimation(self.ui.frame_controlMenu, b'minimumWidth')  # Crear una animación de propiedad para cambiar el ancho mínimo del frame_controlMenu
        self.animacion.setDuration(300)  # Establecer la duración de la animación en 300 ms
        self.animacion.setStartValue(width)  # Establecer el valor inicial de la animación como el ancho actual
        self.animacion.setEndValue(extender)  # Establecer el valor final de la animación como extender
        self.animacion.setEasingCurve(QEasingCurve.InOutQuart)  # Establecer la curva de aceleración de la animación
        self.animacion.start()  # Iniciar la animación




################################################################################################
# 21/05/2023

    # def mostrarEtiquetas(self):
    #     boton_pulsado = self.sender()  # Obtener el botón que emitió la señal
    #     nombre_boton = boton_pulsado.objectName()  # Obtener el nombre del botón

    #     # Extraer el número del botón pulsado
    #     numero = int(nombre_boton.split("_")[1])

    #     frame_name = f"frame_{numero}"  # Construir el nombre del frame basado en el número del botón
    #     frame = getattr(self.ui, frame_name, None)  # Obtener el frame utilizando getattr() y asignar None si no se encuentra

    #     if frame is not None:
    #         etiquetas = frame.findChildren(QLabel)  # Encontrar todas las etiquetas dentro del frame
    #         etiquetas_nombres = [etiqueta.text() for etiqueta in etiquetas]  # Obtener los nombres de las etiquetas
    #         print(etiquetas_nombres)
    #     else:
    #         print(f"No se encontró el frame {frame_name}")


################################################################################################





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