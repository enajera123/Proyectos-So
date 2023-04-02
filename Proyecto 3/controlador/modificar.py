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
#Termina la clase