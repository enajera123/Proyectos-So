import sys
from PyQt5 import uic

from PyQt5.QtWidgets import QMainWindow, QApplication
from os import path
# utilidades
from utilidades.ManejoArchivo import ManejoArchivo
from utilidades.Data import Data
from utilidades.Alerta import Alerta
from utilidades.ArbolUtilidades import ArbolUtilidades
from utilidades.RadioButonUtilidades import RadioButonUtilidades
from utilidades.Generalidades import Generalidades
from utilidades.ComboBoxUtilidades import ComboBoxUtilidades
# Modelo
from modelo.Archivo import Archivo

# =======================
# Controlador
# =======================


class Crear(QMainWindow):
    rutaArchivos = "bin/"+Data.nombre+"/raiz/archivos.bin"

    def __init__(self):  # this
        super(Crear, self).__init__()  # Inicializa la clase -> Initialize
        uic.loadUi("vista/crear.ui", self)
        # Eventos
        # Botones
        self.cbNombreUsuario.setCurrentIndex(-1)
        self.btnRegresar.clicked.connect(self.btnRegresar_click)
        self.btnCrearCarpeta.clicked.connect(self.btnCrearCarpeta_click)
        self.btnSubirNivel.clicked.connect(self.btnSubirNivel_click)
        self.btnAgregarUsuario.clicked.connect(self.btnAgregarUsuario_click)
        self.btnEliminarUsuario.clicked.connect(self.btnEliminarUsuario_click)
        # Cambios en arboles
        self.arbolPrincipal.itemSelectionChanged.connect(
            self.arbolPrincipal_clicked)
        Crear.llenarCampos(self)
        ManejoArchivo.enlistarArchivos(self.arbolPrincipal, Data.rutaModificar)

    def btnEliminarUsuario_click(self, event):
        item = ArbolUtilidades.obtenerItemSeleccionado(self.arbolPermisos, -1)
        ArbolUtilidades.eliminarItem(self.arbolPermisos, item)

    def btnAgregarUsuario_click(self, event):
        arg0 = self.cbNombreUsuario
        arg1 = self.rbtnLectura
        arg2 = self.rbtnEscritura
        arg3 = self.rbtnEjecucion
        arg4 = self.arbolPermisos
        Generalidades.agregarUsuario(arg0,arg1,arg2,arg3,arg4)

    def btnSubirNivel_click(self, event):
        ruta = self.txtRuta.text()
        if (ruta != "bin/"+Data.nombre+"/raiz"):
            ruta = path.dirname(ruta)
            ArbolUtilidades.buscarItem(self.arbolPrincipal, ruta,2)
            ArbolUtilidades.desplegarItem(ArbolUtilidades.obtnerItemSeleccionado(self.arbolPrincipal, -1), False)
            self.txtRuta.setText(ruta)
            if ruta == "bin/"+Data.nombre+"/raiz":
                self.arbolPrincipal.collapseAll()

    def btnRegresar_click(self, event):
        # Notese que se importa el controlador en la funcion para evitar imports circulares
        from controlador.main import Main
        self.hide()
        self.nuevaVentana = Main()
        self.nuevaVentana.show()

    def btnCrearCarpeta_click(self, event):
        nombreCarpeta = self.txtNombreCarpeta.text()
        ruta = self.txtRuta.text()
        permisos = ArbolUtilidades.obtenerDatosColumna(self.arbolPermisos, 1)
        usuarios = ArbolUtilidades.obtenerDatosColumna(self.arbolPermisos, 0)
        if (len(nombreCarpeta) > 0):
            # hacer una verificación de nombres carpetas iguales
                ManejoArchivo.crearCarpeta(ruta+"/"+nombreCarpeta, Data.rutaArchivos,usuarios,permisos)
            # falta una validacion aca para manejar los errores de sobreescritura de carpetas
                ManejoArchivo.enlistarArchivos(self.arbolPrincipal, Data.rutaModificar)
                Crear.reiniciarCampos(self)
        else:
            Crear.mostrarAlerta("Debe escribir un nombre", "error")

    def arbolPrincipal_clicked(self):
        self.txtRuta.setText(ArbolUtilidades.obtenerItemSeleccionado(self.arbolPrincipal, 2))
        # =======================
        # Utilidades
        # =======================

    def llenarCampos(self):
        ruta = Data.rutaModificar
        ComboBoxUtilidades.llenarComboBox(self.cbNombreUsuario, ManejoArchivo.deserializarJSONToUsuarios(ManejoArchivo.leerUsuarios()))
        self.txtRuta.setText(Data.rutaModificar)
        usuario = Data.nombre
        ArbolUtilidades.agregarItem(self.arbolPermisos, [usuario,"[Lectura][Escritura][Ejecucion]"])

    def reiniciarCampos(self):
        self.txtNombreCarpeta.setText("")
        self.txtRuta.setText(Data.rutaModificar)
        RadioButonUtilidades.reiniciarRadioButons(self.rbtnEscritura,self.rbtnLectura,self.rbtnEjecucion)
        self.arbolPermisos.clear()
        ArbolUtilidades.agregarItem(self.arbolPermisos, [Data.nombre,"[Lectura][Escritura][Ejecucion]"])
        

    
# Termina la clase
