# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'v4_ventanaUC.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1097, 688)
        MainWindow.setMinimumSize(QtCore.QSize(1097, 687))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame_principal = QtWidgets.QFrame(self.centralwidget)
        self.frame_principal.setGeometry(QtCore.QRect(0, 0, 1097, 687))
        self.frame_principal.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Raleway")
        self.frame_principal.setFont(font)
        self.frame_principal.setStyleSheet("#frame_principal {\n"
"  background-color:rgba(239,232,224,70);\n"
"  border-image: url(:/images/z_background_limonada.jpg);\n"
"}\n"
"QPushButton {\n"
"    background-color: rgba(233, 233, 232, 200);\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"    border-color: rgba(46, 82, 101, 200);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(239, 232, 224);\n"
"    border-top-left-radius: 20px;\n"
"    border-bottom-left-radius: 20px;\n"
"    color: rgb(0, 0, 0);\n"
"}\n"
"")
        self.frame_principal.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_principal.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_principal.setObjectName("frame_principal")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_principal)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_cabecera = QtWidgets.QFrame(self.frame_principal)
        self.frame_cabecera.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_cabecera.setMaximumSize(QtCore.QSize(16777215, 73))
        self.frame_cabecera.setStyleSheet("\n"
"#frame_cabecera{\n"
"background-color:rgba(239,232,224,70);\n"
"border:0px;\n"
"}")
        self.frame_cabecera.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_cabecera.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_cabecera.setObjectName("frame_cabecera")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_cabecera)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.botonuc_atras = QtWidgets.QPushButton(self.frame_cabecera)
        self.botonuc_atras.setMinimumSize(QtCore.QSize(47, 34))
        self.botonuc_atras.setStyleSheet("border-image: url(:/iconos/z_atras.png);\n"
"\n"
"background-color:   rgba(233,233,232,200);\n"
"border-style:solid;\n"
"border-width: 1px;\n"
"border-color:  rgba(46,82,101,200);\n"
"\n"
"\n"
"background-color:   rgb(239, 232, 224);\n"
"border-top-left-radius: 20px;\n"
"border-bottom-left-radius:20px;\n"
"color:rgb(0,0,0);\n"
"\n"
"")
        self.botonuc_atras.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/iconos/home.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.botonuc_atras.setIcon(icon)
        self.botonuc_atras.setDefault(False)
        self.botonuc_atras.setObjectName("botonuc_atras")
        self.horizontalLayout.addWidget(self.botonuc_atras)
        spacerItem = QtWidgets.QSpacerItem(282, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.labeluc_titulo = QtWidgets.QLabel(self.frame_cabecera)
        font = QtGui.QFont()
        font.setFamily("Raleway")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.labeluc_titulo.setFont(font)
        self.labeluc_titulo.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.labeluc_titulo.setStyleSheet("#label_titulo {\n"
"color: white;\n"
"font-size: 2rem;\n"
"\n"
"\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.labeluc_titulo.setTextFormat(QtCore.Qt.PlainText)
        self.labeluc_titulo.setAlignment(QtCore.Qt.AlignCenter)
        self.labeluc_titulo.setObjectName("labeluc_titulo")
        self.horizontalLayout.addWidget(self.labeluc_titulo)
        spacerItem1 = QtWidgets.QSpacerItem(177, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.botouc_usu = QtWidgets.QPushButton(self.frame_cabecera)
        self.botouc_usu.setMinimumSize(QtCore.QSize(47, 34))
        self.botouc_usu.setStyleSheet("")
        self.botouc_usu.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/iconos/user.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.botouc_usu.setIcon(icon1)
        self.botouc_usu.setObjectName("botouc_usu")
        self.horizontalLayout.addWidget(self.botouc_usu)
        self.botonuc_cerrar = QtWidgets.QPushButton(self.frame_cabecera)
        self.botonuc_cerrar.setMinimumSize(QtCore.QSize(47, 34))
        self.botonuc_cerrar.setStyleSheet("")
        self.botonuc_cerrar.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/iconos/z_cerrar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.botonuc_cerrar.setIcon(icon2)
        self.botonuc_cerrar.setObjectName("botonuc_cerrar")
        self.horizontalLayout.addWidget(self.botonuc_cerrar)
        self.verticalLayout_2.addWidget(self.frame_cabecera)
        self.frame_cuerpo = QtWidgets.QFrame(self.frame_principal)
        self.frame_cuerpo.setStyleSheet("#frame_cuerpo{\n"
"background-color:rgba(239,232,224,70);}\n"
"QPushButton{\n"
"background-color:   rgba(233,233,232,200);\n"
"border-style:solid;\n"
"border-width: 1px;\n"
"border-color:  rgba(46,82,101,200);\n"
"}\n"
"\n"
"\n"
"QPushButton:hover{\n"
"background-color:   rgb(122, 126, 116);\n"
"border-top-left-radius: 20px;\n"
"border-bottom-left-radius:20px;\n"
"color:rgb(0,0,0);\n"
"}\n"
"")
        self.frame_cuerpo.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_cuerpo.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_cuerpo.setObjectName("frame_cuerpo")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_cuerpo)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.stackedWidget = QtWidgets.QStackedWidget(self.frame_cuerpo)
        self.stackedWidget.setStyleSheet("background-color: transparent;\n"
"")
        self.stackedWidget.setObjectName("stackedWidget")
        self.pag_carrito = QtWidgets.QWidget()
        self.pag_carrito.setObjectName("pag_carrito")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.pag_carrito)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame_productos = QtWidgets.QFrame(self.pag_carrito)
        self.frame_productos.setMinimumSize(QtCore.QSize(517, 560))
        self.frame_productos.setStyleSheet("#frame_productos > [id^=\"frame_\"] {\n"
"  max-height: 130px;\n"
"}\n"
"")
        self.frame_productos.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_productos.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_productos.setObjectName("frame_productos")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_productos)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.scrollArea = QtWidgets.QScrollArea(self.frame_productos)
        self.scrollArea.setMinimumSize(QtCore.QSize(517, 0))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents_4 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_4.setGeometry(QtCore.QRect(0, 0, 515, 28))
        self.scrollAreaWidgetContents_4.setObjectName("scrollAreaWidgetContents_4")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_4)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_4)
        self.verticalLayout_4.addWidget(self.scrollArea)
        self.horizontalLayout_2.addWidget(self.frame_productos)
        self.frame_2 = QtWidgets.QFrame(self.pag_carrito)
        self.frame_2.setMinimumSize(QtCore.QSize(489, 560))
        self.frame_2.setStyleSheet("margin-right:10px;")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.lineEdit = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit.setGeometry(QtCore.QRect(20, 50, 301, 31))
        font = QtGui.QFont()
        font.setFamily("Raleway")
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"padding:3px;")
        self.lineEdit.setObjectName("lineEdit")
        self.botouc_validar = QtWidgets.QPushButton(self.frame_2)
        self.botouc_validar.setGeometry(QtCore.QRect(340, 50, 131, 35))
        self.botouc_validar.setMinimumSize(QtCore.QSize(25, 25))
        font = QtGui.QFont()
        font.setFamily("Raleway")
        self.botouc_validar.setFont(font)
        self.botouc_validar.setStyleSheet("QPushButton{\n"
"background-color:   rgba(233,233,232,200);\n"
"border-style:solid;\n"
"border-width: 1px;\n"
"border-color:  rgba(46,82,101,200);\n"
"\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton:hover{\n"
"background-color:   rgb(239, 232, 224);\n"
"border-top-left-radius: 20px;\n"
"border-bottom-left-radius:20px;\n"
"color:rgb(0,0,0);\n"
"\n"
"\n"
"}\n"
"")
        self.botouc_validar.setIcon(icon1)
        self.botouc_validar.setObjectName("botouc_validar")
        self.frame = QtWidgets.QFrame(self.frame_2)
        self.frame.setGeometry(QtCore.QRect(20, 110, 301, 115))
        font = QtGui.QFont()
        font.setFamily("Raleway")
        self.frame.setFont(font)
        self.frame.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setObjectName("gridLayout")
        self.label_subtotal = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Raleway")
        self.label_subtotal.setFont(font)
        self.label_subtotal.setObjectName("label_subtotal")
        self.gridLayout.addWidget(self.label_subtotal, 0, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(169, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 0, 1, 1, 1)
        self.label_subtotal_5 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Raleway")
        self.label_subtotal_5.setFont(font)
        self.label_subtotal_5.setObjectName("label_subtotal_5")
        self.gridLayout.addWidget(self.label_subtotal_5, 0, 2, 1, 1)
        self.label_subtotal_2 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Raleway")
        self.label_subtotal_2.setFont(font)
        self.label_subtotal_2.setObjectName("label_subtotal_2")
        self.gridLayout.addWidget(self.label_subtotal_2, 1, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(169, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 1, 1, 1, 1)
        self.label_subtotal_6 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Raleway")
        self.label_subtotal_6.setFont(font)
        self.label_subtotal_6.setObjectName("label_subtotal_6")
        self.gridLayout.addWidget(self.label_subtotal_6, 1, 2, 1, 1)
        self.label_subtotal_3 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Raleway")
        self.label_subtotal_3.setFont(font)
        self.label_subtotal_3.setObjectName("label_subtotal_3")
        self.gridLayout.addWidget(self.label_subtotal_3, 2, 0, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(169, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem4, 2, 1, 1, 1)
        self.label_subtotal_7 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Raleway")
        self.label_subtotal_7.setFont(font)
        self.label_subtotal_7.setObjectName("label_subtotal_7")
        self.gridLayout.addWidget(self.label_subtotal_7, 2, 2, 1, 1)
        self.botouc_finalizarPedido = QtWidgets.QPushButton(self.frame_2)
        self.botouc_finalizarPedido.setGeometry(QtCore.QRect(340, 140, 131, 35))
        self.botouc_finalizarPedido.setMinimumSize(QtCore.QSize(25, 25))
        font = QtGui.QFont()
        font.setFamily("Raleway")
        self.botouc_finalizarPedido.setFont(font)
        self.botouc_finalizarPedido.setStyleSheet("QPushButton{\n"
"background-color:   rgba(233,233,232,200);\n"
"border-style:solid;\n"
"border-width: 1px;\n"
"border-color:  rgba(46,82,101,200);\n"
"}\n"
"\n"
"\n"
"QPushButton:hover{\n"
"background-color:   rgb(239, 232, 224);\n"
"border-top-left-radius: 20px;\n"
"border-bottom-left-radius:20px;\n"
"color:rgb(0,0,0);\n"
"}\n"
"")
        self.botouc_finalizarPedido.setIcon(icon1)
        self.botouc_finalizarPedido.setObjectName("botouc_finalizarPedido")
        self.horizontalLayout_2.addWidget(self.frame_2)
        self.stackedWidget.addWidget(self.pag_carrito)
        self.pag_usuario = QtWidgets.QWidget()
        self.pag_usuario.setObjectName("pag_usuario")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.pag_usuario)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem5 = QtWidgets.QSpacerItem(235, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem5)
        self.tabWidget = QtWidgets.QTabWidget(self.pag_usuario)
        self.tabWidget.setMinimumSize(QtCore.QSize(550, 0))
        font = QtGui.QFont()
        font.setFamily("Raleway")
        self.tabWidget.setFont(font)
        self.tabWidget.setFocusPolicy(QtCore.Qt.NoFocus)
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setStyleSheet("QPushButton{\n"
"background-color:   rgba(233,233,232,200);\n"
"border-style:solid;\n"
"border-width: 1px;\n"
"border-color:  rgba(46,82,101,200);\n"
"padding:10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color:   rgb(239, 232, 224);\n"
"border-top-left-radius: 20px;\n"
"border-bottom-left-radius:20px;\n"
"color:rgb(0,0,0);\n"
"\n"
"}\n"
"QComboBox{\n"
"border:none;\n"
"border-width:0px;}\n"
"QComboBox::item:selected { color: rgb(241,152,31); }\n"
"QLineEdit{\n"
"border:none;\n"
"border-width:0px;\n"
"padding:3px;\n"
"}\n"
"QLabel{\n"
"padding:3px;\n"
"}\n"
"\n"
"*{background-color:rgb(255,255,255);}\n"
"")
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.groupBox = QtWidgets.QGroupBox(self.tab)
        font = QtGui.QFont()
        font.setFamily("Raleway")
        self.groupBox.setFont(font)
        self.groupBox.setAutoFillBackground(False)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.cbd_municipio = QtWidgets.QComboBox(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("Raleway")
        self.cbd_municipio.setFont(font)
        self.cbd_municipio.setObjectName("cbd_municipio")
        self.gridLayout_4.addWidget(self.cbd_municipio, 10, 3, 1, 1)
        self.cbd_provincia = QtWidgets.QComboBox(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("Raleway")
        self.cbd_provincia.setFont(font)
        self.cbd_provincia.setObjectName("cbd_provincia")
        self.gridLayout_4.addWidget(self.cbd_provincia, 5, 3, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(100, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem6, 0, 0, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(100, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem7, 3, 0, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(99, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem8, 0, 4, 1, 1)
        spacerItem9 = QtWidgets.QSpacerItem(100, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem9, 1, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("Raleway")
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout_4.addWidget(self.label_4, 3, 1, 1, 1)
        self.txtd_telefono = QtWidgets.QLineEdit(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("Raleway")
        self.txtd_telefono.setFont(font)
        self.txtd_telefono.setObjectName("txtd_telefono")
        self.gridLayout_4.addWidget(self.txtd_telefono, 3, 3, 1, 1)
        spacerItem10 = QtWidgets.QSpacerItem(99, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem10, 1, 4, 1, 1)
        spacerItem11 = QtWidgets.QSpacerItem(100, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem11, 2, 0, 1, 1)
        spacerItem12 = QtWidgets.QSpacerItem(99, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem12, 3, 4, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("Raleway")
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout_4.addWidget(self.label_3, 2, 1, 1, 1)
        spacerItem13 = QtWidgets.QSpacerItem(100, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem13, 10, 4, 1, 1)
        self.txtd_nombre = QtWidgets.QLineEdit(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("Raleway")
        self.txtd_nombre.setFont(font)
        self.txtd_nombre.setStyleSheet("margin-top:10px;")
        self.txtd_nombre.setObjectName("txtd_nombre")
        self.gridLayout_4.addWidget(self.txtd_nombre, 0, 3, 1, 1)
        self.txtd_apellidos = QtWidgets.QLineEdit(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("Raleway")
        self.txtd_apellidos.setFont(font)
        self.txtd_apellidos.setObjectName("txtd_apellidos")
        self.gridLayout_4.addWidget(self.txtd_apellidos, 1, 3, 1, 1)
        self.txtd_preseg = QtWidgets.QLineEdit(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("Raleway")
        self.txtd_preseg.setFont(font)
        self.txtd_preseg.setObjectName("txtd_preseg")
        self.gridLayout_4.addWidget(self.txtd_preseg, 21, 3, 1, 1)
        spacerItem14 = QtWidgets.QSpacerItem(99, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem14, 22, 4, 1, 1)
        self.txtd_contra = QtWidgets.QLineEdit(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("Raleway")
        self.txtd_contra.setFont(font)
        self.txtd_contra.setEchoMode(QtWidgets.QLineEdit.Password)
        self.txtd_contra.setObjectName("txtd_contra")
        self.gridLayout_4.addWidget(self.txtd_contra, 19, 3, 1, 1)
        spacerItem15 = QtWidgets.QSpacerItem(99, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem15, 21, 4, 1, 1)
        spacerItem16 = QtWidgets.QSpacerItem(99, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem16, 20, 4, 1, 1)
        spacerItem17 = QtWidgets.QSpacerItem(100, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem17, 22, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("Raleway")
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.gridLayout_4.addWidget(self.label_7, 20, 1, 1, 1)
        self.botonuc_update = QtWidgets.QPushButton(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("Raleway")
        self.botonuc_update.setFont(font)
        self.botonuc_update.setObjectName("botonuc_update")
        self.gridLayout_4.addWidget(self.botonuc_update, 23, 3, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("Raleway")
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout_4.addWidget(self.label_5, 4, 1, 1, 1)
        spacerItem18 = QtWidgets.QSpacerItem(99, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem18, 19, 4, 1, 1)
        spacerItem19 = QtWidgets.QSpacerItem(100, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem19, 19, 0, 1, 1)
        spacerItem20 = QtWidgets.QSpacerItem(100, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem20, 20, 0, 1, 1)
        self.txtd_dni = QtWidgets.QLineEdit(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("Raleway")
        self.txtd_dni.setFont(font)
        self.txtd_dni.setReadOnly(False)
        self.txtd_dni.setObjectName("txtd_dni")
        self.gridLayout_4.addWidget(self.txtd_dni, 2, 3, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("Raleway")
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.gridLayout_4.addWidget(self.label_6, 19, 1, 1, 1)
        spacerItem21 = QtWidgets.QSpacerItem(100, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem21, 4, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("Raleway")
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout_4.addWidget(self.label_2, 1, 1, 1, 1)
        self.txtd_confcontra = QtWidgets.QLineEdit(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("Raleway")
        self.txtd_confcontra.setFont(font)
        self.txtd_confcontra.setEchoMode(QtWidgets.QLineEdit.Password)
        self.txtd_confcontra.setObjectName("txtd_confcontra")
        self.gridLayout_4.addWidget(self.txtd_confcontra, 20, 3, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("Raleway")
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.gridLayout_4.addWidget(self.label_9, 21, 1, 1, 1)
        self.txtd_resseg = QtWidgets.QLineEdit(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("Raleway")
        self.txtd_resseg.setFont(font)
        self.txtd_resseg.setEchoMode(QtWidgets.QLineEdit.Password)
        self.txtd_resseg.setObjectName("txtd_resseg")
        self.gridLayout_4.addWidget(self.txtd_resseg, 22, 3, 1, 1)
        spacerItem22 = QtWidgets.QSpacerItem(99, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem22, 4, 4, 1, 1)
        spacerItem23 = QtWidgets.QSpacerItem(99, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem23, 18, 4, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("Raleway")
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.gridLayout_4.addWidget(self.label_10, 22, 1, 1, 1)
        self.txtd_direccion = QtWidgets.QLineEdit(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("Raleway")
        self.txtd_direccion.setFont(font)
        self.txtd_direccion.setObjectName("txtd_direccion")
        self.gridLayout_4.addWidget(self.txtd_direccion, 18, 3, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("Raleway")
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.gridLayout_4.addWidget(self.label_8, 18, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("Raleway")
        self.label.setFont(font)
        self.label.setStyleSheet("margin-top:10px;")
        self.label.setObjectName("label")
        self.gridLayout_4.addWidget(self.label, 0, 1, 1, 1)
        spacerItem24 = QtWidgets.QSpacerItem(100, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem24, 21, 0, 1, 1)
        spacerItem25 = QtWidgets.QSpacerItem(100, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem25, 18, 0, 1, 1)
        spacerItem26 = QtWidgets.QSpacerItem(99, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem26, 2, 4, 1, 1)
        self.cbd_CA = QtWidgets.QComboBox(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("Raleway")
        self.cbd_CA.setFont(font)
        self.cbd_CA.setStyleSheet("")
        self.cbd_CA.setObjectName("cbd_CA")
        self.gridLayout_4.addWidget(self.cbd_CA, 4, 3, 1, 1)
        spacerItem27 = QtWidgets.QSpacerItem(99, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem27, 10, 0, 1, 1)
        self.label_22 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("Raleway")
        self.label_22.setFont(font)
        self.label_22.setObjectName("label_22")
        self.gridLayout_4.addWidget(self.label_22, 10, 1, 1, 1)
        self.label_21 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("Raleway")
        self.label_21.setFont(font)
        self.label_21.setObjectName("label_21")
        self.gridLayout_4.addWidget(self.label_21, 5, 1, 1, 1)
        spacerItem28 = QtWidgets.QSpacerItem(99, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem28, 5, 0, 1, 1)
        spacerItem29 = QtWidgets.QSpacerItem(100, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem29, 5, 4, 1, 1)
        spacerItem30 = QtWidgets.QSpacerItem(99, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem30, 15, 0, 1, 1)
        self.label_23 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("Raleway")
        self.label_23.setFont(font)
        self.label_23.setObjectName("label_23")
        self.gridLayout_4.addWidget(self.label_23, 15, 1, 1, 1)
        spacerItem31 = QtWidgets.QSpacerItem(100, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem31, 15, 4, 1, 1)
        self.txtd_cp = QtWidgets.QLineEdit(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("Raleway")
        self.txtd_cp.setFont(font)
        self.txtd_cp.setObjectName("txtd_cp")
        self.gridLayout_4.addWidget(self.txtd_cp, 15, 3, 1, 1)
        self.verticalLayout_8.addWidget(self.groupBox)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.pushButton_2 = QtWidgets.QPushButton(self.tab_2)
        font = QtGui.QFont()
        font.setFamily("Raleway")
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout_5.addWidget(self.pushButton_2, 1, 1, 1, 1)
        self.tableWidget = QtWidgets.QTableWidget(self.tab_2)
        font = QtGui.QFont()
        font.setFamily("Raleway")
        self.tableWidget.setFont(font)
        self.tableWidget.setFocusPolicy(QtCore.Qt.TabFocus)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setGridStyle(QtCore.Qt.SolidLine)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Raleway")
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Raleway")
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Raleway")
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Raleway")
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(3, item)
        self.gridLayout_5.addWidget(self.tableWidget, 0, 0, 1, 2)
        self.tabWidget.addTab(self.tab_2, "")
        self.horizontalLayout_5.addWidget(self.tabWidget)
        spacerItem32 = QtWidgets.QSpacerItem(234, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem32)
        self.stackedWidget.addWidget(self.pag_usuario)
        self.page_productoDinamico = QtWidgets.QWidget()
        self.page_productoDinamico.setObjectName("page_productoDinamico")
        self.stackedWidget.addWidget(self.page_productoDinamico)
        self.verticalLayout_3.addWidget(self.stackedWidget)
        self.verticalLayout_2.addWidget(self.frame_cuerpo)
        self.verticalLayout_2.setStretch(0, 1)
        self.verticalLayout_2.setStretch(1, 8)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(1)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.labeluc_titulo.setText(_translate("MainWindow", "Resumen del pedido"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "INTRODUCE TU CÓDIGO DE DESCUENTO"))
        self.botouc_validar.setText(_translate("MainWindow", "Validar"))
        self.label_subtotal.setText(_translate("MainWindow", "Subtotal"))
        self.label_subtotal_5.setText(_translate("MainWindow", "0.00€"))
        self.label_subtotal_2.setText(_translate("MainWindow", "Descuento"))
        self.label_subtotal_6.setText(_translate("MainWindow", "DESCUENTO NO APLICADO"))
        self.label_subtotal_3.setText(_translate("MainWindow", "Total "))
        self.label_subtotal_7.setText(_translate("MainWindow", "0.00€"))
        self.botouc_finalizarPedido.setText(_translate("MainWindow", "FinalizarPedido"))
        self.groupBox.setTitle(_translate("MainWindow", "DATOS PERSONALES"))
        self.label_4.setText(_translate("MainWindow", "Teléfono"))
        self.label_3.setText(_translate("MainWindow", "DNI"))
        self.label_7.setText(_translate("MainWindow", "Confirme contraseña"))
        self.botonuc_update.setText(_translate("MainWindow", "Actualizar"))
        self.label_5.setText(_translate("MainWindow", "Comunidad Autónoma"))
        self.label_6.setText(_translate("MainWindow", "Contraseña"))
        self.label_2.setText(_translate("MainWindow", "Apellidos"))
        self.label_9.setText(_translate("MainWindow", "Pregunta de seguridad"))
        self.label_10.setText(_translate("MainWindow", "Respuesta de seguridad"))
        self.label_8.setText(_translate("MainWindow", "Dirección"))
        self.label.setText(_translate("MainWindow", "Nombre"))
        self.label_22.setText(_translate("MainWindow", "Municipio"))
        self.label_21.setText(_translate("MainWindow", "Provincia"))
        self.label_23.setText(_translate("MainWindow", "Codigo Postal"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Mis datos"))
        self.pushButton_2.setText(_translate("MainWindow", "Generar factura"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID Pedido"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Fecha"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Precio total "))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Usuario"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Mis pedidos"))
# import res_rc
