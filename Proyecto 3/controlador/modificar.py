import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication
from os import path
# utilidades
from utilidades.ManejoArchivo import ManejoArchivo
from utilidades.Data import Data
from utilidades.Alerta import Alerta
# Modelo
from modelo.Archivo import Archivo
# =======================
# Controlador
# =======================


class Modificar(QMainWindow):
    rutaArchivos = "bin/"+Data.nombre+"/raiz/archivos.bin"

    def __init__(self):  # this
        super(Modificar, self).__init__()  # Inicializa la clase -> Initialize
        uic.loadUi("vista/Modificar.ui", self)
        # Eventos
        #self.cbNombreUsuario.setCurrentIndex(-1)
        self.btnRegresar.clicked.connect(self.btnRegresar_click)
        #self.arbolPrincipal.itemSelectionChanged.connect(
        #    self.arbolPrincipal_clicked)
        #Crear.llenarCampos(self)
        #ManejoArchivo.enlistarArchivos(
        #    self.arbolPrincipal, self.txtRuta, Data.rutaModificar)

    def btnRegresar_click(self, event):
        # Notese que se importa el controlador en la funcion para evitar imports circulares
        from controlador.main import Main
        self.hide()
        self.nuevaVentana = Main()
        self.nuevaVentana.show()

        # =======================
        # Utilidades
        # =======================

    def obtenerItemSeleccionado(self, opcion):
        """
            opcion (int): 
            0:nombre
            2:ruta
        """
        selected_item = self.arbolPrincipal.selectedItems()  # Obtiene la linea seleccionada
        if len(selected_item) > 0:
            return ManejoArchivo.obtenerRutaCarpeta(selected_item[0].text(opcion))
        return Data.rutaPrincipal

    def llenarCampos(self):
        ruta = Data.rutaModificar
        self.btnCrearCarpeta.setText(Data.opcion)
        for usuario in ManejoArchivo.leerUsuarios():
            self.cbNombreUsuario.addItem(usuario.nombre)
        if (len(ruta) > 0):
            self.txtRuta.setText(Data.rutaModificar)

    def mostrarAlerta(contenido, tipo):
        alerta = Alerta(contenido, tipo)
        alerta.mostrarAlerta()

    def reiniciarCampos(self):
        self.txtNombreCarpeta.setText("")
        self.txtRuta.setText(Data.rutaModificar)
# Termina la clase
