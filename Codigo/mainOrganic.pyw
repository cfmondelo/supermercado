import sys
from PyQt5 import QtWidgets
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import QPropertyAnimation, QEasingCurve 
from PyQt5.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget, QPushButton 
from unidecode import unidecode
from v2_login import Ui_MainWindow as LoginUi
from v2_2_registrarse import Ui_MainWindow as CrearCuentaUi
from v3_menu import Ui_MainWindow as MenuPrincipalUi
from v4_ventanaUC import Ui_MainWindow as VentanaUCUi
from res import *
from metodosSupermercado import *

from PyQt5 import QtWidgets, QtGui





# INDEX 0
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
        
        


# INDEX 1
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




# INDEX 2
class VentanaPrincipal(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self,parent)
        self.ui = MenuPrincipalUi()
        self.ui.setupUi(self)
        self.ui.botonI_menu.clicked.connect(self.mover_menu1)  # Conecta la señal del botón a la función mover_menu1()
        self.ui.botonm_cerrar.clicked.connect(app.quit)
        self.ui.botonm_lupa.clicked.connect(self.txtm_buscar)  # Boton pulsar
        self.ui.botonm_carrito.clicked.connect(self.cambiar_ventanaUC)



        # self.ui.botonm_usuario.clicked.connect(self.cambiar_ventanaUC)
        # self.ventanaUC = None
   

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


                # Código para crear frames en frame_productos según productosKenia



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
        # texto_busqueda = self.ui.txtm_buscar.text().lower()
        texto_busqueda = unidecode(self.ui.txtm_buscar.text().lower())


        # Limpiar el contenido actual del scroll area
        scroll_layout = self.ui.scrollArea_13.widget().layout()
        if scroll_layout:
            while scroll_layout.count():
                child = scroll_layout.takeAt(0)
                if child.widget():
                    child.widget().deleteLater()

        conexion = conectar()
        prods = mostrarProductos(conexion)

        # Obtener los títulos de productos de la lista de tuplas prods
        # titulos_productos = [unidecode(tupla[1]) for tupla in prods]


        s_layout=self.ui.scrollAreaWidgetContents_13.layout()
        
        contador_frames = 0  # Contador para asignar nombres únicos a los marcos

        for tupla in prods:
            titulo = unidecode(tupla[1])
            # Obtener los demás datos de la tupla
            descrip = tupla[2]
            categ = tupla[3]
            precio = tupla[4]
            cant = tupla[5]
            img = tupla[6]

            if texto_busqueda in titulo.lower():

        #         print(texto_busqueda)

# CREO FRAME DEL PRODUCTO A BUSCAR
                frame_busqueda = QtWidgets.QFrame(self.ui.scrollAreaWidgetContents_13)
                frame_busqueda.setMinimumSize(QtCore.QSize(230, 270))
                frame_busqueda.setMaximumSize(QtCore.QSize(230, 270))
                frame_busqueda.setFrameShape(QtWidgets.QFrame.StyledPanel)
                frame_busqueda.setFrameShadow(QtWidgets.QFrame.Raised)
                frame_busqueda.setObjectName(f"frame_busqueda{contador_frames}")
                # frame_busqueda.setStyleSheet("background-color: rgb(71, 87, 78);")
                # frame_busqueda.setStyleSheet("background-color:  rgb(162, 187, 173);")
                

                # Distribucion del frame_busqueda
                verticalLayout_63 = QtWidgets.QVBoxLayout(frame_busqueda)
                verticalLayout_63.setObjectName("verticalLayout_63")

                # Añado el frame creado al layout del scroll
                s_layout.addWidget(frame_busqueda)


# CREO EL LABEL IMAGEN  en el frma creado con tamaño , stylesheet, texto, distribucion
                labelb_ = QtWidgets.QLabel(frame_busqueda)
                labelb_.setMinimumSize(QtCore.QSize(200, 150))
                labelb_.setMaximumSize(QtCore.QSize(200, 150))
                ruta = "border-image: url(:/{}/{})".format(categ, img)
                labelb_.setStyleSheet(ruta)
                labelb_.setText("")
                labelb_.setObjectName(f"labelb_{contador_frames}")

                # Añado imagen a la distribucion creada para el frame_busqueda
                verticalLayout_63.addWidget(labelb_)


# CREO LA LABEL PARA EL TITULO
                labelt_= QtWidgets.QLabel(frame_busqueda)
                labelt_.setMaximumSize(QtCore.QSize(16777215, 15))
                font = QtGui.QFont()
                font.setBold(True)
                font.setWeight(75)
                font.setStyleStrategy(QtGui.QFont.PreferDefault)
                labelt_.setFont(font)
                labelt_.setText(titulo)
                labelt_.setObjectName(f"labelt_{contador_frames}")

                #Añado la titulo a la distribucion del  frame_busqueda
                verticalLayout_63.addWidget(labelt_)


