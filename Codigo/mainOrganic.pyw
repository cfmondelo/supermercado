import sys
from PyQt5 import QtWidgets
from v2_login import Ui_MainWindow as LoginUi
from v2_2_registrarse import Ui_MainWindow as CrearCuentaUi
from res import *




class Login(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self,parent)
        self.ui = LoginUi()
        self.ui.setupUi(self)
        self.ui.boton_entrar.clicked.connect(self.funcionLogin)
        self.ui.botonl_crearCuentaNueva.clicked.connect(self.cambiarDePantalla)
        self.ui.botonlCerrar.clicked.connect(app.quit)
        


    def funcionLogin(self):
        email=self.ui.txtl_usuario.text()
        password=self.ui.txtl_password.text()
        print("Ha iniciado correctamente: ", email, password)

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
        email=self.ui.txtr_email.text()
        if self.ui.txtr_password.text()==self.ui.txtr_confirmarPassword.text():
            contraseña=self.ui.txtr_password.text()
            print(email,contraseña)
            stacked_widget.setCurrentIndex(0)  # Cambiar a la ventana de Login


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