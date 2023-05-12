import sys
from principal import *

class MiFormulario(QtGui):
    def __init__(self,parent=None):
        QtGui.QWidget.__init__(self,parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
if __name__=='__main__':
    app=QtGui.QGuiApplication(sys.argv)
    myapp=MiFormulario()
    myapp.show()
    sys.exit(app.exec)