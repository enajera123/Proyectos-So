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
from modelo.Archivo import Archivo
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
    def crearCarpeta2(ruta):
        from modelo.Archivo import Archivo
        os.mkdir(ruta)#creacion de carpetas    
        
    def crearCarpeta(rutaArchivo, rutaDefault, *args):
        from modelo.Archivo import Archivo
        if (path.isdir(path.dirname(rutaArchivo))):
            if (os.path.exists(rutaArchivo)):#Si existe lo borra
                shutil.rmtree(rutaArchivo)  # Borrado recursivo
            if "." in rutaArchivo:#Creacion de archivos
                open(rutaArchivo,"w")
            else:
                os.mkdir(rutaArchivo)#creacion de carpetas
            tipoArchivo = ManejoArchivo.obtenerTipoArchivo(rutaArchivo)
            if(len(args)>=2):
                archivo = Archivo(rutaArchivo, tipoArchivo,args[0],args[1])
            else:
                archivo = Archivo(rutaArchivo, tipoArchivo,[],[])
                
            ManejoArchivo.crearArchivo(archivo, rutaDefault)#Crea archivo
            
    def eliminarCarpeta2(ruta):
        if(path.exists(ruta) and path.isdir(ruta)):
            shutil.rmtree(ruta)
            
    def eliminarCarpeta(rutaAbsoluta, rutaDefault):
        if (path.exists(rutaAbsoluta) and path.isdir(rutaAbsoluta)):
            shutil.rmtree(rutaAbsoluta)  # Borrado recursivo
        elif path.isfile(rutaAbsoluta):
            os.remove(rutaAbsoluta)
        ManejoArchivo.eliminarArchivo(rutaAbsoluta, rutaDefault)

    def renombrarCarpeta(rutaAntigua, rutaNueva, rutaDefault):
        if (path.exists(rutaAntigua)):
            os.rename(rutaAntigua, rutaNueva)
            archivo = ManejoArchivo.leerArchivo(rutaDefault, rutaAntigua)
            if archivo:
                archivo.ruta = rutaNueva
                ManejoArchivo.actualizarArchivo(rutaAntigua, archivo, rutaDefault)
                
    def renombrarCarpeta2(rutaAntigua, rutaNueva):
        if (path.exists(rutaAntigua)):
            os.rename(rutaAntigua, rutaNueva)

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
                if(file !="archivos.JSON"):
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
        
    def leerArchivo(ruta, key):
        archivos = ManejoArchivo.leerArchivos(ruta)
        archivo = next((i for i in archivos if i['ruta'] == key), None)
        return Archivo(**archivo) if archivo else None
    
    def deserializarJSONToArchivos(array):
        archivos = []
        for i in array:
            archivo = Archivo(i['ruta'], i['tipoArchivo'], i['listaUsuarios'],i['listaPermisos'])
            archivos.append(archivos)
        return archivos
    
    def actualizarArchivo(ruta, archivo, rutaDefault):
        archivos = ManejoArchivo.leerArchivos(rutaDefault)
        archivos_guardar = []
        for i in archivos:
            if(i['ruta'] == ruta):
                i = archivo.__dict__
            if ruta in i['ruta']:
                i['ruta'] = i['ruta'].replace(ruta,archivo.ruta)
                
            archivos_guardar.append(i)
        ManejoArchivo.guardarArchivos(archivos_guardar,rutaDefault)
        
    def copiarArchivos(destino, origen):
            for element in listdir(destino):
                    ruta = destino+"/"+element
                    if not(path.exists(origen+"/"+element)):
                        if(path.isdir(ruta)):
                            shutil.copytree(ruta, origen+"/"+element)
                        else:
                            shutil.copy(ruta, origen+"/"+element)
    def copiarArchivos2(destino, origen):
        if(path.exists(origen)):
            ruta = origen+"/"+path.basename(destino)
            if(path.exists(ruta)):
                ManejoArchivo.eliminarCarpeta2(ruta)
            if(path.isdir(destino)):
                shutil.copytree(destino, ruta)
            else:
               shutil.copy(destino, ruta)
          
    def moverArchivos(destino, origen):
        for element in listdir(destino):
            ruta = destino+"/"+element
            if not(path.exists(origen+"/"+element)):
                shutil.move(ruta, origen+"/"+element)
                    
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
                if(element !="archivos.JSON"):
                    nombre = element
                    archivo = ruta+"/"+nombre
                    tipoArchivo = ManejoArchivo.obtenerTipoArchivo(archivo)
                    fila = [nombre, tipoArchivo, os.path.relpath(archivo)]
                    item = QTreeWidgetItem(arbol, fila)
                    arbol.insertTopLevelItems(0, [item])
                    ManejoArchivo.listar_carpetas(ruta+"/"+item.text(0), item)
