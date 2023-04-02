import sys
# PyQt5
from PyQt5 import uic
from PyQt5.QtCore import pyqtSignal, QEvent
from PyQt5.QtWidgets import QMainWindow, QApplication
# Utilidades
from utilidades.ManejoArchivo import ManejoArchivo
from utilidades.Data import Data
from utilidades.Alerta import Alerta
# Modelo
from modelo.Usuario import Usuario

# =======================
# Controlador
# =======================


class LoginView(QMainWindow):
    # =======================
    # Inicializadores
    # =======================
    def __init__(self):  # this
        super(LoginView, self).__init__()  # Inicializa la clase -> Initialize
        uic.loadUi("vista/login.ui", self)
        LoginView.conectarEventos(self)

    def conectarEventos(self):
        """Asocia los eventos con sus disparadores"""
        self.btnCrear.clicked.connect(self.btnCrear_click)
        self.btnIniciarSesion.clicked.connect(self.btnIniciarSesion_click)
        self.txtClave.returnPressed.connect(self.on_returnPressed)
        self.txtNombre.returnPressed.connect(self.on_returnPressed)
    # =======================
    # Eventos
    # =======================

    def on_returnPressed(self):
        event = QEvent(QEvent.KeyPress)
        LoginView.btnIniciarSesion_click(self,event)
        

    def btnCrear_click(self, event):
        nombre = self.txtNombre.text().strip()
        clave = self.txtClave.text()
        if (len(nombre) > 0 and len(clave) > 0):
            if (not LoginView.verificarNombre(nombre)):
                alerta = Alerta(
                    "El nombre de usuario ya existe, por favor escoja otro", "Error")
                alerta.mostrarAlerta()
            else:
                LoginView.crearCarpetasDefault(nombre)
                usuario = Usuario(nombre, clave)
                ManejoArchivo.guardarUsuarios([usuario])
                alerta = Alerta(
                    "Usuario Creado Exitosamente. Bienvenido "+nombre, "confirmacion")
                alerta.mostrarAlerta()
                LoginView.bindCampos(nombre, clave)
                LoginView.abrirMain(self)  # Cambio de ventana
        else:
            alerta = Alerta(
                "No puede dejar campos vacios", "error")
            alerta.mostrarAlerta()

    def btnIniciarSesion_click(self, event):
        nombre = self.txtNombre.text().strip()
        clave = self.txtClave.text()
        # Verificar
        usuarios = ManejoArchivo.leerUsuarios()
        for usuario in usuarios:
            if (ManejoArchivo.comprobarUsuario(usuario, nombre, clave)):
                LoginView.bindCampos(nombre, clave)
                LoginView.abrirMain(self)  # Cambio de ventana
                return
        alerta = Alerta("Compruebe sus credenciales", "error")
        alerta.mostrarAlerta()
        # Transferencia entre controladores

    # =======================
    # Funciones Utiles
    # =======================

    def bindCampos(nombre, clave):
        Data.clave = clave
        Data.nombre = nombre

    def crearCarpetasDefault(nombre):
        # Crea una carpeta de un usuario propio
        ManejoArchivo.crearCarpeta(nombre)
        ManejoArchivo.crearCarpeta(nombre+"/raiz")  # Crea la raiz
        ManejoArchivo.crearCarpeta(nombre+"/temporal")  # Crea el temporal

    def abrirMain(self):
        # Notese que se importa el controlador en la funcion para evitar imports circulares
        from controlador.main import Main
        self.hide()
        self.nuevaVentana = Main()
        self.nuevaVentana.show()

    def verificarNombre(nombre):
        usuarios = ManejoArchivo.leerUsuarios()
        for usuario in usuarios:
            if usuario.nombre == nombre:
                return False
        return True

# Termina la clase
