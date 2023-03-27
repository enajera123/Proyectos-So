import sys
import time
import os
# Manejo Archivos
import shutil
import pickle
# path funciones de rutas
from os import path, listdir, stat
# Verifica el tipo de archivo
from mimetypes import MimeTypes
# QTreeWidgetItem Ingresa un item al arbol
from PyQt5.QtWidgets import QTreeWidgetItem
from modelo.Usuario import Usuario


class ManejoArchivo:
    # =======================
    # Constantes
    # =======================
    rutaUsuarios = "bin/usuarios.bin"

    def __init__(self):
        super(ManejoArchivo, self).__init__()
    # =======================
    # Funciones
    # =======================

    def crearCarpeta(nombreCarpeta):
        if (os.path.exists("bin/"+nombreCarpeta)):
            shutil.rmtree("bin/"+nombreCarpeta)  # Borrado recursivo
        os.mkdir("bin/"+nombreCarpeta)

    def eliminarCarpeta(rutaAbsoluta):
        print(path.relpath(rutaAbsoluta))
        if(os.path.exists(path.relpath(rutaAbsoluta))):
            shutil.rmtree(path.relpath(rutaAbsoluta))  # Borrado recursivo
            print("exist")
        print("no exist")

    def obtenerRutaCarpeta(nombreCarpeta):
        return path.abspath(nombreCarpeta)

    def enlistarArchivos(arbol, txtRuta, ruta):
        arbol.clear()
        ruta = path.abspath(ruta)
        txtRuta.setText(ruta)
        if (path.isdir(ruta)):
            for element in listdir(ruta):
                nombre = element
                archivo = ruta+"/"+nombre
                informacionArchivo = stat(archivo)
                if (path.isdir(archivo)):
                    tipoArchivo = "Carpeta"
                else:
                    mime = MimeTypes()
                    tipoArchivo = mime.guess_type(archivo)[0]
                    # size = str(informacion.st_size)+" bytes"
                    # fecha = str(time.ctime(informacion.st_mtime))
                fila = [nombre, tipoArchivo]
                arbol.insertTopLevelItems(0, [QTreeWidgetItem(arbol, fila)])

    def guardarUsuarios(usuarios):
        usuarios_leidos = ManejoArchivo.leerUsuarios()
        for usuario in usuarios:
            usuarios_leidos.append(usuario)
        with open(ManejoArchivo.rutaUsuarios, "wb") as archivo:
            pickle.dump(usuarios_leidos, archivo)

    def leerUsuarios():
        try:
            with open(ManejoArchivo.rutaUsuarios, "rb") as archivo:
                usuarios = pickle.load(archivo)
        except FileNotFoundError:
            usuarios = []
        return usuarios

    def comprobarUsuario(usuario, nombre, clave):
        if usuario.nombre == nombre and usuario.clave == clave:
            return True
        else:
            return False
