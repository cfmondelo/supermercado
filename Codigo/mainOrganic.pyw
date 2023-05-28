import sys
from PyQt5 import QtWidgets
from PyQt5.QtCore import QPropertyAnimation, QEasingCurve 
from PyQt5.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget, QPushButton 
from unidecode import unidecode
from v2_login import Ui_MainWindow as LoginUi
from v2_2_registrarse import Ui_MainWindow as CrearCuentaUi
from v3_menu import Ui_MainWindow as MenuPrincipalUi
from res import *
from metodosSupermercado import *




class Login(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self,parent)
        self.ui = LoginUi()
        self.ui.setupUi(self)
        # self.ui.boton_entrar.clicked.connect(self.funcionLogin)
        self.ui.boton_entrar.clicked.connect(self.cambiarAVentanaPrincipal)
        self.ui.botonl_crearCuentaNueva.clicked.connect(self.cambiarDePantalla)
        self.ui.botonlCerrar.clicked.connect(app.quit)
        


    def funcionLogin(self):
        email = self.ui.txtl_usuario.text().lower()
        password = self.ui.txtl_password.text()

        conexion = conectar()   
        usuarioOK = comprobarUsuario(conexion, email, password)
        if usuarioOK:
            showDialog("Login ok")
            self.cambiarAVentanaPrincipal
        else:
            showDialog("Datos incorrectos")
        desconectar(conexion)

        self.ui.txtl_usuario.clear()
        self.ui.txtl_password.clear()
        

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


###########################################################################################

class VentanaPrincipal(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self,parent)
        self.ui = MenuPrincipalUi()
        self.ui.setupUi(self)
        self.ui.botonI_menu.clicked.connect(self.mover_menu1)  # Conecta la señal del botón a la función mover_menu1()
        self.ui.botonm_cerrar.clicked.connect(app.quit)
        self.ui.botonm_lupa.clicked.connect(self.txtm_buscar)  # Boton pulsar

        # Agrego eventFilters a las etiquetas correspondientes
        self.ui.label_logo.installEventFilter(self)
        self.ui.labelm_imagenZumos_2.installEventFilter(self)
        self.ui.labelm_imagenShots.installEventFilter(self)
        self.ui.labelm_imagenTe.installEventFilter(self)
        self.ui.labelm_imagenBars.installEventFilter(self)


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


    # Cambio de pagina segun la label que pulse
    def eventFilter(self, obj, event):
        if event.type() == QtCore.QEvent.MouseButtonPress:
            if obj == self.ui.label_logo:
                self.mostrarPage(self.ui.page_inicio)
            elif obj == self.ui.labelm_imagenZumos_2:
                self.mostrarPage(self.ui.page_zumos)
            elif obj == self.ui.labelm_imagenShots:
                self.mostrarPage(self.ui.page_shots)
            elif obj == self.ui.labelm_imagenTe:
                self.mostrarPage(self.ui.page_teatox)
            elif obj == self.ui.labelm_imagenBars:
                self.mostrarPage(self.ui.page_bars)
            return True
        return super().eventFilter(obj, event)


    # Mostrar pagina
    def mostrarPage(self, pagina):
        index = self.ui.frame_paginas.layout().itemAt(0).widget().indexOf(pagina)
        self.ui.frame_paginas.layout().itemAt(0).widget().setCurrentIndex(index)

    # Mover menu 
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



    def obtener_nombres_etiquetas(self, paginas):
        nombres_etiquetas = []
        for pagina in paginas:
            etiquetas = pagina.findChildren(QtWidgets.QLabel)
            nombres_etiquetas.extend([etiqueta.objectName() for etiqueta in etiquetas])
        return nombres_etiquetas

    #Al pulsar sobre el boton buscar 
    def txtm_buscar(self):
        texto_busqueda = self.ui.txtm_buscar.text().lower()
        paginas = [
            self.ui.page_desayunos,
            self.ui.page_waters,
            self.ui.page_zumos,
            self.ui.page_platos,
            self.ui.page_cremas,
            self.ui.page_gummies,
            self.ui.page_bars,
            self.ui.page_teatox,
            self.ui.page_kombucha,
            self.ui.page_shots
        ]
        
        for pagina in paginas:
            for widget in pagina.findChildren(QtWidgets.QLabel):
                # texto_label = widget.text().lower()
                texto_label = unidecode(widget.text().lower())
                if texto_busqueda in texto_label:
                    self.mostrarPage(pagina)
                    return

        print("No se encontraron coincidencias")

        self.ui.txtm_buscar.clear()



###########################################################################################





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