import psycopg2
import sys
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import QPropertyAnimation, QEasingCurve 
from PyQt5.QtWidgets import QApplication
from unidecode import unidecode
from v4_ventanaUC import Ui_MainWindow as VentanaUCUi
from res import *

class ProductoKenia(object):
    def __init__(self, prod_id, nombre, descripcion, categoria, precio, cantidad, imagen):
        self.prod_id = prod_id
        self.nombre = nombre
        self.descripcion = descripcion
        self.categoria = categoria
        self.precio = precio
        self.cantidad = cantidad
        self.imagen = imagen

def conectar():
    try:
        conn = psycopg2.connect(
            host="127.0.0.1",
            port="5432",
            database="organic",
            user="admin",
            password="vistaalegre"
        )
        conn.autocommit = True
        return conn
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        return None

def desconectar(conn):
    if conn is not None:
        conn.close()

# Conectar a la base de datos
conn = conectar()

if conn is not None:
    try:
        # Obtener una instancia del frame "productos"
        frame_productos = {}  # Puedes inicializarlo como un diccionario vacío

        # Obtener los productos de la tabla "productosKenia"
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM productosKenia")
        productos = cursor.fetchall()

        # Insertar cada producto en el frame "productos"
        for producto in productos:
            prod_id = producto[0]  # Obtener el ID del producto
            nombre = producto[1]  # Obtener el nombre del producto
            descripcion = producto[2]  # Obtener la descripción del producto
            categoria = producto[3]  # Obtener la categoría del producto
            precio = producto[4]  # Obtener el precio del producto
            cantidad = producto[5]  # Obtener la cantidad del producto
            imagen = producto[6]  # Obtener el nombre de la imagen del producto
            frame_p = ProductoKenia(prod_id, nombre, descripcion, categoria, precio, cantidad, imagen)  # Crear una instancia de ProductoKenia con los datos del producto
            frame_productos[frame_p.nombre] = frame_p

        cursor.close()
    except psycopg2.DatabaseError as error:
        print(error)

# Desconectar de la base de datos
desconectar(conn)


# def datos():

#     for nombre, producto in frame_productos.items():
#         print(f"Nombre: {nombre}")
#         print(f"Descripción: {producto.descripcion}")
#         print(f"Categoría: {producto.categoria}")
#         print(f"Precio: {producto.precio}")
#         print(f"Cantidad: {producto.cantidad}")
#         print(f"Imagen: {producto.imagen}")
#         print()




def mostrarProductosKenia(conn):
  query = f"SELECT * FROM producto;"
  try:
    cur = conn.cursor()
    cur.execute(query)
    prods = cur.fetchall()
  except (Exception, psycopg2.DatabaseError) as error:
    print(error)
  return prods



