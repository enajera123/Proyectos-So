import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication

#=======================
#		Controlador
#=======================
class Modificar(QMainWindow):
    def __init__(self):#this
      super(Modificar,self).__init__()#Inicializa la clase -> Initialize
      uic.loadUi("vista/modificar.ui",self)
      self.cbNombreUsuario.setCurrentIndex(-1)
      self.btnRegresar.clicked.connect(self.btnRegresar_click)
    
    def btnRegresar_click(self,event):            
        # Notese que se importa el controlador en la funcion para evitar imports circulares
        from controlador.main import Main
        self.hide()
        self.nuevaVentana = Main()
        self.nuevaVentana.show()  
#Termina la clase