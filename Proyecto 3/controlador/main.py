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

        self.arbolPrincipal.itemSelectionChanged.connect(
            self.arbolPrincipal_itemSelected)

    # =======================
    #        Eventos
    # =======================
    def btnCommit_click(self, event):
        print("Codigo aqui")

    def btnUpdate_click(self, event):
        print("Codigo aqui")

    def btnRecuperar_click(self, event):
        print("codigo aqui")

    def btnCrear_click(self, event):
        ruta = Main.obtenerRutaItemSeleccionado(self)
        Data.rutaModificar = ruta
        Data.opcion = "Crear"
        if(ruta!=""):
            Main.abrirModificar(self)  # prueba crear

    def btnModificar_click(self, event):
        ruta = Main.obtenerRutaItemSeleccionado(self)
        Data.rutaModificar = ruta
        Data.opcion = "Modificar"
        if ruta != "":
            Main.abrirModificar(self)

    def btnCerrarSesion_click(self, event):
        from controlador.login import LoginView
        self.hide()
        self.nuevaVentana = LoginView()
        self.nuevaVentana.show()

    def btnEliminar_click(self, event):
        ruta = Main.obtenerRutaItemSeleccionado(self)
        if ruta != "":
            ManejoArchivo.eliminarCarpeta(ruta)
            Main.enlistarArchivos(self)
            self.btnCommit.show()

    def arbolPrincipal_itemSelected(self):
        # Obtiene la primera columna
        self.txtRuta.setText(Main.obtenerRutaItemSeleccionado(self))
    # =======================
    # Utilidades
    # =======================

    def obtenerRutaItemSeleccionado(self):
        selected_item = self.arbolPrincipal.selectedItems()  # Obtiene la linea seleccionada
        if len(selected_item) > 0:
            return ManejoArchivo.obtenerRutaCarpeta(selected_item[0].text(2))
        return Data.rutaPrincipal

    def ocultarBotones(self):
        """Oculta los botones de Commit y Update"""
        self.btnCommit.hide()
        self.btnUpdate.hide()

    def enlistarArchivos(self):
        ManejoArchivo.enlistarArchivos(
            self.arbolPrincipal, self.txtRuta, Data.rutaPrincipal)

    def abrirModificar(self):
        # Notese que se importa el controlador en la funcion para evitar imports circulares
        from controlador.modificar import Modificar
        self.hide()
        self.nuevaVentana = Modificar()
        self.nuevaVentana.show()
# Termina la clase
