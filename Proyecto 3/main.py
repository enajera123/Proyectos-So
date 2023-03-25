import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication

#=======================
#		Controlador
#=======================
class Main(QMainWindow):
    def __init__(self):#this
      super(Main,self).__init__()#Inicializa la clase -> Initialize
      uic.loadUi("main.ui",self)
      self.lblHello.setText("")
      self.btnPress.clicked.connect(self.click)#Asocia el evento click al boton btnPress
      
    def click(self,event):
        self.lblHello.setText("Hello World!")
    
        
#Termina la clase
#=======================
#		Main
#=======================
app = QApplication(sys.argv)
main = Main()
main.show()
sys.exit(app.exec_())