class VentanaUC(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = VentanaUCUi()
        self.ui.setupUi(self)


        # Buscar y mostrar todos los frames en frame_productos
        # for index, producto in enumerate(frame_productos.values()):

            # if index == 0:
            #     self.ui.label_imagen.setStyleSheet(f"border-image: url(:/{producto.categoria}/{producto.imagen});")
            # elif index == 1:
            #     self.ui.label_imagen_2.setStyleSheet(f"border-image: url(:/{producto.categoria}/{producto.imagen});")
            # else:
            #     # Crear un nuevo QLabel para cada imagen adicional
            #     label_imagen = QtWidgets.QLabel(self)
            #     label_imagen.setStyleSheet(f"border-image: url(:/{producto.imagen});")
            #     label_imagen.setGeometry(10, 10 + (index-2) * 100, 100, 100)
            #     label_imagen.show()


        #  # Imprimir los nombres de los objetos dentro de frame_productos
        # for frame in self.ui.frame_productos.findChildren(QtWidgets.QFrame):
        #     print(frame.objectName())





# funciona para cargar imagenes

        # Crear un nuevo QFrame dentro del scrollArea para cada producto en frame_productos
        # for index, producto in enumerate(frame_productos.values()):
        #     frame_p = QtWidgets.QFrame(self.ui.scrollAreaWidgetContents_4)
        #     frame_p.setMaximumSize(QtCore.QSize(16777215, 130))
        #     frame_p.setStyleSheet("background-color: rgb(255, 255, 255);")
        #     frame_p.setFrameShape(QtWidgets.QFrame.StyledPanel)
        #     frame_p.setFrameShadow(QtWidgets.QFrame.Raised)
        #     frame_p.setObjectName("frame_p" + str(index))



        #     # Crear una nueva QLabel dentro del scrollArea en frame_productos
        # nueva_label = QtWidgets.QLabel(self.ui.scrollAreaWidgetContents_4)
        # nueva_label.setText("Nueva Label")

        




        # Código para crear frames en frame_productos según productosKenia
        conexion = conectar()
        prods = mostrarProductosKenia(conexion)

        self.frame_names = []  # Lista para almacenar los nombres de los frames
        self.image_names = []  # Lista para almacenar los nombres de las etiquetas de imagen
        self.titulo_productos = []  # Lista para almacenar los títulos de los productos


        scroll_layout = self.ui.scrollAreaWidgetContents_4.layout()

        for i, prod in enumerate(prods):
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


            #Aáde la imagen al frame 2
            label_imagen = QtWidgets.QLabel(frame_img)
            categoria=(str(prod[3]))
            name=(str(prod[6]))
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
            numeric.setObjectName("numeric" + str(i))
            horizontalLayout_cant_precio.addWidget(numeric)


# Añado etiqueta precio y le añado distribucion 
            label_precioProducto = QtWidgets.QLabel(frame_cont_prod)
            label_precioProducto.setObjectName("label_precioProducto" + str(i))
            horizontalLayout_cant_precio.addWidget(label_precioProducto)

            _translate = QtCore.QCoreApplication.translate
            label_tituloProducto.setText(_translate("MainWindow", prod[1]))
            label_precioProducto.setText(_translate("MainWindow", str(prod[4]) + "€"))
            # numeric.setValue(prod[5]) --> No lo quiero 

            self.frame_names.append(frame_p.objectName())
            self.image_names.append(label_imagen.objectName())
            self.titulo_productos.append(label_tituloProducto.objectName())

            # self.result = [(frame_name, image_name, titulo_producto) for frame_name, image_name, titulo_producto in zip(self.frame_names, self.image_names, self.titulo_productos)]
        # print(self.result)

    def cargar_imagenes(self):
        # for tupla in self.result:
        #     for frame_name, label_imagen_name, titulo_producto  in tupla:
        #         print(frame_name)
        #         print(label_imagen_name)
        #         print(titulo_producto)
        for frame_name, label_imagen_name, titulo_producto in self.result:
            print(frame_name)
            print(label_imagen_name)
            print(titulo_producto)

                # # Obtener la imagen del producto según el título
                # imagen_producto = obtener_imagen_producto(titulo_producto)

                # # Actualizar el estilo de la etiqueta de imagen del frame con la imagen obtenida
                # label_imagen.setStyleSheet(f"border-image: url(:/{imagen_producto});")
                # label_imagen.show()





def obtener_imagen_producto(titulo_producto):
    # Conexión a la base de datos
    conexion = psycopg2.connect(
        host="localhost",
        database="basedatos",
        user="usuario",
        password="contraseña"
    )
    cursor = conexion.cursor()

    # Consulta SQL para obtener la imagen del producto según el título
    consulta = "SELECT imagen FROM productos WHERE titulo = %s"
    cursor.execute(consulta, (titulo_producto,))
    resultado = cursor.fetchone()

    # Cerrar la conexión a la base de datos
    conexion.close()

    if resultado:
        imagen = resultado[0]
        return imagen
    else:
        return None




# Llamar a la función principal
if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)

    stacked_widget = QtWidgets.QStackedWidget()  # Se crea un objeto stacked_widget 
    ventana_uc = VentanaUC()
    stacked_widget.addWidget(ventana_uc)

    stacked_widget.resize(625, 565)
    stacked_widget.setCurrentIndex(0)  # Iniciar en la ventana de Login

    # Para esconder el marco principal en la ventana principal
    stacked_widget.setWindowFlags(QtCore.Qt.FramelessWindowHint)
    # stacked_widget.setAttribute(QtCore.Qt.WA_TranslucentBackground)

    stacked_widget.show()
    # datos()

    sys.exit(app.exec_())

