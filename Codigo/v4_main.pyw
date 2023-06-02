import psycopg2
import sys
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import QPropertyAnimation, QEasingCurve 
from PyQt5.QtWidgets import QApplication
from unidecode import unidecode
from v4_ventanaUC import Ui_MainWindow as VentanaUCUi
from res import *
from metodosSupermercado import *


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

# Desconectar de la base de datos
desconectar(conn)


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


        # Código para crear frames en frame_productos según productosKenia
        conexion = conectar()
        prods = mostrarCarrito(conexion)

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


            #Aáde la imagen al frame 2
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

        precioSub = precioTot - (21 * precioTot/100)

        total = QtWidgets.QLabel(self.ui.label_subtotal_7)
        subtotal = QtWidgets.QLabel(self.ui.label_subtotal_5)
        total.setText(_translate("MainWindow", str(precioTot)+"€"))
        subtotal.setText(_translate("MainWindow", str(precioSub)+"€"))




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

