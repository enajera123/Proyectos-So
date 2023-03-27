import sys
import time
from PyQt5 import uic
# QMainWindow clase ventana principal
# QApplication Arracna la aplicacion
# QTreeWidgetItem Ingresa un item al arbol
from PyQt5.QtWidgets import QMainWindow, QApplication, QTreeWidgetItem
# listdir enlista el directorio
# stat devuelve informacion del archivo
# path funciones de rutas
from os import path, listdir, stat
# Verifica el tipo de archivo
from mimetypes import MimeTypes
# Clases
# sys.path.append(path.abspath("../modelo"))
from utilidades.ManejoArchivo import ManejoArchivo
from utilidades.Data import Data


# from ..modelo.ManejoArchivo import ManejoArchivo
# =======================
# Controlador
# =======================


class Main(QMainWindow):
    # =======================
    # Inicializadores
    # =======================
    def __init__(self):  # this
        super(Main, self).__init__()  # Inicializa la clase -> Initialize
        uic.loadUi("vista/main.ui", self)
        Main.ocultarBotones(self)
        Main.conectarEventos(self)
        Main.enlistarArchivos(self)

    def conectarEventos(self):
        """Asocia los eventos con sus disparadores"""
        self.btnCommit.clicked.connect(self.btnCommit_click)

        self.btnUpdate.clicked.connect(self.btnUpdate_click)

        self.btnCrear.clicked.connect(self.btnCrear_click)

        self.btnRecuperar.clicked.connect(self.btnRecuperar_click)

        self.btnModificar.clicked.connect(self.btnModificar_click)

        self.btnEliminar.clicked.connect(self.btnEliminar_click)

        self.btnCerrarSesion.clicked.connect(self.btnCerrarSesion_click)

        self.arbolPrincipal.clicked.connect(
            self.arbolPrincipal_itemSelected)

    # =======================
    #        Eventos
    # =======================
    def btnCommit_click(self, event):
        print("Codigo voanvoa")

    def btnUpdate_click(self, event):
        print("Codigo aqui")

    def btnRecuperar_click(self, event):
        ManejoArchivo.enlistarArchivos(
            self.arbolPrincipal, self.txtRuta, "controlador")

    def btnCrear_click(self, event):
        ManejoArchivo.crearCarpeta("bin")

    def btnModificar_click(self, event):
        print("Codigo aqui")

    def btnCerrarSesion_click(self, event):
        from controlador.login import LoginView
        self.hide()
        self.nuevaVentana = LoginView()
        self.nuevaVentana.show()

    def btnEliminar_click(self, event):
        ManejoArchivo.eliminarCarpeta(Main.obtenerRutaItemSeleccionado(self))
        Main.enlistarArchivos(self)
        self.btnCommit.show()

    def arbolPrincipal_itemSelected(self, event):
        self.txtRuta.setText(Main.obtenerRutaItemSeleccionado(self))  # Obtiene la primera columna
    # =======================
    # Utilidades
    # =======================
    def obtenerRutaItemSeleccionado(self):
        selected_item = self.arbolPrincipal.selectedItems()  # Obtiene la linea seleccionada
        return ManejoArchivo.obtenerRutaCarpeta("bin/"+Data.nombre+"/"+selected_item[0].text(0))

    def ocultarBotones(self):
        """Oculta los botones de Commit y Update"""
        self.btnCommit.hide()
        self.btnUpdate.hide()

    def enlistarArchivos(self):
        ManejoArchivo.enlistarArchivos(
            self.arbolPrincipal, self.txtRuta, "bin/"+Data.nombre)


# Termina la clase
