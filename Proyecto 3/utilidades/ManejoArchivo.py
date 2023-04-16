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
from utilidades.Data import Data


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

    def crearCarpeta(ruta):
        """
        Solo crea dentro de la carpeta bin
        """
        if (path.isdir(path.dirname(ruta))):
            if (os.path.exists(ruta)):
                shutil.rmtree(ruta)  # Borrado recursivo
            os.mkdir(ruta)

    def eliminarCarpeta(rutaAbsoluta):
        if (os.path.exists(rutaAbsoluta)):
            shutil.rmtree(rutaAbsoluta)  # Borrado recursivo

    def renombrarCarpeta(nombreCarpeta, nuevoNombre):
        if (path.exists(nombreCarpeta)):
            os.rename(nombreCarpeta, nuevoNombre)

    def obtenerRutaCarpeta(nombreCarpeta):
        return path.relpath(nombreCarpeta)

    def enlistarArchivos(arbol, txtRuta, ruta):
        """
        Args:
            arbol (QtreeWidget): Arbol
            txtRuta (QLineEdit): TextBox
            ruta (String): ruta relativa
        """
        arbol.clear()
        txtRuta.setText(ruta)  # Ingresa en el txt la ruta de la raiz(Default)
        ruta = path.abspath(ruta)

        if (path.isdir(ruta)):
            for element in listdir(ruta):
                nombre = element
                archivo = ruta+"/"+nombre
                if (path.isdir(archivo)):
                    tipoArchivo = "Carpeta"
                else:
                    mime = MimeTypes()
                    tipoArchivo = mime.guess_type(archivo)[0]
                fila = [nombre, tipoArchivo, os.path.relpath(archivo)]
                item = QTreeWidgetItem(arbol, fila)
                arbol.insertTopLevelItems(0, [item])
                ManejoArchivo.listar_carpetas(ruta+"/"+item.text(0), item)

    def listar_carpetas(path, parent):
        """
        Args:
            path (string): Ruta Absoluta
            parent (QTreeWidgetItem): item del tree
        """
        # Verificar si la ruta es un directorio
        if os.path.isdir(path):
            # Obtener una lista de todos los archivos y carpetas en el directorio
            files = os.listdir(path)
            # Recorrer todos los archivos y carpetas
            for file in files:
                # Obtener la ruta completa del archivo o carpeta
                full_path = os.path.join(path, file)
                # Si es una carpeta, agregarla al árbol
                if os.path.isdir(full_path):
                    item = QTreeWidgetItem(parent)
                    ManejoArchivo.bindQTreeWidgetItem(
                        item, file, "Carpeta", os.path.relpath(full_path))
                    # Listar todas las subcarpetas recursivamente
                    ManejoArchivo.listar_carpetas(full_path, item)
                # Si es un archivo, agregarlo al árbol
                elif os.path.isfile(full_path):
                    archivo = QTreeWidgetItem(parent)
                    mime = MimeTypes()
                    tipoArchivo = mime.guess_type(full_path)[0]
                    ManejoArchivo.bindQTreeWidgetItem(
                        archivo, file, tipoArchivo, os.path.relpath(full_path))

    def bindQTreeWidgetItem(item, *args):
        """Ingresa los datos dentro de una fila del QTreeWidgetItem"""
        n = 0
        for arg in args:
            item.setText(n, arg)
            n += 1

    # =======================
    # Control de usuarios
    # =======================
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
# =======================
# Control de archivos
# =======================

    def guardarArchivos(archivo, ruta):
        with open(ruta, "wb") as arch:
            pickle.dump(archivo, arch)

    def leerArchivos(ruta):
        try:
            with open(ruta, "rb") as archivo:
                archivos_leidos = pickle.load(archivo)
        except FileNotFoundError:
            archivos_leidos = []
        return archivos_leidos

    def eliminarArchivo(rutaArchivo, ruta):
        try:
            with open(ruta, "rb+") as file:
                archivos_leidos = pickle.load(file)
                for archivo_leido in archivos_leidos:
                    if archivo_leido.ruta == rutaArchivo:
                        archivos_leidos.remove(archivo_leido)
                file.seek(0)  # Posiciona el cursos en 0
                pickle.dump(archivos_leidos, file)  # Sobreescribe
                file.truncate()  # Asegura
        except FileNotFoundError:
            return
