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
from modelo.Archivo import Archivo

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
        LoginView.btnIniciarSesion_click(self, event)

    def btnCrear_click(self, event):
        nombre = self.txtNombre.text().strip()
        clave = self.txtClave.text()
        ruta = "bin/"+nombre+"/raiz"
        rutaArchivos = "bin/"+nombre+"/raiz/archivos.bin"
        if (len(nombre) > 0 and len(clave) > 0):
            if (not LoginView.verificarNombre(nombre)):
                LoginView.mostrarAlerta(
                    "El nombre de usuario ya existe, por favor escoja otro", "error")
            else:
                LoginView.crearCarpetasDefault(nombre)
                usuario = Usuario(nombre, clave)
                ManejoArchivo.guardarUsuarios([usuario])
                LoginView.mostrarAlerta(
                    "Usuario Creado Exitosamente. Bienvenido "+nombre, "confirmacion")
                LoginView.bindCampos(nombre, clave, ruta, rutaArchivos)
                LoginView.abrirMain(self)  # Cambio de ventana
        else:
            LoginView.mostrarAlerta("No puede dejar campos vacios", "error")

    def btnIniciarSesion_click(self, event):
        nombre = self.txtNombre.text().strip()
        clave = self.txtClave.text()
        ruta = "bin/"+nombre+"/raiz"
        rutaArchivos = "bin/"+nombre+"/raiz/archivos.bin"
        # Verificar
        usuarios = ManejoArchivo.leerUsuarios()
        for usuario in usuarios:
            if (ManejoArchivo.comprobarUsuario(usuario, nombre, clave)):
                LoginView.bindCampos(nombre, clave, ruta, rutaArchivos)
                LoginView.abrirMain(self)  # Cambio de ventana
                return
            LoginView.mostrarAlerta("Compruebe sus credenciales", "error")
        # Transferencia entre controladores

    # =======================
    # Funciones Utiles
    # =======================

    def bindCampos(nombre, clave, ruta, rutaArchivos):
        Data.clave = clave
        Data.nombre = nombre
        Data.rutaPrincipal = ruta
        Data.rutaArchivos = rutaArchivos

    def crearCarpetasDefault(nombre):
        # Crea una carpeta de un usuario propio
        ManejoArchivo.crearCarpeta("bin/"+nombre)
        ManejoArchivo.crearCarpeta("bin/"+nombre+"/raiz")  # Crea la raiz
        ManejoArchivo.crearCarpeta(
            "bin/"+nombre+"/temporal")  # Crea el temporal
        # ManejoArchivo.guardarArchivos(
        #     archivos, "bin/"+nombre+"/raiz/archivos.bin")

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

    def mostrarAlerta(contenido, tipo):
        alerta = Alerta(contenido, tipo)
        alerta.mostrarAlerta()

# Termina la clase
