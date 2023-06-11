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
from functools import partial
from datetime import date
from pasarFactura import *




# INDEX 0
class Login(QtWidgets.QMainWindow):
    
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self,parent)
        self.ui = LoginUi()
        self.ui.setupUi(self)
            
        # icon = QtGui.QIcon(':/iconos/logo_naranja.png')
        # self.setWindowIcon(icon)
        self.ui.boton_entrar.clicked.connect(self.funcionLogin)
        # self.ui.boton_entrar.clicked.connect(self.cambiarAVentanaPrincipal)
        self.ui.botonl_crearCuentaNueva.clicked.connect(self.cambiarDePantalla)
        self.ui.botonlCerrar.clicked.connect(app.quit)
        self.__email=""


    def funcionLogin(self):
        self.__email = self.ui.txtl_usuario.text().lower()
        password = self.ui.txtl_password.text()

        conexion = conectar()   
        usuarioOK = comprobarUsuario(conexion, self.__email, password)
        if usuarioOK:
            self.cambiarAVentanaPrincipal()
        else:
            showDialog("Datos incorrectos")
        desconectar(conexion)

        self.ui.txtl_usuario.clear()
        self.ui.txtl_password.clear()
        
    def getEmail(self):
        return self.__email

    def cambiarDePantalla(self):
        crear_cuenta = CrearCuenta()
        # stacked_widget.addWidget(crear_cuenta)
        stacked_widget.setCurrentIndex(1)

    def cambiarAVentanaPrincipal(self):
        ventanaPrincipal = VentanaPrincipal()
        # stacked_widget.addWidget(ventanaPrincipal)
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
        try:
            
            usuario    = self.ui.txtr_usuario.text()
            contra     = self.ui.txtr_password.text()
            contraRepe = self.ui.txtr_confirmarPassword.text()
            email      = self.ui.txtr_email.text().lower()
            preSeg     = self.ui.txtr_preguntaSeguridad.text()
            resSeg     = self.ui.txtr_respuestaSeguridad.text()

            datos = (email, usuario, contra, contraRepe, preSeg, resSeg)
            vacio = camposVacios(datos)
            
            if vacio:
                showDialog("Debe rellenar todos los datos")
            elif len(contra) < 8:
                showDialog("La contraseña debe tener al menos 8 caracteres")
            elif contra != contraRepe:
                showDialog("El campo de confirmación de contraseña debe ser igual al de contraseña")
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
        except Exception as ex:
            print(ex)




