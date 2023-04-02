import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication

#utilidades
from utilidades.ManejoArchivo import ManejoArchivo
from utilidades.Data import Data
from utilidades.Alerta import Alerta

#=======================
#		Controlador
#=======================
class Modificar(QMainWindow):
    def __init__(self):#this
      super(Modificar,self).__init__()#Inicializa la clase -> Initialize
      uic.loadUi("vista/modificar.ui",self)
      self.cbNombreUsuario.setCurrentIndex(-1)
      self.btnRegresar.clicked.connect(self.btnRegresar_click)
      self.btnCrearCarpeta.clicked.connect(self.btnCrearCarpeta_click)
    
    def btnRegresar_click(self,event):            
        # Notese que se importa el controlador en la funcion para evitar imports circulares
        from controlador.main import Main
        self.hide()
        self.nuevaVentana = Main()
        self.nuevaVentana.show()  
 
    def btnCrearCarpeta_click(self, event):
        nombreCarpeta = self.txtNombreCarpeta.text()
        if (len(nombreCarpeta) > 0):
          #hacer una verificación de nombres carpetas iguales
          ManejoArchivo.crearCarpetaNoDefault(nombreCarpeta)
          #falta una validacion aca para manejar los errores de sobreescritura de carpetas
          alerta = Alerta("Carpeta Creada Exitosamente. ", "confirmacion")
          alerta.mostrarAlerta()
         
#Termina la clase