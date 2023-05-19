# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'v2_2_registrarse.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(617, 567)
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
        self.label_6 = QtWidgets.QLabel(self.widget)
        self.label_6.setGeometry(QtCore.QRect(40, 30, 280, 430))
        self.label_6.setStyleSheet("border-image: url(:/images/5.jpg);\n"
"border-image: url(:/images/z_background-login.jpg);\n"
"border-top-left-radius:50px;")
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.widget)
        self.label_7.setGeometry(QtCore.QRect(40, 30, 280, 430))
        self.label_7.setStyleSheet("background-color:rgba(0,0,0,80);\n"
"border-top-left-radius:50px;")
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.widget)
        self.label_8.setGeometry(QtCore.QRect(270, 30, 240, 430))
        self.label_8.setStyleSheet("background-color:rgba(255,255,255,255);\n"
"border-bottom-right-radius: 50px;\n"
"")
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")
        self.labelr_registrarse = QtWidgets.QLabel(self.widget)
        self.labelr_registrarse.setGeometry(QtCore.QRect(290, 50, 191, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.labelr_registrarse.setFont(font)
        self.labelr_registrarse.setStyleSheet("color:rgba(0,0,0,200);")
        self.labelr_registrarse.setObjectName("labelr_registrarse")
        self.txtr_usuario = QtWidgets.QLineEdit(self.widget)
        self.txtr_usuario.setGeometry(QtCore.QRect(290, 110, 190, 40))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.txtr_usuario.setFont(font)
        self.txtr_usuario.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46,82,101,200);\n"
"color:rgba(0,0,0,240);\n"
"padding-bottom:7px;")
        self.txtr_usuario.setObjectName("txtr_usuario")
        self.txtr_password = QtWidgets.QLineEdit(self.widget)
        self.txtr_password.setGeometry(QtCore.QRect(290, 190, 190, 40))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.txtr_password.setFont(font)
        self.txtr_password.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46,82,101,200);\n"
"color:rgba(0,0,0,240);\n"
"padding-bottom:7px;")
        self.txtr_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.txtr_password.setObjectName("txtr_password")
        self.botonr_entrar = QtWidgets.QPushButton(self.widget)
        self.botonr_entrar.setGeometry(QtCore.QRect(290, 380, 190, 40))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.botonr_entrar.setFont(font)
        self.botonr_entrar.setStyleSheet("background-color:   rgba(233,233,232,200);\n"
"border-style:solid;\n"
"border-width: 1px;\n"
"border-color:  rgba(46,82,101,200);")
        self.botonr_entrar.setObjectName("botonr_entrar")
        self.txtr_confirmarPassword = QtWidgets.QLineEdit(self.widget)
        self.txtr_confirmarPassword.setGeometry(QtCore.QRect(290, 230, 190, 40))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.txtr_confirmarPassword.setFont(font)
        self.txtr_confirmarPassword.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46,82,101,200);\n"
"color:rgba(0,0,0,240);\n"
"padding-bottom:7px;")
        self.txtr_confirmarPassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.txtr_confirmarPassword.setObjectName("txtr_confirmarPassword")
        self.txtr_respuestaSeguridad = QtWidgets.QLineEdit(self.widget)
        self.txtr_respuestaSeguridad.setGeometry(QtCore.QRect(290, 310, 190, 40))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.txtr_respuestaSeguridad.setFont(font)
        self.txtr_respuestaSeguridad.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46,82,101,200);\n"
"color:rgba(0,0,0,240);\n"
"padding-bottom:7px;")
        self.txtr_respuestaSeguridad.setEchoMode(QtWidgets.QLineEdit.Password)
        self.txtr_respuestaSeguridad.setObjectName("txtr_respuestaSeguridad")
        self.txtr_email = QtWidgets.QLineEdit(self.widget)
        self.txtr_email.setGeometry(QtCore.QRect(290, 150, 190, 40))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.txtr_email.setFont(font)
        self.txtr_email.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46,82,101,200);\n"
"color:rgba(0,0,0,240);\n"
"padding-bottom:7px;")
        self.txtr_email.setObjectName("txtr_email")
        self.txtr_preguntaSeguridad = QtWidgets.QLineEdit(self.widget)
        self.txtr_preguntaSeguridad.setGeometry(QtCore.QRect(290, 270, 190, 40))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.txtr_preguntaSeguridad.setFont(font)
        self.txtr_preguntaSeguridad.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46,82,101,200);\n"
"color:rgba(0,0,0,240);\n"
"padding-bottom:7px;")
        self.txtr_preguntaSeguridad.setObjectName("txtr_preguntaSeguridad")
        self.botonrCerrar = QtWidgets.QPushButton(self.widget)
        self.botonrCerrar.setGeometry(QtCore.QRect(470, 40, 31, 31))
        self.botonrCerrar.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../Iconos/x.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.botonrCerrar.setIcon(icon)
        self.botonrCerrar.setObjectName("botonrCerrar")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.labelr_registrarse.setText(_translate("MainWindow", "Registrarse"))
        self.txtr_usuario.setPlaceholderText(_translate("MainWindow", "Nombre de usuario"))
        self.txtr_password.setPlaceholderText(_translate("MainWindow", "Contraseña"))
        self.botonr_entrar.setText(_translate("MainWindow", "Entrar"))
        self.txtr_confirmarPassword.setPlaceholderText(_translate("MainWindow", "Confirme su contraseña"))
        self.txtr_respuestaSeguridad.setPlaceholderText(_translate("MainWindow", "Respuesta de seguridad"))
        self.txtr_email.setPlaceholderText(_translate("MainWindow", "Email"))
        self.txtr_preguntaSeguridad.setPlaceholderText(_translate("MainWindow", "Pregunta de seguridad"))
# import res_rc
