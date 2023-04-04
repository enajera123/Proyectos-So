import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication
from os import path
# utilidades
from utilidades.ManejoArchivo import ManejoArchivo
from utilidades.Data import Data
from utilidades.Alerta import Alerta

# =======================
# Controlador
# =======================


class Modificar(QMainWindow):

    def __init__(self):  # this
        super(Modificar, self).__init__()  # Inicializa la clase -> Initialize
        uic.loadUi("vista/modificar.ui", self)
        self.cbNombreUsuario.setCurrentIndex(-1)
        self.btnRegresar.clicked.connect(self.btnRegresar_click)
        self.btnCrearCarpeta.clicked.connect(self.btnCrearCarpeta_click)
        self.arbolPrincipal.itemSelectionChanged.connect(
            self.arbolPrincipal_clicked)
        Modificar.llenarCampos(self)
        ManejoArchivo.enlistarArchivos(
            self.arbolPrincipal, self.txtRuta, Data.rutaModificar)

    def btnRegresar_click(self, event):
        # Notese que se importa el controlador en la funcion para evitar imports circulares
        from controlador.main import Main
        self.hide()
        self.nuevaVentana = Main()
        self.nuevaVentana.show()

    def btnCrearCarpeta_click(self, event):
        nombreCarpeta = self.txtNombreCarpeta.text()
        if (len(nombreCarpeta) > 0):
            ruta = Data.rutaModificar+"/"+nombreCarpeta
            # hacer una verificación de nombres carpetas iguales
            ManejoArchivo.crearCarpeta(ruta)
            # falta una validacion aca para manejar los errores de sobreescritura de carpetas
            ManejoArchivo.enlistarArchivos(
                self.arbolPrincipal, self.txtRuta, Data.rutaModificar)

    def arbolPrincipal_clicked(self):
        self.txtNombreCarpeta.setText(
            Modificar.obtenerNombreItemSeleccionado(self))
        # =======================
        # Utilidades
        # =======================

    def obtenerNombreItemSeleccionado(self):
        selected_item = self.arbolPrincipal.selectedItems()  # Obtiene la linea seleccionada
        if len(selected_item) > 0:
            return ManejoArchivo.obtenerRutaCarpeta(selected_item[0].text(0))
        return Data.rutaPrincipal

    def llenarCampos(self):
        ruta = Data.rutaModificar
        self.btnCrearCarpeta.setText(Data.opcion)
        if (len(ruta) > 0):
            self.txtRuta.text = Data.rutaModificar
# Termina la clase
