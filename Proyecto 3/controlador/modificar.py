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
        uic.loadUi("vista/modificar.ui", self)
        # Eventos
        self.cbNombreUsuario.setCurrentIndex(-1)
        self.btnRegresar.clicked.connect(self.btnRegresar_click)
        self.btnCrearCarpeta.clicked.connect(self.btnCrearCarpeta_click)
        self.arbolPrincipal.itemSelectionChanged.connect(self.arbolPrincipal_clicked)
        Modificar.llenarCampos(self)
        ManejoArchivo.enlistarArchivos(self.arbolPrincipal, self.txtRuta, Data.rutaModificar)

    def btnRegresar_click(self, event):
        # Notese que se importa el controlador en la funcion para evitar imports circulares
        from controlador.main import Main
        self.hide()
        self.nuevaVentana = Main()
        self.nuevaVentana.show()

    def btnCrearCarpeta_click(self, event):
        nombreCarpeta = self.txtNombreCarpeta.text()
        ruta = self.txtRuta.text()
        if (len(nombreCarpeta) > 0):
            # hacer una verificación de nombres carpetas iguales
            if (self.btnCrearCarpeta.text() == "Crear"):  # Crear
                ManejoArchivo.crearCarpeta(ruta+"/"+nombreCarpeta, Data.rutaArchivos)
            # falta una validacion aca para manejar los errores de sobreescritura de carpetas
                ManejoArchivo.enlistarArchivos(
                    self.arbolPrincipal, self.txtRuta, Data.rutaModificar)
            else:  # Modificar
                rutaNueva = path.dirname(ruta)+"/"+nombreCarpeta
                ManejoArchivo.renombrarCarpeta(ruta, rutaNueva)
                Data.rutaModificar = rutaNueva
                Modificar.reiniciarCampos(self)
        else:
            Modificar.mostrarAlerta("Debe escribir un nombre", "error")

    def arbolPrincipal_clicked(self):
        self.txtNombreCarpeta.setText(
            Modificar.obtenerItemSeleccionado(self, 0))
        self.txtRuta.setText(Modificar.obtenerItemSeleccionado(self, 2))

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
        for usuario in ManejoArchivo.deserializarJSONToUsuarios(ManejoArchivo.leerUsuarios()):
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
