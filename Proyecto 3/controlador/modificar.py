import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QListWidget
#from ManejoArchivo import ManejoArchivo

#=======================
#		Controlador
#=======================
class Modificar(QMainWindow):
    def __init__(self):#this
      super(Modificar,self).__init__()#Inicializa la clase -> Initialize
      uic.loadUi("vista/modificar.ui",self)
      self.cbNombreUsuario.setCurrentIndex(-1)
      self.btnRegresar.clicked.connect(self.btnRegresar_click)
      self.btnAgregarUsuario.clicked.connect(self.btnAgregarUsuario_click)
      #self.ManejoArchivo_instance = ManejoArchivo()
      #usuarios = self.ManejoArchivo_instance.leerUsuarios()
      #self.cbNombreUsuario.addItems(usuarios)
      
      
    def btnRegresar_click(self,event):            
        # Notese que se importa el controlador en la funcion para evitar imports circulares
        from controlador.main import Main
        self.hide()
        self.nuevaVentana = Main()
        self.nuevaVentana.show()
        
    def btnAgregarUsuario_click(self,event):            
        #Agrega al listview el usuario con sus respectivos permisos
        item = self.cbNombreUsuario.currentText()
        if (self.cbNombreUsuario.currentIndex() != -1):
          self.lisitWPerUsuarios.addItem(item)
#Termina la clase