# INDEX 2
class VentanaPrincipal(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self,parent)
        self.ui = MenuPrincipalUi()
        self.ui.setupUi(self)
        self.ventanaUC = VentanaUC()
        self.ui.botonI_menu.clicked.connect(self.mover_menu1)  # Conecta la señal del botón a la función mover_menu1()
        self.ui.botonm_cerrar.clicked.connect(app.quit)
        self.ui.botonm_lupa.clicked.connect(self.txtm_buscar)  # Boton pulsar
        self.ui.botonm_carrito.clicked.connect(self.cambiar_ventanaUC_carrito)
        self.ui.botonm_usuario.clicked.connect(self.cambiar_ventanaUC_usuario)

        # Power waters
        self.ui.botonComprar_4.clicked.connect(partial(self.insertar, 'Mix aguas (2 sabores x3)'))
        self.ui.botonComprar_5.clicked.connect(partial(self.insertar, 'Agua con Carbón activado (x6)'))
        self.ui.botonComprar_6.clicked.connect(partial(self.insertar, 'Agua con Espirulina azul (x6)'))

        # Zumitos
        self.ui.botonComprar_7.clicked.connect(partial(self.insertar, 'Piña, Fresa y Avena (x6)'))
        self.ui.botonComprar_8.clicked.connect(partial(self.insertar, 'Naranaja, Zanahoria y Mango (x6)'))
        self.ui.botonComprar_9.clicked.connect(partial(self.insertar, 'Aguacate y Espinacas (x6)'))
        self.ui.botonComprar_10.clicked.connect(partial(self.insertar, 'Frutas del bosque y Plátano (x6)'))
        self.ui.botonComprar_11.clicked.connect(partial(self.insertar, 'Mango, Espinacas y Chía (x6)'))
        self.ui.botonComprar_12.clicked.connect(partial(self.insertar, 'Piña, Manzana y Menta (x6)'))
        self.ui.botonComprar_13.clicked.connect(partial(self.insertar, 'Mix Degustación Zumos (x7)'))
        self.ui.botonComprar_14.clicked.connect(partial(self.insertar, 'Limón y Cayena (x6)'))

        # Platos preparados
        self.ui.botonComprar_15.clicked.connect(partial(self.insertar, 'Mix Degustación Platos Preparados (x6)'))
        self.ui.botonComprar_16.clicked.connect(partial(self.insertar, 'Lentejas con Verduras y Quinoa'))
        self.ui.botonComprar_17.clicked.connect(partial(self.insertar, 'Coliflor rehogada con Pimentón'))
        self.ui.botonComprar_18.clicked.connect(partial(self.insertar, 'Burger vegana con arroz y frutos secos'))
        self.ui.botonComprar_19.clicked.connect(partial(self.insertar, 'Burger vegana con ensalada de garbanzos'))
        self.ui.botonComprar_20.clicked.connect(partial(self.insertar, 'Menestra de Verduras'))
        self.ui.botonComprar_21.clicked.connect(partial(self.insertar, 'Cous cous con verduras'))

        # Cremas
        self.ui.botonComprar_22.clicked.connect(partial(self.insertar, 'Mix Degustación Cremas (x6)'))
        self.ui.botonComprar_23.clicked.connect(partial(self.insertar, 'Crema de Trigueros con Yuca'))
        self.ui.botonComprar_24.clicked.connect(partial(self.insertar, 'Crema de Guisantes con Menta'))
        self.ui.botonComprar_25.clicked.connect(partial(self.insertar, 'Crema de coliflor con curry'))
        self.ui.botonComprar_26.clicked.connect(partial(self.insertar, 'Crema de Calabaza y Naranja'))
        self.ui.botonComprar_27.clicked.connect(partial(self.insertar, 'Crema de Zanahoria'))
        self.ui.botonComprar_28.clicked.connect(partial(self.insertar, 'Crema de tomate Thai'))

        # Gummies
        self.ui.botonComprar_29.clicked.connect(partial(self.insertar, 'Hair & Nails Gummies'))
        self.ui.botonComprar_30.clicked.connect(partial(self.insertar, 'Fat Burn Gummies'))
        self.ui.botonComprar_31.clicked.connect(partial(self.insertar, 'Sleep Gummies'))
        self.ui.botonComprar_32.clicked.connect(partial(self.insertar, 'Immunity Gummies'))

        # Barras
        self.ui.botonComprar_33.clicked.connect(partial(self.insertar, '12 Mix Bars'))
        self.ui.botonComprar_34.clicked.connect(partial(self.insertar, 'Caja Cocoa Bars'))
        self.ui.botonComprar_35.clicked.connect(partial(self.insertar, 'Caja Apple Bars'))
        self.ui.botonComprar_36.clicked.connect(partial(self.insertar, 'Caja Strawberry Bars'))
        self.ui.botonComprar_41.clicked.connect(partial(self.insertar, 'Mix Bars (x3)'))

        # TeaTo y te desato
        self.ui.botonComprar_42.clicked.connect(partial(self.insertar, 'NIGHT TEA - Rest & Sleep'))
        self.ui.botonComprar_43.clicked.connect(partial(self.insertar, 'DAY TEA - Active & Burn'))
        self.ui.botonComprar_44.clicked.connect(partial(self.insertar, 'IMMUNITY TEA'))

        # Kombucha y Kompoca
        self.ui.botonComprar_45.clicked.connect(partial(self.insertar, 'Caja Kombucha Limón'))
        self.ui.botonComprar_46.clicked.connect(partial(self.insertar, 'Caja Kombucha Jengibre'))
        self.ui.botonComprar_47.clicked.connect(partial(self.insertar, 'Caja Kombucha Frutas del bosque'))
        self.ui.botonComprar_48.clicked.connect(partial(self.insertar, 'MIX Kombucha (x6)'))

        # Chupitaso
        self.ui.botonComprar_37.clicked.connect(partial(self.insertar, 'Caja shot Cold Care'))
        self.ui.botonComprar_38.clicked.connect(partial(self.insertar, 'Caja shot Energy'))
        self.ui.botonComprar_39.clicked.connect(partial(self.insertar, 'Caja Green Shot'))
        self.ui.botonComprar_40.clicked.connect(partial(self.insertar, 'Caja shot Antiox'))
        self.ui.botonComprar_49.clicked.connect(partial(self.insertar, 'Caja Shot Mix 4'))


        # Agrego eventFilters a las etiquetas correspondientes
        self.ui.label_logo.installEventFilter(self)
        self.ui.labelm_imagenZumos_2.installEventFilter(self)
        self.ui.labelm_imagenShots.installEventFilter(self)
        self.ui.labelm_imagenTe.installEventFilter(self)
        self.ui.labelm_imagenBars.installEventFilter(self)


        # Crear un diccionario para mapear los botones con las páginas 
        self.page_mapping = {
            #lo he quitado porque salía cortado y era más fácil quitarlo que intentarlo poner con scroll
            # self.ui.botonpDesayunos: self.ui.page_desayunos,
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


    def insertar(self, nombre):
        conn = conectar()
        # Conseguir el id y precio de producto
        prod = buscarProd(conn, nombre)
        if len(prod) > 0:
            # buscar en carrito si ya existe ese producto y aumentar la cantidad
            cant = buscarCarr(conn, prod[0], login.getEmail())
            if cant != None:
                actualizarCarr(conn, cant[0], prod[0], login.getEmail())
            else:
                insertarCarr(conn, prod, login.getEmail())

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



    def cambiar_ventanaUC_usuario(self):
        stacked_widget.setCurrentIndex(3)
        ventanaUC.cambiar_a_ventana_usuario()


    def cambiar_ventanaUC_carrito(self):
        stacked_widget.setCurrentIndex(3)
        ventanaUC.refrescarCarrito() #refresco carrito antes de meterme
        ventanaUC.cambiar_a_ventana_carrito()




# INDEX 3
class VentanaUC(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = VentanaUCUi()
        self.ui.setupUi(self)
        self.ui.botonuc_cerrar.clicked.connect(app.quit)
        self.ui.botonuc_atras.clicked.connect(self.cambiarAVentanaPrincipal)
        self.ui.botouc_finalizarPedido.clicked.connect(self.finalizarPedido)
        self.ui.botouc_usu.clicked.connect(self.cambiar_a_ventana_usuario)
        self.ui.pushButton_2.clicked.connect(self.generarFactura)
        self.ui.botonuc_update.clicked.connect(self.actualizarDatos)
        self.ui.cbd_CA.currentIndexChanged.connect(self.comboCCAA_changed)
        self.ui.cbd_provincia.currentIndexChanged.connect(self.comboProv_changed)
        # self.refrescarCarrito()
        #Para la tabla de usuarios
        # En el constructor de la clase VentanaUC, después de self.ui.setupUi(self)



        self.stacked_widget = self.ui.frame_cuerpo.findChild(QtWidgets.QStackedWidget)  # Obtener el QStackedWidget dentro de frame_cuerpo

#>>>>>>>>>>>>>>Carol

        self.ui.botouc_validar.clicked.connect(self.comprobarDescuento)
        
        #variables del objeto
        self.descuento=0
        self.precioTot=0
        self.precioSub=0
        self.cupon = ""
        self.datos_fila = [] ## Crear una lista para almacenar los datos de la fila seleccionada

#<<<<<<<<<<<<< Carol

        self.ui.label_subtotal_5.setText(str(f"{self.precioSub:0.2f}")+"€") #subtotal
        self.ui.label_subtotal_7.setText(str(f"{self.precioTot:0.2f}")+"€") #total
        
    # >>>>>> Manera de Andrea para rellenar los campos de total y subtotal
        # _translate = QtCore.QCoreApplication.translate
        # total = QtWidgets.QLabel(self.ui.label_subtotal_7)
        # subtotal = QtWidgets.QLabel(self.ui.label_subtotal_5)
        # total.setText(_translate("MainWindow", str(f"{self.precioTot:0.2f}")+"€"))
        # subtotal.setText(_translate("MainWindow", str(f"{self.precioSub:0.2f}")+"€"))
    #<<<<<<< Fin Andrea
        
    def refrescarCarrito(self): #lo he quitado del constructor y lo pongo a parte
                # Código para crear frames en frame_productos según productosKenia
        
        scroll_layout = self.ui.scrollAreaWidgetContents_4.layout()
        if scroll_layout:
            while scroll_layout.count():
                child = scroll_layout.takeAt(0)
                if child.widget():
                    child.widget().deleteLater()
        
        
        conexion = conectar()
        prods = mostrarCarrito(conexion, login.getEmail())
        # print(prods)
        if len(prods) > 0:
            scroll_layout = self.ui.scrollAreaWidgetContents_4.layout()

            self.precioTot = 0

            for i, prod in enumerate(prods):
                self.precioTot += (prod[2] * prod[3])

                
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
                # self.precioTot-=self.descuento
                self.precioSub = self.precioTot/1.21 #corrijo la operación para calcular precio sin IVA
            # except Exception as ex:
            #     print(ex)
        #LO COMENTO PORQUE EL LABEL NO SE QUITA CUANDO SE AGREGAN PRODUCTOS
        # else:
        #     frame_p = QtWidgets.QFrame(self.ui.scrollAreaWidgetContents_4)
        #     frame_p.setMaximumSize(QtCore.QSize(16777215, 130))
        #     frame_p.setMinimumHeight(150)
        #     frame_p.setMinimumWidth(517)
        #     frame_p.setStyleSheet("background-color: rgb(255, 255, 255);")
        #     frame_p.setFrameShape(QtWidgets.QFrame.StyledPanel)
        #     frame_p.setFrameShadow(QtWidgets.QFrame.Raised)
        #     frame_p.setObjectName("frame_p")
            
        #     label_noprod = QtWidgets.QLabel(frame_p)
        #     label_noprod.setStyleSheet(" text-align:center;")
        #     label_noprod.setText("No hay productos en el carrito")
        #     label_noprod.setObjectName("label_noprod")

            self.precioTot = 0
            self.precioSub = 0
        self.precioTot-=(self.descuento*self.precioTot/100)
        if self.precioTot==0:
            self.descuento=0
            self.ui.label_subtotal_6.setText("DESCUENTO NO APLICADO") #descuento
            self.ui.lineEdit.setText("")
        self.ui.label_subtotal_5.setText(str(f"{self.precioSub:0.2f}")+"€") #subtotal
        self.ui.label_subtotal_7.setText(str(f"{self.precioTot-(self.descuento*self.precioTot/100):0.2f}")+"€") #total
              
    def finalizarPedido(self):

        conn = conectar()
        datosUsu = existeUsu(conn, login.getEmail())
        dir = [datosUsu[5], datosUsu[6], datosUsu[7], datosUsu[8], datosUsu[9], datosUsu[11]]
        if(camposNone(dir)):
            showDialog("Debe introducir su dirección y dni para realizar una compra")
        else:
            fecha = date.today()
            fecha_str = fecha.strftime("%Y/%m/%d")
            showDialog(login.getEmail())
            insertarLineaPed(conn, login.getEmail(), self.cupon, self.precioTot, fecha_str)
        desconectar(conn)

        self.refrescarCarrito()

    def cambiarAVentanaPrincipal(self):
        stacked_widget.setCurrentIndex(2)

    def cambiar_a_ventana_usuario(self):
        self.stacked_widget.setCurrentWidget(self.ui.pag_usuario)  # Cambiar a la página "pag_usuario"
        self.cargarDatosTablaTickets()
        self.cargarDatosUsuario()

    def cambiar_a_ventana_carrito(self):
            self.stacked_widget.setCurrentWidget(self.ui.pag_carrito)  # Cambiar a la página "carrito"

    def actualizarDatos(self):
        conexion = conectar()
        error = False
        
        datosUsu = existeUsu(conexion, login.getEmail())
        # correo, nombre, contraseña, preseg ,resseg, direccion, cp, ca, prov, mun, tel, dni, apellidos

        if len(self.ui.txtd_nombre.text()) > 0:
            nombre = self.ui.txtd_nombre.text()
        else: nombre = datosUsu[1]

        if len(self.ui.txtd_contra.text()) > 0:
            contra = self.ui.txtd_contra.text()
            if len(contra) < 8:
                showDialog("La contraseña debe tener al menos 8 caracteres")
                error = True
            elif contra != self.ui.txtd_confcontra.text():
                showDialog("El campo de confirmación de contraseña debe ser igual al de contraseña")
                error = True
            else: contra = cifrarContra(contra)
        else: contra = datosUsu[2]

        if len(self.ui.txtd_preseg.text()) > 0:
            preseg = self.ui.txtd_preseg.text()
        else: preseg = datosUsu[3]

        if len(self.ui.txtd_resseg.text()) > 0:
            resseg = self.ui.txtd_resseg.text()
            resseg = cifrarContra(resseg)
        else: resseg = datosUsu[4]

        if len(self.ui.txtd_direccion.text()) > 0:
            dir = self.ui.txtd_direccion.text()
        else: dir = datosUsu[5]

        if len(self.ui.txtd_cp.text()) > 0:
            cp = self.ui.txtd_cp.text()
        else: cp = datosUsu[6]

        if len(self.ui.cbd_CA.currentText()) > 0:
            ca = buscarCANom(conexion, self.ui.cbd_CA.currentText())
        else: ca = datosUsu[7]

        if len(self.ui.cbd_provincia.currentText()) > 0:
            prov = buscarProvNom(conexion, self.ui.cbd_provincia.currentText())
        else: prov = datosUsu[8]

        if len(self.ui.cbd_municipio.currentText()) > 0:
            mun = buscarMunNom(conexion, self.ui.cbd_municipio.currentText())
        else: mun = datosUsu[9]

        if len(self.ui.txtd_telefono.text()) > 0:
            tel = self.ui.txtd_telefono.text()
        else: tel = datosUsu[10]

        if len(self.ui.txtd_dni.text()) > 0:
            dni = self.ui.txtd_dni.text()
        else: dni = datosUsu[11]

        if len(self.ui.txtd_apellidos.text()) > 0:
            apell = self.ui.txtd_apellidos.text()
        else: apell = datosUsu[12]

        if not error:
            datos = (nombre, contra, preseg, resseg, dir, cp, ca, prov, mun, tel, dni, apell)
            actualizarUsu(conexion, datos, login.getEmail())

        desconectar(conexion)

# >>>>>>>>>>> Carol

    def comprobarDescuento(self):
        try:
            conexion=conectar()
            self.cupon=self.ui.lineEdit.text()
            self.descuento=comprobarCupon(conexion,self.cupon)
            if self.descuento !=0:
                self.precioTot-=(self.descuento*self.precioTot/100)
                self.precioSub=self.precioTot/1.21
                self.ui.label_subtotal_6.setText("-"+str(self.descuento)+"%") #descuento
                self.ui.label_subtotal_5.setText(str(f"{self.precioSub:0.2f}")+"€") #subtotal
                self.ui.label_subtotal_7.setText(str(f"{self.precioTot:0.2f}")+"€") #total
        except Exception as ex:
            print(ex)
        
# <<<<<<<<<<<< Carol

    def cargarDatosUsuario(self):
        conexion = conectar()
        datosUsu = existeUsu(conexion, login.getEmail())

        # correo, nombre, contraseña, preseg ,resseg, direccion, cp, ca, prov, mun, tel, dni, apellidos

        ccaa = cargarCCAA(conexion)
        for ca in ccaa:
            self.ui.cbd_CA.addItem(ca[1])

        self.ui.txtd_nombre.setText(datosUsu[1])
        self.ui.txtd_preseg.setText(datosUsu[3])

        if datosUsu[12] != None:
            self.ui.txtd_apellidos.setText(datosUsu[12])
            
        if datosUsu[11] != None:
            self.ui.txtd_dni.setText(datosUsu[11])
            
        if datosUsu[10] != None:
            self.ui.txtd_telefono.setText(datosUsu[10])
            
        if datosUsu[6] != None:
            self.ui.txtd_cp.setText(str(datosUsu[6]))
        
        if datosUsu[5] != None:
            self.ui.txtd_direccion.setText(datosUsu[5])
        
        if datosUsu[7] != None: 
            ca = buscarCA(conexion, datosUsu[7])
            prov = buscarProv(conexion, datosUsu[8])
            mun = buscarMun(conexion, datosUsu[9])

            indiceca = self.ui.cbd_CA.findText(ca)
            self.ui.cbd_CA.setCurrentIndex(indiceca)
            
            indiceprov = self.ui.cbd_provincia.findText(prov)
            self.ui.cbd_provincia.setCurrentIndex(indiceprov)
            
            indicemun = self.ui.cbd_municipio.findText(mun)
            self.ui.cbd_municipio.setCurrentIndex(indicemun)
        else:
            self.ui.cbd_CA.setCurrentIndex(-1)
            self.ui.cbd_provincia.setCurrentIndex(-1)
            self.ui.cbd_municipio.setCurrentIndex(-1)

        desconectar(conexion)

    def comboCCAA_changed(self):
        conexion = conectar()
        self.ui.cbd_provincia.setCurrentIndex(-1)
        self.ui.cbd_municipio.setCurrentIndex(-1)
        self.ui.cbd_provincia.clear()
        self.ui.cbd_municipio.clear()

        ca = buscarCANom(conexion, self.ui.cbd_CA.currentText())

        provs = cargarProvs(conexion, ca)
        for prov in provs:
            self.ui.cbd_provincia.addItem(prov[2])
        desconectar(conexion)

    def comboProv_changed(self):
        conexion = conectar()
        # self.ui.cbd_municipio.setCurrentIndex(-1)
        self.ui.cbd_municipio.clear()

        prov = buscarProvNom(conexion, self.ui.cbd_provincia.currentText())
        muns = cargarMuns(conexion, prov)
        for mun in muns:
            self.ui.cbd_municipio.addItem(mun[4])
            
        desconectar(conexion)

    def cargarDatosTablaTickets(self):
        conexion = conectar()
        tickets = obtenerTickets(conexion, login.getEmail())


        print(str(tickets))
        stacked_widget = self.ui.frame_cuerpo.findChild(QtWidgets.QStackedWidget)  # Obtener el QStackedWidget dentro de frame_cuerpo
        table_widget = stacked_widget.findChild(QtWidgets.QTableWidget)  # Obtener el QTableWidget dentro de QStackedWidget

        table_widget.setRowCount(len(tickets))  # Establecer el número de filas en la tabla

        for i, ticket in enumerate(tickets):
            # Obtener los datos del ticket
            tick_id = ticket[0]
            usuario = ticket[1]
            desc_id = ticket[2]
            precio = ticket[3]
            fecha = ticket[4]

            # Insertar los datos en la tabla
            table_widget.setItem(i, 0, QtWidgets.QTableWidgetItem(str(tick_id)))
            table_widget.setItem(i, 1, QtWidgets.QTableWidgetItem(str(fecha)))
            table_widget.setItem(i, 2, QtWidgets.QTableWidgetItem(str(precio)))
            table_widget.setItem(i, 3, QtWidgets.QTableWidgetItem(str(usuario)))


        # Centrar el texto en las celdas
        for i in range(table_widget.rowCount()):
            for j in range(table_widget.columnCount()):
                item = table_widget.item(i, j)
                item.setTextAlignment(QtCore.Qt.AlignCenter)

        
        # Modificar el tamaño de las columnas
        table_widget.setColumnWidth(0, 125)  # Columna 0: ID del ticket
        table_widget.setColumnWidth(1, 125)  # Columna 1: Fecha
        table_widget.setColumnWidth(2, 125)  # Columna 2: Precio
        table_widget.setColumnWidth(3, 125)  # Columna 3: Usuario
        
        # Conectar la señal itemSelectionChanged a la función filaSeleccionada
        table_widget.itemSelectionChanged.connect(self.filaSeleccionada)

    def filaSeleccionada(self):
        #Igualo a 0 la lista para que no se vaya sumando cada vez que selecciono una nueva.
        self.datos_fila=[]
        #  widget pag_usuario
        pag_usuario_widget = self.ui.pag_usuario
        # Busco el QTableWidget dentro de pag_usuario
        table_widget_pag_usuario = pag_usuario_widget.findChild(QtWidgets.QTableWidget)

        if table_widget_pag_usuario:
            # Obtener las celdas seleccionadas
            selected_rows = table_widget_pag_usuario.selectedItems()

            # si se seleccionó alguna fila
            if selected_rows:
                fila_seleccionada = selected_rows[0].row()
                print("Fila seleccionada:", fila_seleccionada)

                columnas = table_widget_pag_usuario.columnCount() # Obtener el número de columnas del QTableWidget

                for columna in range(columnas):
                    # Obtener el item (celda) en la fila seleccionada y la columna actual
                    item = table_widget_pag_usuario.item(fila_seleccionada, columna)

                    if item is not None:
                        dato = item.text()
                        self.datos_fila.append(dato)
                    else:
                        self.datos_fila.append("")

                print("Datos de la fila seleccionada:", self.datos_fila)
                print("---")

            else:
                print("No se ha seleccionado ninguna fila.")
        else:
            print("No se encontró un QTableWidget dentro de pag_usuario.")


        #Lo comento porque este código no hace nada (creo):
        
        # push_button = pag_usuario_widget.findChild(QtWidgets.QPushButton, "pushButton")
        # if push_button is not None:
        #     if push_button.isChecked():
        #         print("boton pulsado")
        
    def generarFactura(self):
        # print(self.datos_fila)
        if self.datos_fila:
            #si hay datos en la lista
            #PREPARO LOS DATOS PARA LA FACTURA
            compraID=self.datos_fila[0]
            #Producto= [nombre producto, cantidad, precio]
            listaProductos=[] #lista de listas
            datosTicket=obtenerLineaPedidosPorTickID(compraID) #devuelve: lineaID, prodID, precio, cantidad, compraID
            print(datosTicket)
            for i in range(len(datosTicket)):
                producto=[]
                nombre=nombreProducto(datosTicket[i][1])
                print(nombre)
                producto.append(nombre)
                producto.append(datosTicket[i][3]) #cantidad
                producto.append(datosTicket[i][2]) #precio del producto
                listaProductos.append(producto)
            datosCompra=buscarCompra(compraID)
            datosUsuario=buscarUsuario(self.datos_fila[3])
            #le quito la tupla a las listas que vienen con ellas
            datosCompra  = [elemento for tupla in datosCompra  for elemento in tupla] 
            datosUsuario = [elemento for tupla in datosUsuario for elemento in tupla]
            # print("aqui")
            # print(listaProductos)
            # print("--")
            # print(datosCompra)
            # print("--")
            # print(datosUsuario)
            #CREO EL HTML CON LOS DATOS

            addLineasProductos(listaProductos,datosCompra,datosUsuario) 
            crea_pdf(compraID,datosCompra[0],rutaHtml())
            showDialog("Factura generada correctamente en la ruta: "+rutaPdf(compraID,datosCompra[0]))
            print()
        else:
            showDialog("Debe seleccionar un pedido")
            

#MAIN
if __name__ == "__main__":
    
    try:
        app = QtWidgets.QApplication(sys.argv)

        stacked_widget = QtWidgets.QStackedWidget()  #Se crea un objeto stacked_widget 
        login = Login()
        crear_cuenta = CrearCuenta()
        ventanaPrincipal = VentanaPrincipal()
        ventanaUC = VentanaUC()
        icon = QtGui.QIcon(':/iconos/z_logo_naranja.png')

        # window = QtWidgets.QMainWindow()

        #Se agregan las ventanas al objeto stacked widget
        stacked_widget.addWidget(login)
        stacked_widget.addWidget(crear_cuenta)
        stacked_widget.addWidget(ventanaPrincipal)
        stacked_widget.addWidget(ventanaUC)

        
        # window.setCentralWidget(stacked_widget)
        # window.setWindowIcon(icon)

        ### stacked_widget.addWidget(crear_cuenta) #La creo mejor arriba en CrearCuenta

        #>>>> Código para que sea responsive
        desktop = QApplication.desktop()
        screen_geometry = desktop.availableGeometry()
        width = int(screen_geometry.width() * 0.8)  # 80% del ancho de la pantalla
        height = int(screen_geometry.height() * 0.7)  # 70% de la altura de la pantalla
        stacked_widget.resize(width, height)
        #<<<<<< Fin código para que sea responsive

        # stacked_widget.resize(800, 565)
        stacked_widget.setCurrentIndex(0)  # Iniciar en la ventana de Login

        # Para esconder el marco principal en la ventana principal
        stacked_widget.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        stacked_widget.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        # stacked_widget.setWindowIcon(icon)s


        # icon = QtGui.QIcon(':/iconos/logo_naranja.png')
        # window.setWindowIcon(icon)

        stacked_widget.show()
        # window.show()
        # login.show()


        # num_widgets = stacked_widget.count()
        # print("Número de widgets: ", num_widgets)

        app.setWindowIcon(icon)
        sys.exit(app.exec_())
    except Exception as ex:
        print(ex)
    