import sys
from login import *
from resLogin import *
from PyQt5 import QtWidgets



class Login(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self,parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.funcionLogin)


    def funcionLogin(self):
        email=self.ui.lineEdit.text()
        password=self.ui.lineEdit_2.text()
        print("Ha iniciado correctamente: ", email, password)

# class CrearCuenta(QtWidgets.QMainWindow):
#     def __init__(self, parent=None):
#         QtWidgets.QWidget.__init__(self,parent)
#         self.ui = Ui_MainWindow()
#         self.ui.setupUi(self)
#         self.ui.pushButton.clicked.connect(self.funcionLogin)


#     def funcionLogin(self):
#         email=self.ui.lineEdit.text()
#         password=self.ui.lineEdit_2.text()
#         print("Ha iniciado correctamente: ", email, password)


#MAIN
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = Login()
    myapp.show()
    sys.exit(app.exec_())