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
  def conectarEventos(self):
    """Asocia los eventos con sus disparadores"""
    self.btnAgregarUsuario.clicked.connect(self.btnAgregarUsuario_click)
  # =======================
  # Eventos
  # =======================
  
  def btnAgregarUsuario_click(self, event):
    Usuario = self.cbNombreUsuario.SelectedItem
    if (self.cbNombreUsuario.SelectedIndex != -1):
      self.listPermisosUsuarios.Items.Add(Usuario)
  #Termina la clase