# CREO LA LABEL PARA EL PRECIO
                labelp_ = QtWidgets.QLabel(frame_busqueda)
                labelp_.setMaximumSize(QtCore.QSize(16777215, 15))
                font = QtGui.QFont()
                font.setBold(True)
                font.setWeight(75)
                labelp_.setFont(font)
                labelp_.setText(str(precio)+"€")
                labelp_.setObjectName(f"labelp_{contador_frames}")

                #Añado precio a la distribucion del  frame_busqueda
                verticalLayout_63.addWidget(labelp_)

# CREO EL BOTON COMPRAR
                botonc_ = QtWidgets.QPushButton(frame_busqueda)
                botonc_.setMinimumSize(QtCore.QSize(200, 34))
                botonc_.setMaximumSize(QtCore.QSize(200, 34))
                botonc_.setObjectName(f"botonc_{contador_frames}")
                botonc_.setText("Comprar")

                #Añado el botn a la distribucion del  frame_busqueda
                verticalLayout_63.addWidget(botonc_)

    # NO ME FUNCIONA El grid layout
                # #Añade al frame del producto creado a la disposicion de grid 
                # self.gridLayout_11.addWidget(frame_busqueda, contador_frames // 3, contador_frames % 3, 1, 1)

                contador_frames += 1



        # Mostrar la página de búsqueda en el scroll area
        self.mostrarPage(self.ui.page_busquedas)
        self.ui.txtm_buscar.clear()



    def cambiar_ventanaUC(self):
        ventanaUC = VentanaUC()
        stacked_widget.addWidget(ventanaUC)
        stacked_widget.setCurrentIndex(3)



#### ---> PROBLEMAS PARA LA KENIA DEL FUTURO

##### NO SE HACERLO  Y ME ESTOY LIANDO Y YA NO SE PENSAR- QUIERO QUE AL PULSAR SOBRE EL BOTON USUARIO LLAME A LA OTRA VENTANA A LA V4 PERO QUE SE VAYA A LA PAG DE USUARIO
        # # Llamar a la función ventanaUsuario si el botón pulsado es botonm_usuario
        # if self.sender() == self.ui.botonm_usuario:
        #     self.ventanaUsuario()

    # def ventanaUsuario(self):
    #     if self.ventanaUC:
    #         stacked_widget_uc = self.ventanaUC.ui.frame_cuerpo.findChild(QtWidgets.QStackedWidget)
    #         if stacked_widget_uc:
    #             index_pag_usuario = 2  # Índice de la página 'pag_usuario' dentro de stacked_widget_uc
    #             stacked_widget_uc.setCurrentIndex(index_pag_usuario)






