import psycopg2
import sys
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import QPropertyAnimation, QEasingCurve 
from PyQt5.QtWidgets import QApplication
from unidecode import unidecode
from v4_ventanaUC import Ui_MainWindow as VentanaUCUi
from res import *



class VentanaUC(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = VentanaUCUi()
        self.ui.setupUi(self)

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

    sys.exit(app.exec_())

