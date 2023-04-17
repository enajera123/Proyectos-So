import sys
import time
import os
# Manejo Archivos
import shutil
import pickle
import json
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
    rutaUsuarios = "bin/usuarios.JSON"

    def __init__(self):
        super(ManejoArchivo, self).__init__()
    # =======================
    # Manejo Carpetas
    # =======================

    def crearCarpeta(rutaArchivo, rutaDefault):
        from modelo.Archivo import Archivo
        if (path.isdir(path.dirname(rutaArchivo))):
            if (os.path.exists(rutaArchivo)):
                shutil.rmtree(rutaArchivo)  # Borrado recursivo
            if "." in rutaArchivo:
                open(rutaArchivo,"w")
            else:
                os.mkdir(rutaArchivo)
            tipoArchivo = ManejoArchivo.obtenerTipoArchivo(rutaArchivo)
            archivo = Archivo(rutaArchivo, tipoArchivo)
            ManejoArchivo.crearArchivo(archivo, rutaDefault)

    def eliminarCarpeta(rutaAbsoluta, rutaDefault):
        if (os.path.exists(rutaAbsoluta)):
            shutil.rmtree(rutaAbsoluta)  # Borrado recursivo
            ManejoArchivo.eliminarArchivo(rutaAbsoluta, rutaDefault)

    def renombrarCarpeta(rutaAntigua, rutaNueva, rutaDefault):
        if (path.exists(rutaAntigua)):
            os.rename(rutaAntigua, rutaNueva)
            ManejoArchivo.actualizarArchivo(rutaAntigua, rutaNueva, rutaDefault)

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
                    ManejoArchivo.bindQTreeWidgetItem(item, file, "Carpeta", os.path.relpath(full_path))
                    # Listar todas las subcarpetas recursivamente
                    ManejoArchivo.listar_carpetas(full_path, item)
                # Si es un archivo, agregarlo al árbol
                elif os.path.isfile(full_path):
                    archivo = QTreeWidgetItem(parent)
                    tipoArchivo = ManejoArchivo.obtenerTipoArchivo(full_path)
                    ManejoArchivo.bindQTreeWidgetItem(archivo, file, tipoArchivo, os.path.relpath(full_path))

    

    # =======================
    # Control de usuarios
    # =======================

    def leerUsuarios():
        if not os.path.exists(ManejoArchivo.rutaUsuarios):
            return []
        with open(ManejoArchivo.rutaUsuarios, 'r') as f:
            return json.load(f)

    def leerUsuario(id):
        usuarios = ManejoArchivo.leerUsuarios()
        usuario = next(
            (usuario for usuario in usuarios if usuario['id'] == id), None)
        return Usuario(**usuario) if usuario else None

    def crearUsuario(usuario):
        usuarios = ManejoArchivo.leerUsuarios()
    # Validamos que el id del usuario no esté siendo utilizado por otro usuario
        if next((x for x in usuarios if x['id'] == usuario.id), None) is not None:
            # Si el id ya está en uso, buscamos un nuevo id que no esté siendo utilizado
            nuevo_id = max([x['id'] for x in usuarios]) + 1
            # Actualizamos el id del usuario
            usuario.id = nuevo_id
        usuarios.append(usuario.__dict__)
        ManejoArchivo.guardarUsuarios(usuarios)

    def guardarUsuarios(usuarios):
        # Convertimos la lista de usuarios a una lista de diccionarios y la guardamos en el archivo
        with open(ManejoArchivo.rutaUsuarios, 'w') as f:
            json.dump(usuarios, f)

    def eliminarUsuario(id):
        usuarios = leerUsuarios()
        index = next((i for i, x in enumerate(
            usuarios) if x['id'] == id), None)
        if index is not None:
            del usuarios[index]
            ManejoArchivo.guardarUsuarios(usuarios)

    def deserializarJSONToUsuarios(array):
        usuarios = []
        for i in array:
            usuario = Usuario(i['id'], i['nombre'], i['clave'])
            usuarios.append(usuario)
        return usuarios

# =======================
# Control de archivos
# =======================
    def guardarArchivos(archivos, ruta):
        with open(ruta, 'w') as f:
            json.dump(archivos, f)

    def leerArchivos(ruta):
        if not os.path.exists(ruta):
            return []
        with open(ruta, 'r') as f:
            return json.load(f)
        
    def actualizarArchivo(rutaAntigua, rutaNueva,rutaDefault):
        
        archivos = ManejoArchivo.leerArchivos(rutaDefault)
        for i in archivos:
            if(i['ruta'] == rutaAntigua):
                i['ruta'] = rutaNueva
        ManejoArchivo.guardarArchivos(archivos,rutaDefault)
        
    def crearArchivo(archivo, ruta):
        archivos = ManejoArchivo.leerArchivos(ruta)
        archivos.append(archivo.__dict__)
        ManejoArchivo.guardarArchivos(archivos, ruta)

    def eliminarArchivo(rutaArchivo, rutaDefault):
        archivos = ManejoArchivo.leerArchivos(rutaDefault)
        iterator = []
        for i in archivos:#Borrado iterativo en el JSON
            if not(rutaArchivo in i['ruta']):#Si no esta contenido
                iterator.append(i)#Se agrega
        ManejoArchivo.guardarArchivos(iterator, rutaDefault)#Se guarda el arreglo
    #=======================
    #		Utilidades
    #=======================
    def obtenerRutaCarpeta(nombreCarpeta):
        return path.relpath(nombreCarpeta)
    
    def obtenerTipoArchivo(ruta):
        if (path.isdir(ruta)):
            tipoArchivo = "Carpeta"
        else:
            mime = MimeTypes()
            tipoArchivo = mime.guess_type(ruta)[0]
        return tipoArchivo
    
    def bindQTreeWidgetItem(item, *args):
        """Ingresa los datos dentro de una fila del QTreeWidgetItem"""
        n = 0
        for arg in args:
            item.setText(n, arg)
            n += 1
            
    def enlistarArchivos(arbol, ruta):
        """
        Args:
            arbol (QtreeWidget): Arbol
            ruta (String): ruta relativa
        """
        arbol.clear()
        
        ruta = path.abspath(ruta)
        if (path.isdir(ruta)):
            for element in listdir(ruta):
                nombre = element
                archivo = ruta+"/"+nombre
                tipoArchivo = ManejoArchivo.obtenerTipoArchivo(archivo)
                fila = [nombre, tipoArchivo, os.path.relpath(archivo)]
                item = QTreeWidgetItem(arbol, fila)
                arbol.insertTopLevelItems(0, [item])
                ManejoArchivo.listar_carpetas(ruta+"/"+item.text(0), item)
