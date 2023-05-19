# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'v2_login.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(625, 567)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(30, 30, 550, 500))
        self.widget.setStyleSheet("QPushButton#pushButton:pressed{\n"
"    padding-left:5px;\n"
"    padding-top:5px;\n"
"    background-color:rgba(150,123,111,255);\n"
"}\n"
"\n"
"QPushButton#pushButton_2:pressed{\n"
"    padding-left:5px;\n"
"    padding-top:5px;\n"
"    background-color:rgba(91,88,53,255);\n"
"}\n"
"")
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(40, 30, 280, 430))
        self.label.setStyleSheet("border-image: url(:/images/5.jpg);\n"
"border-image: url(:/images/z_background-login.jpg);\n"
"border-top-left-radius:50px;")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(40, 30, 280, 430))
        self.label_2.setStyleSheet("background-color:rgba(0,0,0,80);\n"
"border-top-left-radius:50px;")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(270, 30, 240, 430))
        self.label_3.setStyleSheet("background-color:rgba(255,255,255,255);\n"
"border-bottom-right-radius: 50px;\n"
"")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.labell_login = QtWidgets.QLabel(self.widget)
        self.labell_login.setGeometry(QtCore.QRect(330, 50, 131, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.labell_login.setFont(font)
        self.labell_login.setStyleSheet("color:rgba(0,0,0,200);")
        self.labell_login.setObjectName("labell_login")
        self.txtl_usuario = QtWidgets.QLineEdit(self.widget)
        self.txtl_usuario.setGeometry(QtCore.QRect(290, 130, 190, 40))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.txtl_usuario.setFont(font)
        self.txtl_usuario.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46,82,101,200);\n"
"color:rgba(0,0,0,240);\n"
"padding-bottom:7px;")
        self.txtl_usuario.setObjectName("txtl_usuario")
        self.txtl_password = QtWidgets.QLineEdit(self.widget)
        self.txtl_password.setGeometry(QtCore.QRect(290, 200, 190, 40))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.txtl_password.setFont(font)
        self.txtl_password.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46,82,101,200);\n"
"color:rgba(0,0,0,240);\n"
"padding-bottom:7px;")
        self.txtl_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.txtl_password.setObjectName("txtl_password")
        self.boton_entrar = QtWidgets.QPushButton(self.widget)
        self.boton_entrar.setGeometry(QtCore.QRect(290, 260, 190, 40))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.boton_entrar.setFont(font)
        self.boton_entrar.setStyleSheet("background-color:   rgba(233,233,232,200);\n"
"border-style:solid;\n"
"border-width: 1px;\n"
"border-color:  rgba(46,82,101,200);")
        self.boton_entrar.setObjectName("boton_entrar")
        self.labell_olvidastePassword = QtWidgets.QLabel(self.widget)
        self.labell_olvidastePassword.setGeometry(QtCore.QRect(330, 310, 131, 16))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.labell_olvidastePassword.setFont(font)
        self.labell_olvidastePassword.setStyleSheet("color:rgba(0,0,0,210);")
        self.labell_olvidastePassword.setObjectName("labell_olvidastePassword")
        self.botonl_crearCuentaNueva = QtWidgets.QPushButton(self.widget)
        self.botonl_crearCuentaNueva.setGeometry(QtCore.QRect(290, 340, 190, 40))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.botonl_crearCuentaNueva.setFont(font)
        self.botonl_crearCuentaNueva.setStyleSheet("background-color:   rgba(233,233,232,200);\n"
"border-style:solid;\n"
"border-width: 1px;\n"
"border-color:  rgba(46,82,101,200);")
        self.botonl_crearCuentaNueva.setObjectName("botonl_crearCuentaNueva")
        self.botonlCerrar = QtWidgets.QPushButton(self.widget)
        self.botonlCerrar.setGeometry(QtCore.QRect(470, 40, 31, 31))
        self.botonlCerrar.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../Iconos/cerrar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.botonlCerrar.setIcon(icon)
        self.botonlCerrar.setObjectName("botonlCerrar")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.labell_login.setText(_translate("MainWindow", "Log In"))
        self.txtl_usuario.setPlaceholderText(_translate("MainWindow", "Email"))
        self.txtl_password.setPlaceholderText(_translate("MainWindow", "Contraseña"))
        self.boton_entrar.setText(_translate("MainWindow", "Entrar"))
        self.labell_olvidastePassword.setText(_translate("MainWindow", "¿Has olvidado tu contraseña?"))
        self.botonl_crearCuentaNueva.setText(_translate("MainWindow", "Crear nueva cuenta "))
# import res_rc