# INDEX 3
class VentanaUC(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = VentanaUCUi()
        self.ui.setupUi(self)
        self.ui.botonuc_cerrar.clicked.connect(app.quit)
        self.ui.botonuc_atras.clicked.connect(self.cambiarAVentanaPrincipal)
        self.ui.botouc_validar.clicked.connect(self.comprobarDescuento)
        
        #variable del objeto
        self.descuento=0

        # Código para crear frames en frame_productos según productosKenia
        conexion = conectar()
        prods = mostrarCarrito(conexion)

        if len(prods) > 0:
            scroll_layout = self.ui.scrollAreaWidgetContents_4.layout()

            precioTot = 0

            for i, prod in enumerate(prods):
                precioTot += prod[2] * prod[3]

                
    #AÑADE FRAME PRODUCTO AL SCROLL AREA ------------------------->
                frame_p = QtWidgets.QFrame(self.ui.scrollAreaWidgetContents_4)
                frame_p.setMaximumSize(QtCore.QSize(16777215, 130))
                frame_p.setMinimumHeight(150)
                frame_p.setStyleSheet("background-color: rgb(255, 255, 255);")
                frame_p.setFrameShape(QtWidgets.QFrame.StyledPanel)
                frame_p.setFrameShadow(QtWidgets.QFrame.Raised)
                frame_p.setObjectName("frame_p" + str(i))

    #Creo una distribucion horizontal para la imagen y los datos
                horizontalLayout_prod = QtWidgets.QHBoxLayout(frame_p)
                horizontalLayout_prod.setObjectName("horizontalLayout_prod")

                scroll_layout.addWidget(frame_p)

    # AÑADE FRAME PARA IAMGEN --------------------------->
                frame_img = QtWidgets.QFrame(frame_p)
                frame_img.setFrameShape(QtWidgets.QFrame.StyledPanel)
                frame_img.setFrameShadow(QtWidgets.QFrame.Raised)
                frame_img.setObjectName("frame_img" + str(i))
                # frame_img.setStyleSheet("background-color: rgb(255, 0, 0);")


    #Creo distribucion para la imagen dentro del frame
                horizontalLayout_img = QtWidgets.QHBoxLayout(frame_img)
                horizontalLayout_img.setObjectName("horizontalLayout_img" + str(i))


                #Añade la imagen al frame 2
                label_imagen = QtWidgets.QLabel(frame_img)
                categoria=(str(prod[1]))
                name=(str(prod[4]))
                ruta = "border-image: url(:/{}/{})".format(categoria, name)
                label_imagen.setStyleSheet(ruta)
                label_imagen.setText("")
                label_imagen.setObjectName("label_imagen" + str(i))

    #Introduzco la distribucion para el frame producto y para la imagen 
                horizontalLayout_img.addWidget(label_imagen)
                horizontalLayout_prod.addWidget(frame_img)



    #AÑADE EL FRAME DE DATOS PRODUCTO ----------------------------->
                frame_cont_prod = QtWidgets.QFrame(frame_p)
                frame_cont_prod.setFrameShape(QtWidgets.QFrame.StyledPanel)
                frame_cont_prod.setFrameShadow(QtWidgets.QFrame.Raised)
                frame_cont_prod.setObjectName("frame_cont" + str(i))
                # frame_cont_prod.setStyleSheet("background-color: rgb(0, 255, 0);")

    #Hago que el Frame imagen y datos este pegados horizontal
                horizontalLayout_prod.addWidget(frame_cont_prod)


    #Añado sitribucion vertical dentro del frame de datos
                verticalLayout_contprod = QtWidgets.QVBoxLayout(frame_cont_prod)
                verticalLayout_contprod.setObjectName("verticalLayout_contprod" + str(i))
            
    #Añado titulo de producto
                label_tituloProducto = QtWidgets.QLabel(frame_cont_prod)
                label_tituloProducto.setObjectName("label_tituloProducto" + str(i))
                label_tituloProducto.setFixedHeight(20)
                # label_tituloProducto.setStyleSheet("background-color: blue;")

    #Añado el titulo a la distribucion vertical
                verticalLayout_contprod.addWidget(label_tituloProducto)

    #Añado un fram para precio y cantidad
                frame_cant_precio = QtWidgets.QFrame(frame_cont_prod)
                frame_cant_precio.setFrameShape(QtWidgets.QFrame.StyledPanel)
                frame_cant_precio.setFrameShadow(QtWidgets.QFrame.Raised)
                frame_cant_precio.setObjectName("frame_cant_precio" + str(i))           
                # frame_cant_precio.setStyleSheet("background-color: grey;")

    #Añado Frame precio cantidad a la distribucion vertical
                verticalLayout_contprod.addWidget(frame_cant_precio)

    #Añado distribucion horizontal al frame precio cant       
                horizontalLayout_cant_precio = QtWidgets.QHBoxLayout(frame_cant_precio)
                horizontalLayout_cant_precio.setObjectName("horizontalLayout_cant_precio" + str(i))


    #Creo spinbox y le añado distribucion 
                numeric = QtWidgets.QSpinBox(frame_cont_prod)
                numeric.setMinimum(1)
                numeric.setObjectName("numeric" + str(i))
                numeric.setValue(prod[3])
                horizontalLayout_cant_precio.addWidget(numeric)


    # Añado etiqueta precio y le añado distribucion 
                label_precioProducto = QtWidgets.QLabel(frame_cont_prod)
                label_precioProducto.setObjectName("label_precioProducto" + str(i))
                horizontalLayout_cant_precio.addWidget(label_precioProducto)

                _translate = QtCore.QCoreApplication.translate
                label_tituloProducto.setText(_translate("MainWindow", prod[0]))
                label_precioProducto.setText(_translate("MainWindow", str(prod[2]) + "€"))
                # numeric.setValue(prod[5]) --> No lo quiero 



    # CODIGO DE ANDREA - LO COMENTO PORQUE SINO NO ME FUNCIONA
            # try:
                precioSub = precioTot - (21 * precioTot/100)
            # except Exception as ex:
            #     print(ex)
            #funcionalidad botón VALIDAR. NO FUNCIONA, ME DA ERROR
        else:
            frame_p = QtWidgets.QFrame(self.ui.scrollAreaWidgetContents_4)
            frame_p.setMaximumSize(QtCore.QSize(16777215, 130))
            frame_p.setMinimumHeight(150)
            frame_p.setMinimumWidth(517)
            frame_p.setStyleSheet("background-color: rgb(255, 255, 255);")
            frame_p.setFrameShape(QtWidgets.QFrame.StyledPanel)
            frame_p.setFrameShadow(QtWidgets.QFrame.Raised)
            frame_p.setObjectName("frame_p")
            
            label_noprod = QtWidgets.QLabel(frame_p)
            label_noprod.setStyleSheet(" text-align:center;")
            label_noprod.setText("No hay productos en el carrito")
            label_noprod.setObjectName("label_noprod")

            precioTot = 0
            precioSub = 0

        _translate = QtCore.QCoreApplication.translate
        total = QtWidgets.QLabel(self.ui.label_subtotal_7)
        subtotal = QtWidgets.QLabel(self.ui.label_subtotal_5)
        total.setText(_translate("MainWindow", str(precioTot)+"€"))
        subtotal.setText(_translate("MainWindow", str(precioSub)+"€"))
        
        
    def cambiarAVentanaPrincipal(self):
        stacked_widget.setCurrentIndex(2)

    def comprobarDescuento(self):
        try:
            conexion=conectar()
            cupon=self.ui.lineEdit.text()
            self.descuento=comprobarCupon(conexion,cupon)
            self.ui.label_subtotal_6.setText(str(self.descuento))
        except Exception as ex:
            print(ex)
        

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

    