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


class Modificar(QMainWindow):
    
    rutaArchivos = "bin/"+Data.nombre+"/raiz/archivos.bin"
    def __init__(self):  # this
        super(Modificar, self).__init__()  # Inicializa la clase -> Initialize
        uic.loadUi("vista/modificar.ui", self)
        # Eventos
        #clicks
        self.btnRegresar.clicked.connect(self.btnRegresar_click)
        self.btnEliminarUsuario.clicked.connect(self.btnEliminarUsuario_click)
        self.btnAgregarUsuario.clicked.connect(self.btnAgregarUsuario_click)
        self.rbtnLectura.clicked.connect(self.rbtnLectura_click)
        self.rbtnEscritura.clicked.connect(self.rbtnEscritura_click)
        self.rbtnEjecucion.clicked.connect(self.rbtnEjecucion_click)
        #Cambios
        self.arbolPermisos.itemSelectionChanged.connect(self.arbolPermisos_clicked)
        self.cbUsuarios.currentIndexChanged.connect(self.cbUsuarios_selectionChanged)
        Modificar.llenarCampos(self)
        
    def cbUsuarios_selectionChanged(self, event):
        nombre = ComboBoxUtilidades.obtenerValorComboBox(self.cbUsuarios)
        item = ArbolUtilidades.buscarItem(self.arbolPermisos, nombre, 0)
        if item:
            permisos = item.text(1)
        else:
            permisos = "[None]"
        Modificar.cambiarPermisosRadioButons(self, permisos)
        self.arbolPermisos.setCurrentItem(item)
        
    def rbtnLectura_click(self, event):
        Modificar.cambioRadioButons(self, self.rbtnLectura, "Lectura")

    def rbtnEscritura_click(self, event):
        Modificar.cambioRadioButons(self, self.rbtnEscritura, "Escritura")

    def rbtnEjecucion_click(self, event):
        Modificar.cambioRadioButons(self, self.rbtnEjecucion, "Ejecucion")

    def btnEliminarUsuario_click(self, event):
        item = ArbolUtilidades.obtenerItemSeleccionado(self.arbolPermisos, -1)
        ArbolUtilidades.eliminarItem(self.arbolPermisos, item)

    def btnRegresar_click(self, event):
        # Notese que se importa el controlador en la funcion para evitar imports circulares
        from controlador.main import Main
        Modificar.guardarCambios(self)
        self.hide()
        self.nuevaVentana = Main()
        self.nuevaVentana.show()

    def btnAgregarUsuario_click(self, event):
        arg0 = self.cbUsuarios
        arg1 = self.rbtnLectura
        arg2 = self.rbtnEscritura
        arg3 = self.rbtnEjecucion
        arg4 = self.arbolPermisos
        Generalidades.agregarUsuario(arg0,arg1,arg2,arg3,arg4)

    def arbolPermisos_clicked(self):
        item = ArbolUtilidades.obtenerItemSeleccionado(self.arbolPermisos, -1)
        for i in item:
            Modificar.cambiarPermisosRadioButons(self, i.text(1))
            self.cbUsuarios.setCurrentText(i.text(0))
        
        # =======================
        # Utilidades
        # =======================
    
    def llenarCampos(self):
        
        ruta = Data.rutaModificar
        ComboBoxUtilidades.llenarComboBox(self.cbUsuarios, ManejoArchivo.deserializarJSONToUsuarios(ManejoArchivo.leerUsuarios()))
        self.txtRuta.setText(Data.rutaModificar)
        archivo = ManejoArchivo.leerArchivo(Data.rutaArchivos, "ruta", Data.rutaModificar)
        if archivo:
            for i in range(len(archivo.listaUsuarios)):
                ArbolUtilidades.agregarItem(self.arbolPermisos, [archivo.listaUsuarios[i], archivo.listaPermisos[i]])

    def guardarCambios(self):
        archivo = ManejoArchivo.leerArchivo(Data.rutaArchivos, "ruta", Data.rutaModificar)
        if archivo:
            id = archivo.id
            ruta = archivo.ruta
            tipoArchivo = archivo.tipoArchivo
            listaUsuarios = ArbolUtilidades.obtenerDatosColumna(self.arbolPermisos, 0)
            listaPermisos = ArbolUtilidades.obtenerDatosColumna(self.arbolPermisos, 1)
            archivo = Archivo(id, ruta, tipoArchivo, listaUsuarios, listaPermisos)
            ManejoArchivo.actualizar(ruta, archivo, Data.rutaArchivos)

    def cambioRadioButons(self, radioButon, permiso):
        item = ArbolUtilidades.obtenerItemSeleccionado(self.arbolPermisos, -1)
        for i in item:
            if not radioButon.isChecked():
                cadena = i.text(1)
                cadena = cadena.replace("["+permiso+"]", "")
            else:
                cadena = i.text(1)
                cadena = cadena.replace(cadena, cadena+"["+permiso+"]")
            ArbolUtilidades.modificarItem(cadena, i, 1)
            
    def cambiarPermisosRadioButons(self, usuario):
        self.cbUsuarios.setCurrentText(usuario)
        RadioButonUtilidades.llenarRadioButtons(self, usuario)
# Termina la clase
