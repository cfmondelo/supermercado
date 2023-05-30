# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'v4_ventanaUC.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from metodosSupermercado import *

class Ui_MainWindow(object):
    
    def carrito(self):
        i = 0
        conexion = conectar()
        prods = mostrarProductos(conexion)

        for prod in prods:
          i+=1
          self.frame_p = QtWidgets.QFrame(self.frame_productos)
          self.frame_p.setMaximumSize(QtCore.QSize(16777215, 130))
          self.frame_p.setStyleSheet("background-color: rgb(255, 255, 255);")
          self.frame_p.setFrameShape(QtWidgets.QFrame.StyledPanel)
          self.frame_p.setFrameShadow(QtWidgets.QFrame.Raised)
          self.frame_p.setObjectName("frame_p"+ str(i))

          self.horizontalLayout_prod = QtWidgets.QHBoxLayout(self.frame_p)
          self.horizontalLayout_prod.setObjectName("horizontalLayout_prod")

          self.frame_img = QtWidgets.QFrame(self.frame_p)
          self.frame_img.setFrameShape(QtWidgets.QFrame.StyledPanel)
          self.frame_img.setFrameShadow(QtWidgets.QFrame.Raised)
          self.frame_img.setObjectName("frame_img"+ str(i))

          self.verticalLayout_img = QtWidgets.QVBoxLayout(self.frame_img)
          self.verticalLayout_img.setObjectName("verticalLayout_img"+ str(i))

          self.label_imagen = QtWidgets.QLabel(self.frame_img)
          self.label_imagen.setStyleSheet("border-image: url(:"+ prod[6]+ ");")
          self.label_imagen.setText("")
          self.label_imagen.setObjectName("label_imagen"+ str(i))
          self.verticalLayout_img.addWidget(self.label_imagen)
          self.horizontalLayout_prod.addWidget(self.frame_img)

          self.frame_cont_prod = QtWidgets.QFrame(self.frame_p)
          self.frame_cont_prod.setFrameShape(QtWidgets.QFrame.StyledPanel)
          self.frame_cont_prod.setFrameShadow(QtWidgets.QFrame.Raised)
          self.frame_cont_prod.setObjectName("frame_cont"+ str(i))

          self.gridLayout_contprod = QtWidgets.QGridLayout(self.frame_cont_prod)
          self.gridLayout_contprod.setObjectName("gridLayout_contprod"+ str(i))

          self.label_tituloProducto = QtWidgets.QLabel(self.frame_cont_prod)
          self.label_tituloProducto.setObjectName("label_tituloProducto"+ str(i))
          self.gridLayout_contprod.addWidget(self.label_tituloProducto, 0, 0, 1, 2)

          self.numeric = QtWidgets.QSpinBox(self.frame_cont_prod)
          self.numeric.setObjectName("numeric"+ str(i))
          self.gridLayout_contprod.addWidget(self.numeric, 1, 0, 1, 1)

          self.label_precioProducto = QtWidgets.QLabel(self.frame_cont_prod)
          self.label_precioProducto.setObjectName("label_precioProducto"+ str(i))

          self.gridLayout_contprod.addWidget(self.label_precioProducto, 1, 1, 1, 1)

          self.horizontalLayout_prod.addWidget(self.frame_cont_prod)
          self.verticalLayout_4.addWidget(self.frame_p)

          
          _translate = QtCore.QCoreApplication.translate

          self.label_tituloProducto.setText( _translate("MainWindow", prod[1]))
          self.label_precioProducto.setText( _translate("MainWindow", str(prod[4])+ "€"))

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1097, 687)
        MainWindow.setMinimumSize(QtCore.QSize(1097, 687))

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")

        self.frame_principal = QtWidgets.QFrame(self.centralwidget)
        self.frame_principal.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_principal.setStyleSheet("\n"
                                           "#frame_principal {\n"
                                           "  border-image: url(:/images/z_background_limonada.jpg);\n"
                                           "  background-color: transparent;\n"
                                           "\n"
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
                                          "background-color:rgba(0,0,0,80);\n"
                                          "}")
        self.frame_cabecera.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_cabecera.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_cabecera.setObjectName("frame_cabecera")

        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_cabecera)
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.botonuc_atras = QtWidgets.QPushButton(self.frame_cabecera)
        self.botonuc_atras.setMinimumSize(QtCore.QSize(25, 25))
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
        icon.addPixmap(QtGui.QPixmap(":/iconos/user.png"),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.botonuc_atras.setIcon(icon)
        self.botonuc_atras.setObjectName("botonuc_atras")
        self.horizontalLayout.addWidget(self.botonuc_atras)

        spacerItem = QtWidgets.QSpacerItem(
            282, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)

        self.labeluc_titulo = QtWidgets.QLabel(self.frame_cabecera)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
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

        spacerItem1 = QtWidgets.QSpacerItem(
            177, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)

        self.botouc_minimizar = QtWidgets.QPushButton(self.frame_cabecera)
        self.botouc_minimizar.setMinimumSize(QtCore.QSize(25, 25))
        self.botouc_minimizar.setStyleSheet("")
        self.botouc_minimizar.setText("")
        self.botouc_minimizar.setIcon(icon)
        self.botouc_minimizar.setObjectName("botouc_minimizar")
        self.horizontalLayout.addWidget(self.botouc_minimizar)

        self.botouc_min = QtWidgets.QPushButton(self.frame_cabecera)
        self.botouc_min.setMinimumSize(QtCore.QSize(25, 25))
        self.botouc_min.setStyleSheet("")
        self.botouc_min.setText("")
        self.botouc_min.setIcon(icon)
        self.botouc_min.setObjectName("botouc_min")
        self.horizontalLayout.addWidget(self.botouc_min)
        
        self.botonuc_max = QtWidgets.QPushButton(self.frame_cabecera)
        self.botonuc_max.setMinimumSize(QtCore.QSize(25, 25))
        self.botonuc_max.setStyleSheet("")
        self.botonuc_max.setText("")
        self.botonuc_max.setIcon(icon)
        self.botonuc_max.setObjectName("botonuc_max")
        self.horizontalLayout.addWidget(self.botonuc_max)

        self.botonuc_cerrar = QtWidgets.QPushButton(self.frame_cabecera)
        self.botonuc_cerrar.setMinimumSize(QtCore.QSize(25, 25))
        self.botonuc_cerrar.setStyleSheet("")
        self.botonuc_cerrar.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/iconos/z_cerrar.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.botonuc_cerrar.setIcon(icon1)
        self.botonuc_cerrar.setObjectName("botonuc_cerrar")
        self.horizontalLayout.addWidget(self.botonuc_cerrar)
        self.verticalLayout_2.addWidget(self.frame_cabecera)

        self.frame_cuerpo = QtWidgets.QFrame(self.frame_principal)
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
        self.frame_productos.setStyleSheet("#frame_productos > [id^=\"frame_\"] {\n"
                                           "  max-height: 130px;\n"
                                           "}\n"
                                           "")
        self.frame_productos.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_productos.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_productos.setObjectName("frame_productos")

        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_productos)
        self.verticalLayout_4.setObjectName("verticalLayout_4")

        self.carrito()

        # self.frame_p_1 = QtWidgets.QFrame(self.frame_productos)
        # self.frame_p_1.setMaximumSize(QtCore.QSize(16777215, 130))
        # self.frame_p_1.setStyleSheet("background-color: rgb(255, 255, 255);")
        # self.frame_p_1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        # self.frame_p_1.setFrameShadow(QtWidgets.QFrame.Raised)
        # self.frame_p_1.setObjectName("frame_p_1")

        # self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_p_1)
        # self.horizontalLayout_3.setObjectName("horizontalLayout_3")

        # self.frame_3 = QtWidgets.QFrame(self.frame_p_1)
        # self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        # self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        # self.frame_3.setObjectName("frame_3")

        # self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_3)
        # self.verticalLayout_5.setObjectName("verticalLayout_5")

        # self.label_imagen = QtWidgets.QLabel(self.frame_3)
        # self.label_imagen.setStyleSheet(
        #     "border-image: url(:/Desayunos/z_desayuno1.jpg);")
        # self.label_imagen.setText("")
        # self.label_imagen.setObjectName("label_imagen")
        # self.verticalLayout_5.addWidget(self.label_imagen)
        # self.horizontalLayout_3.addWidget(self.frame_3)

        # self.frame_4 = QtWidgets.QFrame(self.frame_p_1)
        # self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        # self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        # self.frame_4.setObjectName("frame_4")

        # self.gridLayout_2 = QtWidgets.QGridLayout(self.frame_4)
        # self.gridLayout_2.setObjectName("gridLayout_2")

        # self.label_tituloProducto = QtWidgets.QLabel(self.frame_4)
        # self.label_tituloProducto.setObjectName("label_tituloProducto")
        # self.gridLayout_2.addWidget(self.label_tituloProducto, 0, 0, 1, 2)

        # self.spinBox = QtWidgets.QSpinBox(self.frame_4)
        # self.spinBox.setObjectName("spinBox")
        # self.gridLayout_2.addWidget(self.spinBox, 1, 0, 1, 1)

        # self.label_precioProducto = QtWidgets.QLabel(self.frame_4)
        # self.label_precioProducto.setObjectName("label_precioProducto")
        # self.gridLayout_2.addWidget(self.label_precioProducto, 1, 1, 1, 1)
        # self.horizontalLayout_3.addWidget(self.frame_4)
        # self.verticalLayout_4.addWidget(self.frame_p_1)



        # self.frame_p_2 = QtWidgets.QFrame(self.frame_productos)
        # self.frame_p_2.setMaximumSize(QtCore.QSize(16777215, 130))
        # self.frame_p_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        # self.frame_p_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        # self.frame_p_2.setFrameShadow(QtWidgets.QFrame.Raised)
        # self.frame_p_2.setObjectName("frame_p_2")

        # self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_p_2)
        # self.horizontalLayout_4.setObjectName("horizontalLayout_4")

        # self.frame_5 = QtWidgets.QFrame(self.frame_p_2)
        # self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        # self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        # self.frame_5.setObjectName("frame_5")

        # self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frame_5)
        # self.verticalLayout_6.setObjectName("verticalLayout_6")
        # self.label_imagen_2 = QtWidgets.QLabel(self.frame_5)
        # self.label_imagen_2.setStyleSheet(
        #     "border-image: url(:/Desayunos/z_desayuno1.jpg);")
        # self.label_imagen_2.setText("")
        # self.label_imagen_2.setObjectName("label_imagen_2")
        # self.verticalLayout_6.addWidget(self.label_imagen_2)
        # self.horizontalLayout_4.addWidget(self.frame_5)

        # self.frame_6 = QtWidgets.QFrame(self.frame_p_2)
        # self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        # self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        # self.frame_6.setObjectName("frame_6")

        # self.gridLayout_3 = QtWidgets.QGridLayout(self.frame_6)
        # self.gridLayout_3.setObjectName("gridLayout_3")

        # self.label_tituloProducto_2 = QtWidgets.QLabel(self.frame_6)
        # self.label_tituloProducto_2.setObjectName("label_tituloProducto_2")
        # self.gridLayout_3.addWidget(self.label_tituloProducto_2, 0, 0, 1, 2)

        # self.spinBox_2 = QtWidgets.QSpinBox(self.frame_6)
        # self.spinBox_2.setObjectName("spinBox_2")
        # self.gridLayout_3.addWidget(self.spinBox_2, 1, 0, 1, 1)

        # self.label_precioProducto_2 = QtWidgets.QLabel(self.frame_6)
        # self.label_precioProducto_2.setObjectName("label_precioProducto_2")
        # self.gridLayout_3.addWidget(self.label_precioProducto_2, 1, 1, 1, 1)
        # self.horizontalLayout_4.addWidget(self.frame_6)
        # self.verticalLayout_4.addWidget(self.frame_p_2)
        
        self.horizontalLayout_2.addWidget(self.frame_productos)

        self.frame_2 = QtWidgets.QFrame(self.pag_carrito)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")

        self.lineEdit = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit.setGeometry(QtCore.QRect(40, 50, 301, 31))
        self.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit.setObjectName("lineEdit")

        self.botouc_validar = QtWidgets.QPushButton(self.frame_2)
        self.botouc_validar.setGeometry(QtCore.QRect(370, 50, 121, 35))
        self.botouc_validar.setMinimumSize(QtCore.QSize(25, 25))
        self.botouc_validar.setStyleSheet(
            "background-color: rgb(255, 255, 127);")
        self.botouc_validar.setIcon(icon)
        self.botouc_validar.setObjectName("botouc_validar")

        self.frame = QtWidgets.QFrame(self.frame_2)
        self.frame.setGeometry(QtCore.QRect(40, 110, 301, 115))
        self.frame.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")

        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setObjectName("gridLayout")

        self.label_subtotal = QtWidgets.QLabel(self.frame)
        self.label_subtotal.setObjectName("label_subtotal")
        self.gridLayout.addWidget(self.label_subtotal, 0, 0, 1, 1)

        spacerItem2 = QtWidgets.QSpacerItem(
            169, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 0, 1, 1, 1)

        self.label_subtotal_5 = QtWidgets.QLabel(self.frame)
        self.label_subtotal_5.setObjectName("label_subtotal_5")
        self.gridLayout.addWidget(self.label_subtotal_5, 0, 2, 1, 1)

        self.label_subtotal_2 = QtWidgets.QLabel(self.frame)
        self.label_subtotal_2.setObjectName("label_subtotal_2")
        self.gridLayout.addWidget(self.label_subtotal_2, 1, 0, 1, 1)

        spacerItem3 = QtWidgets.QSpacerItem(
            169, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 1, 1, 1, 1)

        self.label_subtotal_6 = QtWidgets.QLabel(self.frame)
        self.label_subtotal_6.setObjectName("label_subtotal_6")
        self.gridLayout.addWidget(self.label_subtotal_6, 1, 2, 1, 1)

        self.label_subtotal_3 = QtWidgets.QLabel(self.frame)
        self.label_subtotal_3.setObjectName("label_subtotal_3")
        self.gridLayout.addWidget(self.label_subtotal_3, 2, 0, 1, 1)

        spacerItem4 = QtWidgets.QSpacerItem(
            169, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem4, 2, 1, 1, 1)

        self.label_subtotal_7 = QtWidgets.QLabel(self.frame)
        self.label_subtotal_7.setObjectName("label_subtotal_7")
        self.gridLayout.addWidget(self.label_subtotal_7, 2, 2, 1, 1)

        self.botouc_finalizarPedido = QtWidgets.QPushButton(self.frame_2)
        self.botouc_finalizarPedido.setGeometry(
            QtCore.QRect(370, 140, 121, 35))
        self.botouc_finalizarPedido.setMinimumSize(QtCore.QSize(25, 25))
        self.botouc_finalizarPedido.setStyleSheet(
            "background-color: rgb(255, 255, 127);")
        self.botouc_finalizarPedido.setIcon(icon)
        self.botouc_finalizarPedido.setObjectName("botouc_finalizarPedido")
        self.horizontalLayout_2.addWidget(self.frame_2)
        self.stackedWidget.addWidget(self.pag_carrito)

        self.pag_usuario = QtWidgets.QWidget()
        self.pag_usuario.setObjectName("pag_usuario")
        self.stackedWidget.addWidget(self.pag_usuario)
        self.verticalLayout_3.addWidget(self.stackedWidget)
        self.verticalLayout_2.addWidget(self.frame_cuerpo)
        self.verticalLayout_2.setStretch(0, 1)
        self.verticalLayout_2.setStretch(1, 8)
        self.verticalLayout.addWidget(self.frame_principal)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.labeluc_titulo.setText(_translate( "MainWindow", "Resumen del pedido"))

        # self.label_tituloProducto.setText( _translate("MainWindow", "TextLabel"))
        # self.label_precioProducto.setText( _translate("MainWindow", "TextLabel"))

        # self.label_tituloProducto_2.setText( _translate("MainWindow", "TextLabel"))
        # self.label_precioProducto_2.setText(_translate("MainWindow", "TextLabel"))

        self.botouc_validar.setText(_translate("MainWindow", "Validar"))

        self.label_subtotal.setText(_translate("MainWindow", "Subtotal"))
        self.label_subtotal_5.setText(_translate("MainWindow", "r_sub"))
        self.label_subtotal_2.setText(_translate("MainWindow", "Descuento"))
        self.label_subtotal_6.setText(_translate("MainWindow", "r_desc"))
        self.label_subtotal_3.setText(_translate("MainWindow", "Total "))
        self.label_subtotal_7.setText(_translate("MainWindow", "r_total"))
        self.botouc_finalizarPedido.setText(
            _translate("MainWindow", "FinalizarPedido"))
# import res_rc
