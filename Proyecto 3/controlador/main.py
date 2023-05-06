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
        self.lblNombre.setText(Data.nombre)
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
        
        self.arbolPrincipal.itemDoubleClicked.connect(self.arbolPrincipal_dobleClick)
        
        self.arbolPrincipal.itemSelectionChanged.connect(self.arbolPrincipal_itemSelected)

    # =======================
    #        Eventos
    # =======================
    def btnCommit_click(self, event):
        from utilidades.ManejoPermisos import ManejoPermisos
        ManejoPermisos.crearVersion()  
        ManejoPermisos.commit()
        Main.mostrarVersiones(self)
        Alerta("El commit se ha creado correctamente!", "confirmacion").mostrarAlerta()
        
    def btnUpdate_click(self, event):
        ManejoArchivo.eliminarCarpeta(Data.rutaPrincipal)
        ManejoArchivo.crearCarpeta_Archivo(Data.rutaPrincipal)
        #Se copia lo que esta en raiz a la temporal
        ManejoArchivo.copiarContenidoCarpeta(Data.rutaPermanente, Data.rutaPrincipal)
        ArbolUtilidades.enlistarArchivos(self.arbolPrincipal, Data.rutaPrincipal)
        Alerta("¡Update realizado!", "confirmacion")

    def btnRecuperar_click(self, event):
        from utilidades.ManejoPermisos import ManejoPermisos
        item = ArbolUtilidades.obtenerItemSeleccionado(self.arbolTemporal, -1)
        exito = False
        ruta = item[0].text(2) 
        if not (item[0].parent()):
           exito = ManejoPermisos.recuperarVersionCompleta(ruta)
        else:
            exito = ManejoPermisos.recuperarArchivo(ruta)
        if exito:
            Alerta("¡Se hizo la recuperación exitósamente!", "confirmacion")
            ArbolUtilidades.enlistarArchivos(self.arbolPrincipal, Data.rutaPrincipal) 

    def btnCrear_click(self, event):
        ruta = Data.rutaPrincipal
        Data.rutaModificar = ruta
        if (ruta != ""):
            Main.abrirCrear(self)  # prueba crear

    def btnModificar_click(self, event):
        ruta = ArbolUtilidades.obtenerItemSeleccionado(self.arbolPrincipal, 2)
        Data.rutaModificar = ruta
        if ruta != "":
            from utilidades.ManejoPermisos import ManejoPermisos
            archivo = ManejoArchivo.leerArchivo(Data.rutaArchivos, "ruta", ruta)
            if ManejoPermisos.verificaPermiso(archivo, "[Escritura]"):
                Main.abrirModificar(self)
            else:
                Alerta("Usted no posee permisos de escritura por tanto no puede modificar los permisos de este archivo", "Error").mostrarAlerta()
            

    def btnCerrarSesion_click(self, event):
        from controlador.login import LoginView
        self.hide()
        self.nuevaVentana = LoginView()
        self.nuevaVentana.show()

    def btnEliminar_click(self, event):
        ruta = self.txtRuta.text()
        if ruta != "" and ruta != Data.rutaPrincipal:
            ManejoArchivo.eliminar(ruta, Data.rutaArchivos)
            
        Main.reiniciarCampos(self)
            
    def btnCambiarNom_click(self, event):
        NuevoNom = self.txtCambiarNom.text()
        ruta = self.txtRuta.text()
        if len(NuevoNom) > 0:
            if(ruta!=""):
                rutaNueva = path.dirname(ruta)+"/"+NuevoNom
                if not path.exists(rutaNueva):
                    archivo = ManejoArchivo.leerArchivo(Data.rutaArchivos, "ruta", ruta)
                    if(archivo):
                        archivo.ruta = rutaNueva
                        ManejoArchivo.actualizar(ruta, archivo, Data.rutaArchivos)
                        ManejoArchivo.renombrarCarpeta(ruta, rutaNueva)   
                    Main.reiniciarCampos(self)
                else:
                    Alerta("Ya existe un archivo con ese nombre, por favor escoge otro nombre", "error").mostrarAlerta()
        else:
            Main.mostrarAlerta("Debe escribir un nombre", "error")            

    def arbolPrincipal_itemSelected(self):
        # Obtiene la primera columna
        self.txtRuta.setText(ArbolUtilidades.obtenerItemSeleccionado(self.arbolPrincipal, 2))
        self.txtCambiarNom.setText(ArbolUtilidades.obtenerItemSeleccionado(self.arbolPrincipal, 0))
        
    def arbolVersiones_itemSelected(self):
        # Obtiene la primera columna
        ruta = ArbolUtilidades.obtenerItemSeleccionado(self.arbolTemporal, 2)
        self.txtRuta.setText(ruta)
        self.txtCambiarNom.setText(ArbolUtilidades.obtenerItemSeleccionado(self.arbolTemporal, 0))
        Data.rutaVersionRecuperar = Main.obtenerRutaVersion(ruta)
        
    def arbolPrincipal_dobleClick(self):
        ruta = ArbolUtilidades.obtenerItemSeleccionado(self.arbolPrincipal, 2)
        archivo = ManejoArchivo.leerArchivo(Data.rutaArchivos, "ruta", ruta)
        if archivo:
            from utilidades.ManejoPermisos import ManejoPermisos
            if ManejoPermisos.verificaPermiso(archivo, "[Ejecucion]"):
                ManejoArchivo.abrirArchivo(ruta)
            else:
                Alerta("Usted no posee permisos de ejecucion sobre este archivo", "error").mostrarAlerta()
    # =======================
    # Utilidades
    # =======================
    def obtenerRutaVersion(ruta):
        array = ruta.split("/")
        ruta = ""
        if(len(array)>3):
            for i in range(0,4):
                ruta+= array[i]+"/"
        return ruta
            
    def ocultarBotones(self):
        """Oculta los botones de Commit y Update"""
        #self.btnCommit.hide()
        #self.btnUpdate.hide()

    def enlistarArchivos(self):
        ArbolUtilidades.enlistarArchivos(self.arbolPrincipal, Data.rutaPrincipal)
        ArbolUtilidades.enlistarArchivos(self.arbolTemporal, Data.rutaVersiones)
        #self.txtRutabindQTreeWidgetItem(item, *args):
        """Ingresa los datos dentro de una fila del QTreeWidgetItem"""
        #n = 0
        #for arg in args:
         #   item.setText(n, arg)
          #  n += 1
            

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
        ArbolUtilidades.enlistarArchivos(self.arbolTemporal, Data.rutaVersiones)
# Termina la clase
    