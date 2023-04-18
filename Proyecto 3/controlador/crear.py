import sys
from PyQt5 import uic

from PyQt5.QtWidgets import QMainWindow, QApplication
from os import path
# utilidades
from utilidades.ManejoArchivo import ManejoArchivo
from utilidades.Data import Data
from utilidades.Alerta import Alerta
from utilidades.ArbolUtilidades import ArbolUtilidades
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
        item = Crear.obetenerValorComboBox(self.cbNombreUsuario)
        permisos = Crear.leerRadioButons(self)
        if (item):
            ArbolUtilidades.agregarItem(self.arbolPermisos, [item, permisos])
            Crear.reiniciarRadioButons(self)

    def btnSubirNivel_click(self, event):
        ruta = self.txtRuta.text()
        if (ruta != "bin/"+Data.nombre+"/raiz"):
            ruta = path.dirname(ruta)
            ArbolUtilidades.buscarItem(self.arbolPrincipal, ruta)
            ArbolUtilidades.desplegarItem(
                ArbolUtilidades.obtenerItemSeleccionado(self.arbolPrincipal, -1), False)
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
        if (len(nombreCarpeta) > 0):
            # hacer una verificación de nombres carpetas iguales
            if (self.btnCrearCarpeta.text() == "Crear"):  # Crear
                ManejoArchivo.crearCarpeta(ruta+"/"+nombreCarpeta, Data.rutaArchivos)
            # falta una validacion aca para manejar los errores de sobreescritura de carpetas
                ManejoArchivo.enlistarArchivos(self.arbolPrincipal, Data.rutaModificar)
            else:  # Modificar
                rutaNueva = path.dirname(ruta)+"/"+nombreCarpeta
                ManejoArchivo.renombrarCarpeta(ruta, rutaNueva)
                Data.rutaModificar = rutaNueva
                Crear.reiniciarCampos(self)
        else:
            Crear.mostrarAlerta("Debe escribir un nombre", "error")

    def arbolPrincipal_clicked(self):
        self.txtNombreCarpeta.setText(
            ArbolUtilidades.obtenerItemSeleccionado(self.arbolPrincipal, 0))
        self.txtRuta.setText(
            ArbolUtilidades.obtenerItemSeleccionado(self.arbolPrincipal, 2))
        # =======================
        # Utilidades
        # =======================

    def obetenerValorComboBox(comboBox):
        indice = comboBox.currentIndex()
        valor = comboBox.itemText(indice)
        return valor

    def llenarCampos(self):
        ruta = Data.rutaModificar
        for usuario in ManejoArchivo.deserializarJSONToUsuarios(ManejoArchivo.leerUsuarios()):
            self.cbNombreUsuario.addItem(usuario.nombre)
            self.txtRuta.setText(Data.rutaModificar)

    def mostrarAlerta(contenido, tipo):
        alerta = Alerta(contenido, tipo)
        alerta.mostrarAlerta()

    def reiniciarCampos(self):
        self.txtNombreCarpeta.setText("")
        self.txtRuta.setText(Data.rutaModificar)

    def leerRadioButons(self):
        cadena = ""
        lectura = self.rbtnLectura
        escritura = self.rbtnEscritura
        ejecucion = self.rbtnEjecucion
        if (lectura.isChecked()):
            cadena += "[Lectura]"
        if (escritura.isChecked()):
            cadena += "[Escritura]"
        if (ejecucion.isChecked()):
            cadena += "[Ejecucion]"
        if not (lectura.isChecked() or escritura.isChecked() or ejecucion.isChecked()):
            cadena += "[None]"
        return cadena
    def reiniciarRadioButons(self):
        self.rbtnLectura.setChecked(False)
        self.rbtnEscritura.setChecked(False)
        self.rbtnEjecucion.setChecked(False)
        
# Termina la clase
