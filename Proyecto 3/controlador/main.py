import sys
import time
from PyQt5 import uic
#QMainWindow clase ventana principal
#QApplication Arracna la aplicacion
#QTreeWidgetItem Ingresa un item al arbol
from PyQt5.QtWidgets import QMainWindow, QApplication, QTreeWidgetItem
#listdir enlista el directorio
#stat devuelve informacion del archivo
#path funciones de rutas
from os import path, listdir, stat
#Verifica el tipo de archivo
from mimetypes import MimeTypes
#Clases
#sys.path.append(path.abspath("../modelo"))
from modelo.ManejoArchivo import ManejoArchivo

#from ..modelo.ManejoArchivo import ManejoArchivo
# =======================
# Controlador
# =======================
class Main(QMainWindow):
    def __init__(self):  # this
        super(Main, self).__init__()  # Inicializa la clase -> Initialize
        uic.loadUi("vista/main.ui", self)
        Main.ocultarBotones(self)
        Main.conectarEventos(self)

    def conectarEventos(self):
        """Asocia los eventos con sus disparadores"""
        self.btnCommit.clicked.connect(self.btnCommit_click)
        self.btnUpdate.clicked.connect(self.btnUpdate_click)
        self.btnCrear.clicked.connect(self.btnCrear_click)
        self.btnRecuperar.clicked.connect(self.btnRecuperar_click)
        self.btnModificar.clicked.connect(self.btnModificar_click)
        self.btnEliminar.clicked.connect(self.btnEliminar_click)

    def ocultarBotones(self):
        """Oculta los botones de Commit y Update"""
        self.btnCommit.hide()
        self.btnUpdate.hide()

    def btnCommit_click(self, event):
        print("Codigo voanvoa")

    def btnUpdate_click(self, event):
        print("Codigo aqui")

    def btnRecuperar_click(self, event):
        print("Codigo aqui")
        self.arbolPrincipal.clear()
        ruta = path.abspath("controlador")#Toma en cuenta desde el proyecto en adelante
        self.txtRuta.setText(ruta)
        if (path.isdir(ruta)):
            for element in listdir(ruta):
                name = element
                pathinfo = ruta+"/"+name
                informacion = stat(pathinfo)
                if(path.isdir(pathinfo)):
                    tipoArchivo = "Carpeta"
                else:
                    mime = MimeTypes()
                    tipoArchivo = mime.guess_type(pathinfo)[0]
                    #size = str(informacion.st_size)+" bytes"
                fecha = str(time.ctime(informacion.st_mtime))
                fila = [name,tipoArchivo]
                self.arbolPrincipal.insertTopLevelItems(0,[QTreeWidgetItem(self.arbolPrincipal,fila)])
                    

    def btnCrear_click(self, event):
        ManejoArchivo.crearCarpeta("bin")
        

    def btnModificar_click(self, event):
        print("Codigo aqui")

    def btnEliminar_click(self, event):
        print("Codigo aqui")


# Termina la clase
