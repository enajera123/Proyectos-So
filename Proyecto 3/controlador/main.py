import sys
from datetime import datetime
from PyQt5 import uic
# QMainWindow clase ventana principal
# QApplication Arracna la aplicacion
# QTreeWidgetItem Ingresa un item al arbol
from PyQt5.QtWidgets import QMainWindow, QApplication, QTreeWidgetItem, QInputDialog
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
from utilidades.Alerta import Alerta
from utilidades.ArbolUtilidades import ArbolUtilidades


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
        
        self.btnCambiarNom.clicked.connect(self.btnCambiarNom_click)

        self.btnCerrarSesion.clicked.connect(self.btnCerrarSesion_click)
        
        self.arbolTemporal.itemSelectionChanged.connect(self.arbolVersiones_itemSelected)
        

        self.arbolPrincipal.itemSelectionChanged.connect(self.arbolPrincipal_itemSelected)

    # =======================
    #        Eventos
    # =======================
    def btnCommit_click(self, event):
        nombre = Data.nombre+"("+datetime.now().strftime("%Y-%m-%d %H-%M-%S")+")"
        rutaVersion = "bin/"+Data.nombre+"/versiones"+"/"+nombre
        ManejoArchivo.procesarRegistros()
        '''            
        if(len(listdir(Data.rutaPermanente))>0):
            ManejoArchivo.eliminarCarpeta2(Data.rutaPermanente)
            ManejoArchivo.crearCarpeta2(Data.rutaPermanente)
        ManejoArchivo.copiarArchivos(Data.rutaPrincipal, Data.rutaPermanente)
        '''
        ManejoArchivo.crearCarpeta2(rutaVersion)
        ManejoArchivo.copiarArchivos(Data.rutaPermanente, rutaVersion)
        Main.mostrarVersiones(self)
        Alerta("El commit se ha creado correctamente!", "confirmacion").mostrarAlerta()
        

    def btnUpdate_click(self, event):
        ManejoArchivo.eliminarCarpeta2(Data.rutaPrincipal)
        ManejoArchivo.crearCarpeta2(Data.rutaPrincipal)
        ManejoArchivo.copiarArchivos(Data.rutaPermanente, Data.rutaPrincipal)
        ManejoArchivo.enlistarArchivos(self.arbolPrincipal, Data.rutaPrincipal)

    def btnRecuperar_click(self, event):
        ruta = ArbolUtilidades.obtenerItemSeleccionado(self.arbolTemporal, 2)
        #ManejoArchivo.eliminarCarpeta2(Data.rutaPrincipal)
        #ManejoArchivo.crearCarpeta2(Data.rutaPrincipal)
        ManejoArchivo.copiarArchivos2(ruta, Data.rutaPrincipal)
        ManejoArchivo.enlistarArchivos(self.arbolPrincipal, Data.rutaPrincipal)

    def btnCrear_click(self, event):
        ruta = Data.rutaPrincipal
        Data.rutaModificar = ruta
        if (ruta != ""):
            Main.abrirCrear(self)  # prueba crear

    def btnModificar_click(self, event):
        ruta = ArbolUtilidades.obtenerItemSeleccionado(self.arbolPrincipal, 2)
        Data.rutaModificar = ruta
        if ruta != "":
            Main.abrirModificar(self)

    def btnCerrarSesion_click(self, event):
        from controlador.login import LoginView
        self.hide()
        self.nuevaVentana = LoginView()
        self.nuevaVentana.show()

    def btnEliminar_click(self, event):
        ruta = self.txtRuta.text()
        if ruta != "" and ruta != Data.rutaPrincipal:
            ManejoArchivo.crearRegistro("Eliminar",ruta)
            ManejoArchivo.eliminarCarpeta(ruta, Data.rutaArchivos)
        Main.reiniciarCampos(self)
            
    def btnCambiarNom_click(self, event):
        NuevoNom = self.txtCambiarNom.text()
        ruta = self.txtRuta.text()
        if len(NuevoNom) > 0:
            if(ruta!=""):
                rutaNueva = path.dirname(ruta)+"/"+NuevoNom
                ManejoArchivo.renombrarCarpeta(ruta, rutaNueva, Data.rutaArchivos)
                ManejoArchivo.crearRegistro("Renombrar",ruta,rutaNueva)   
            Main.reiniciarCampos(self)
        else:
            Main.mostrarAlerta("Debe escribir un nombre", "error")            

    def arbolPrincipal_itemSelected(self):
        # Obtiene la primera columna
        self.txtRuta.setText(ArbolUtilidades.obtenerItemSeleccionado(self.arbolPrincipal, 2))
        self.txtCambiarNom.setText(ArbolUtilidades.obtenerItemSeleccionado(self.arbolPrincipal, 0))
        
    def arbolVersiones_itemSelected(self):
        # Obtiene la primera columna
        self.txtRuta.setText(ArbolUtilidades.obtenerItemSeleccionado(self.arbolTemporal, 2))
        self.txtCambiarNom.setText(ArbolUtilidades.obtenerItemSeleccionado(self.arbolTemporal, 0))
    # =======================
    # Utilidades
    # =======================
        
    def ocultarBotones(self):
        """Oculta los botones de Commit y Update"""
        #self.btnCommit.hide()
        #self.btnUpdate.hide()

    def enlistarArchivos(self):
        ManejoArchivo.enlistarArchivos(self.arbolPrincipal, Data.rutaPrincipal)
        self.txtRuta.setText(Data.rutaPrincipal)  # Ingresa en el txt la ruta de la raiz(Default)
        Main.mostrarVersiones(self)

    def abrirModificar(self):
        # Notese que se importa el controlador en la funcion para evitar imports circulares
        from controlador.modificar import Modificar
        self.hide()
        self.nuevaVentana = Modificar()
        self.nuevaVentana.show()
        
    def abrirCrear(self):
        from controlador.crear import Crear
        self.hide()
        self.nuevaVentana = Crear()
        self.nuevaVentana.show()
        
    def reiniciarCampos(self):
        self.txtCambiarNom.setText("")
        self.txtRuta.setText(Data.rutaModificar)
        Main.enlistarArchivos(self)
        
    def mostrarAlerta(contenido, tipo):
        alerta = Alerta(contenido, tipo)
        alerta.mostrarAlerta()
        
    def mostrarVersiones(self):
        ManejoArchivo.enlistarArchivos(self.arbolTemporal, Data.rutaVersiones)
# Termina la clase
