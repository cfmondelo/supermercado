from PyQt5 import QtCore, QtGui, QtWidgets
import psycopg2

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 300)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        # Utilizamos un QVBoxLayout para el diseño vertical
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        
        # Etiqueta para el título del producto
        self.label_titulo = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.label_titulo.setFont(font)
        self.label_titulo.setAlignment(QtCore.Qt.AlignCenter)
        self.label_titulo.setObjectName("label_titulo")
        self.verticalLayout.addWidget(self.label_titulo)
        
        # Etiqueta para la descripción del producto
        self.label_descripcion = QtWidgets.QLabel(self.centralwidget)
        self.label_descripcion.setAlignment(QtCore.Qt.AlignCenter)
        self.label_descripcion.setObjectName("label_descripcion")
        self.verticalLayout.addWidget(self.label_descripcion)
        
        # Etiqueta para la imagen del producto
        self.label_imagen = QtWidgets.QLabel(self.centralwidget)
        self.label_imagen.setAlignment(QtCore.Qt.AlignCenter)
        self.label_imagen.setObjectName("label_imagen")
        self.verticalLayout.addWidget(self.label_imagen)
        
        # Selector de cantidad
        self.spinBox_cantidad = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_cantidad.setObjectName("spinBox_cantidad")
        self.verticalLayout.addWidget(self.spinBox_cantidad)
        
        # Botón de comprar
        self.btn_comprar = QtWidgets.QPushButton(self.centralwidget)
        self.btn_comprar.setObjectName("btn_comprar")
        self.verticalLayout.addWidget(self.btn_comprar)
        
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        # Se define la función de traducción
        _translate = QtCore.QCoreApplication.translate
        
        # Se establece el título de la ventana
        MainWindow.setWindowTitle(_translate("MainWindow", "Compra de Artículos"))
        
        # Se establece el texto de la etiqueta de título del producto
        self.label_titulo.setText(_translate("MainWindow", "Título del Producto"))
        
        # Se establece el texto de la etiqueta de descripción del producto
        self.label_descripcion.setText(_translate("MainWindow", "Descripción del Producto"))
        
        # Se establece el texto del botón de comprar
        self.btn_comprar.setText(_translate("MainWindow", "Comprar"))



    def cargarImagen_desdeBDD(self):
        try:
            conn = psycopg2.connect(database="organic", user="admin", password="vistaalegre", host="localhost", port="5432")
            cursor = conn.cursor()

            # Consulta SQL para obtener la imagen del producto con id=2
            cursor.execute("SELECT imagen FROM producto WHERE prod_id = 2")

            # Obtener la imagen de la consulta
            image = cursor.fetchone()[0]

            # Cargar la imagen en la etiqueta
            pixmap = QtGui.QPixmap(image)
            self.label_imagen.setPixmap(pixmap)

            conn.close()
        except (Exception, psycopg2.Error) as error:
            print("Error while connecting to PostgreSQL", error)




def main():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
