import sys
from principal import *
from PyQt5 import QtWidgets

class MiFormulario(QtWidgets.QMainWindow):
    def __init__(self,parent=None):
        QtWidgets.QWidget.__init__(self,parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
if __name__=='__main__':
    app=QtWidgets.QApplication(sys.argv)
    myapp=MiFormulario()
    myapp.show()
    sys.exit(app.exec)
    