import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication

#=======================
#		Controlador
#=======================
class Create(QMainWindow):
    def __init__(self):#this
      super(Create,self).__init__()#Inicializa la clase -> Initialize
      uic.loadUi("vista/create.ui",self)
      self.cbNombreUsuario.setCurrentIndex(-1)
#Termina la clase