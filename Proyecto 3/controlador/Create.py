import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication

#=======================
#		Controlador
#=======================
class Main(QMainWindow):
    def __init__(self):#this
      super(Main,self).__init__()#Inicializa la clase -> Initialize
      uic.loadUi("Create.ui",self)
      self.cbNombreUsuario.setCurrentIndex(-1)
    
        
#Termina la clase
#=======================
#		Main
#=======================
app = QApplication(sys.argv)
main = Main()
main.show()
sys.exit(app.exec_())