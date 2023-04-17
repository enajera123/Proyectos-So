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
        # Variables
        variables = LoginView.VariablesCampos(self.txtNombre.text().strip(), self.txtClave.text())
        # Comprobacion
        if (len(variables[0]) > 0 and len(variables[1]) > 0):
            if (not LoginView.verificarNombre(variables[0])):
                # Alerta
                LoginView.mostrarAlerta("El nombre de usuario ya existe, por favor escoja otro", "error")
            else:
                # Creacion
                LoginView.crearUsuario(variables[0], variables[1])
                LoginView.bindCampos(variables[0], variables[1], variables[2], variables[3])
                LoginView.abrirMain(self)  # Cambio de ventana
        else:
            LoginView.mostrarAlerta("No puede dejar campos vacios", "error")

    def btnIniciarSesion_click(self, event):
        variables = LoginView.VariablesCampos(self.txtNombre.text().strip(), self.txtClave.text())
        # Verificar
        usuarios = ManejoArchivo.deserializarJSONToUsuarios(ManejoArchivo.leerUsuarios())
        for usuario in usuarios:
            if (LoginView.comprobarUsuario(usuario, variables[0], variables[1])):
                LoginView.bindCampos(variables[0], variables[1], variables[2], variables[3])
                LoginView.abrirMain(self)  # Cambio de ventana
                return
        LoginView.mostrarAlerta("Compruebe sus credenciales", "error")
        # Transferencia entre controladores

    # =======================
    # Funciones Utiles
    # =======================
    def comprobarUsuario(usuario, nombre, clave):
        if usuario.nombre == nombre and usuario.clave == clave:
            return True
        else:
            return False
    def VariablesCampos(nombre, clave):
        return nombre, clave, "bin/"+nombre+"/raiz", "bin/"+nombre+"/archivos.JSON"

    def crearUsuario(nombre, clave):
        usuario = Usuario(0, nombre, clave)
        ManejoArchivo.crearUsuario(usuario)
        LoginView.mostrarAlerta("Usuario Creado Exitosamente. Bienvenido "+nombre, "confirmacion")
        LoginView.crearCarpetasDefault(nombre)

    def bindCampos(nombre, clave, ruta, rutaArchivos):
        Data.clave = clave
        Data.nombre = nombre
        Data.rutaPrincipal = ruta
        Data.rutaArchivos = rutaArchivos

    def crearCarpetasDefault(nombre):
        # Crea una carpeta de un usuario propio
        rutaArchivos = "bin/"+nombre+"/archivos.JSON";
        ManejoArchivo.crearCarpeta("bin/"+nombre, rutaArchivos)
        ManejoArchivo.crearCarpeta("bin/"+nombre+"/raiz", rutaArchivos)  # Crea la raiz
        ManejoArchivo.crearCarpeta("bin/"+nombre+"/temporal", rutaArchivos)  # Crea el temporal
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
        usuarios = ManejoArchivo.deserializarJSONToUsuarios(usuarios)
        for usuario in usuarios:
            if usuario.nombre == nombre:
                return False
        return True

    def mostrarAlerta(contenido, tipo):
        alerta = Alerta(contenido, tipo)
        alerta.mostrarAlerta()

# Termina la clase
