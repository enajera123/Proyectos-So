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
                LoginView.bindCampos(variables[0], variables[1], variables[2], variables[3],variables[4],variables[5])
                LoginView.abrirMain(self)  # Cambio de ventana
        else:
            LoginView.mostrarAlerta("No puede dejar campos vacios", "error")

    def btnIniciarSesion_click(self, event):
        variables = LoginView.VariablesCampos(self.txtNombre.text().strip(), self.txtClave.text())
        # Verificar
        usuarios = ManejoArchivo.deserializarJSONToUsuarios(ManejoArchivo.leerUsuarios())
        for usuario in usuarios:
            if (LoginView.comprobarUsuario(usuario, variables[0], variables[1])):
                LoginView.bindCampos(variables[0], variables[1], variables[2], variables[3],variables[4],variables[5])
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
        """
        Returns:
           nombre, clave, rutaTemporal, rutaArchivos, rutaPermanente, rutaVersiones
        """
        rutaDefecto = "bin/"+nombre
        return nombre, clave, rutaDefecto+"/temporal", rutaDefecto+"/temporal/archivos.JSON",rutaDefecto+"/raiz", rutaDefecto+"/versiones"

    def crearUsuario(nombre, clave):
        usuario = Usuario(0, nombre, clave)
        ManejoArchivo.crearUsuario(usuario)
        LoginView.mostrarAlerta("Usuario Creado Exitosamente. Bienvenido "+nombre, "confirmacion")
        LoginView.crearCarpetasDefault(nombre)

    def bindCampos(*args):
        """nombre, clave, rutaTemporal, rutaArchivos, rutaPermanente, rutaVersiones """
        Data.nombre = args[0]
        Data.clave = args[1]
        Data.rutaPrincipal = args[2]
        Data.rutaArchivos = args[3]
        Data.rutaPermanente = args[4]
        Data.rutaVersiones = args[5]

    def crearCarpetasDefault(nombre):
        # Crea una carpeta de un usuario propio
        #rutaArchivos = "bin/"+nombre+"/archivos.JSON";
        ManejoArchivo.crearCarpeta_Archivo("bin/"+nombre)
        ManejoArchivo.crearCarpeta_Archivo("bin/"+nombre+"/raiz")  # Crea la raiz
        ManejoArchivo.crearCarpeta_Archivo("bin/"+nombre+"/temporal")  # Crea el temporal
        ManejoArchivo.crearCarpeta_Archivo("bin/"+nombre+"/versiones")  # Crea de versiones

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
