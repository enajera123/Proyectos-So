import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication
from modelo.ManejoArchivo import ManejoArchivo
# =======================
# Controlador
# =======================
class LoginView(QMainWindow):
    def __init__(self):  # this
        super(LoginView, self).__init__()  # Inicializa la clase -> Initialize
        uic.loadUi("vista/login.ui", self)
        LoginView.conectarEventos(self)     

    def conectarEventos(self):
        """Asocia los eventos con sus disparadores"""
        self.btnCrear.clicked.connect(self.btnCrear_click)
        self.btnIniciarSesion.clicked.connect(self.btnIniciarSesion_click)
    
    def btnCrear_click(self,event):
        nombre = self.txtNombre.text().strip()
        clave = self.txtNombre.text()
        ManejoArchivo.crearCarpeta(nombre)
        ManejoArchivo.crearCarpeta(nombre+"/raiz")
        ManejoArchivo.crearCarpeta(nombre+"/temporal")
    def btnIniciarSesion_click(self,event):
        print("codigo aqui") 
# Termina la clase
# =======================
# Main
# =======================


