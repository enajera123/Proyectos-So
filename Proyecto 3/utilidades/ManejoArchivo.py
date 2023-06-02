import sys
import time
import os
# Manejo Archivos
import shutil
import pickle
import json
import subprocess
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
    rutaIds = "bin/ids.JSON"

    def __init__(self):
        super(ManejoArchivo, self).__init__()
    # =======================
    # Manejo Carpetas
    # =======================
    def crearCarpeta_Archivo(ruta):
        from modelo.Archivo import Archivo
        if "." in ruta:
            open(ruta, "w")
        else:
            os.mkdir(ruta)#creacion de carpetas    
        
    def crear(rutaArchivo, rutaDefault, *args):
        """Crea un archivo o carpeta y tambien su objeto en el JSON para el manejo

        Args:
            rutaArchivo (_type_): Ruta del archivo a crear
            rutaDefault (_type_): Ruta del JSON
        """
        from modelo.Archivo import Archivo
        if (path.isdir(path.dirname(rutaArchivo))):    
            if "." in rutaArchivo:#Creacion de archivos
                rutaArchivo = ManejoArchivo.duplicadoArchivo(rutaArchivo)
                open(rutaArchivo,"w")
            else:
                rutaArchivo = ManejoArchivo.duplicadoCarpeta(rutaArchivo)
                os.mkdir(rutaArchivo)#creacion de carpetas
            tipoArchivo = ManejoArchivo.obtenerTipoArchivo(rutaArchivo)
            id = ManejoArchivo.obtenerId()
            if(len(args)>=2):
                archivo = Archivo(id, rutaArchivo, tipoArchivo,args[0],args[1])
            else:
                archivo = Archivo(id, rutaArchivo, tipoArchivo,[],[])
                
            ManejoArchivo.crearArchivo(archivo, rutaDefault)#Crea archivo
          
    def obtenerId():
        array = ManejoArchivo.leerIds()
        ids = [d["id"]for d in array]
        newId = max(ids)+1 if ids else 1
        array.append({"id": newId})
        ManejoArchivo.guardarId(array)
        return newId
        
        
    def leerIds():
        if not os.path.exists(ManejoArchivo.rutaIds):
            return []
        with open(ManejoArchivo.rutaIds, 'r') as f:
            return json.load(f)
        
    def guardarId(ids):
        with open(ManejoArchivo.rutaIds, 'w') as f:
            json.dump(ids, f)
            
    def eliminarId(id):
        ids = ManejoArchivo.leerIds() 
        newIds = []
        for i in ids:
            if not i["id"] == id:
                newIds.append(i)
        ManejoArchivo.guardarId(newIds)
        
    def eliminarCarpeta(ruta):
        if(path.exists(ruta) ):
            if path.isdir(ruta):
                shutil.rmtree(ruta)
            if path.isfile(ruta):
                os.remove(ruta)
        
            
    def eliminar(rutaAbsoluta, rutaDefault):
        """Elimina tanto fisico como del JSON
        """
        if (path.exists(rutaAbsoluta)):
            archivo = ManejoArchivo.leerArchivo(rutaDefault, "ruta", rutaAbsoluta)
            if archivo:
                ManejoArchivo.eliminarArchivo(rutaDefault, archivo)
            if(path.isdir(rutaAbsoluta)):
                shutil.rmtree(rutaAbsoluta)  # Borrado recursivo
            elif path.isfile(rutaAbsoluta):
                os.remove(rutaAbsoluta)
            

    def renombrarCarpeta(rutaAntigua, rutaNueva):
        if (path.exists(rutaAntigua)):
            os.rename(rutaAntigua, rutaNueva)   
    
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
        
    def leerArchivo(ruta, key, value):
        archivos = ManejoArchivo.leerArchivos(ruta)
        archivo = next((i for i in archivos if i[key] == value), None)
        return Archivo(**archivo) if archivo else None
    
    

    
    def deserializarJSONToArchivos(array):
        
        archivos = []
        for i in array:
            archivo = Archivo(i['id'], i['ruta'], i['tipoArchivo'], i['listaUsuarios'],i['listaPermisos'])
            archivos.append(archivo)
        return archivos
    
    
    def actualizar(ruta, archivo, rutaDefault):
        """Actualiza un archivo del JSON, no renombra fisicamente

        Args:
            ruta (_type_): Ruta a modificar
            archivo (_type_): Archivo objeto
            rutaDefault (_type_): Ruta de los archivos JSON
        """
        archivos = ManejoArchivo.leerArchivos(rutaDefault)
        archivos_guardar = []
        for i in archivos:
            if(i['id'] == archivo.id):
                i = archivo.__dict__
            archivos_guardar.append(i)

        ManejoArchivo.guardarArchivos(archivos_guardar,rutaDefault)
        ManejoArchivo.actualizarHijos(ruta, archivo, rutaDefault)#Se deben actualizar las rutas de 
        #los hijos para mantener la sincronizacion
        
    def actualizarHijos(ruta, archivo, rutaDefault):
        direccionesHijas = ManejoArchivo.obtenerDirecciones(ruta)
        hijos = []
        for direccion in direccionesHijas:
            archivoHijo = ManejoArchivo.leerArchivo(rutaDefault, "ruta", direccion)
            archivoHijo.ruta = archivoHijo.ruta.replace(ruta, archivo.ruta)
            hijos.append(archivoHijo)
        archivos = ManejoArchivo.leerArchivos(rutaDefault)
        archivosGuardar = []
        for i in archivos:
            for hijo in hijos:
                if hijo.id == i['id']:
                    i = hijo.__dict__
                    break
            archivosGuardar.append(i)
        ManejoArchivo.guardarArchivos(archivosGuardar, rutaDefault)
            
    def copiarContenidoCarpeta(destino, origen):
        """Copia el contenido de la carpeta
        """
        for element in listdir(destino):
            ruta = destino+"/"+element
            if not(path.exists(origen+"/"+element)):
                if(path.isdir(ruta)):
                    shutil.copytree(ruta, origen+"/"+element)
                else:
                    shutil.copy(ruta, origen+"/"+element)
                    
    def copiarArchivo2(destino, origen):
        """Copia el archivo, si existe alguno con esa ruta lo mueve a un duplicado
        """
        rutaAlternativa = origen
        if(path.isdir(path.dirname(origen))):
            if(path.exists(origen)):
                rutaAlternativa = ManejoArchivo.duplicadoArchivo(origen)
                shutil.copy(origen, rutaAlternativa)
                os.remove(origen)
            shutil.copy(destino, origen)
        return rutaAlternativa.replace("raiz", "temporal")
            
    def sobreescribirArchivo(destino, origen):
        if path.exists(origen):
            if path.isfile(origen):
                os.remove(origen)
                shutil.copy(destino, origen)
            else:
                shutil.rmtree(origen)
                shutil.copytree(destino, origen)
        else:
            if path.isfile(destino):
                shutil.copy(destino, origen)
            else:
                 shutil.copytree(destino, origen)
            
                
    def copiarArchivo(destino, origen):
        """Copia la carpeta o el archivo
        """
        if(path.exists(origen)):
            ruta = origen+"/"+path.basename(destino)
            
            if(path.isdir(ruta)):
                ruta = ManejoArchivo.duplicadoCarpeta(ruta)
            elif (path.isfile(ruta)):
                ruta = ManejoArchivo.duplicadoArchivo(ruta)
            if(path.isdir(destino)):
                shutil.copytree(destino, ruta)
            else:
               shutil.copy(destino, ruta)
            
    def copiarCarpeta(destino, origen):
        """Copia una carpeta desde el origen al destino completamente vacia
        """
        rutaAlternativa = origen
        if(path.isdir(path.dirname(origen))):
            if path.isdir(destino):
                if(path.exists(origen)):
                    rutaAlternativa = ManejoArchivo.duplicadoCarpeta(origen)#Crea un duplicado
                    shutil.copytree(origen, rutaAlternativa)#Copia la existente al duplicado
                    shutil.rmtree(origen)#Para dejar libre la ruta
                shutil.copytree(destino, origen)#Se copia la que se necesita
                ManejoArchivo.vaciarCarpeta(origen)#Se vacia la carpeta
               # for archivo in listdir(origen):
                #    ruta = path.join(origen, archivo)
                 #   if(path.isdir(ruta)):
                  #      shutil.rmtree(ruta)
                   # else:
                    #    os.remove(ruta)
        return rutaAlternativa.replace("raiz", "temporal")
    
    def vaciarCarpeta(origen):
        for archivo in listdir(origen):
            ruta = path.join(origen, archivo)
            if(path.isdir(ruta)):
                shutil.rmtree(ruta)
            else:
                os.remove(ruta)
        
    def duplicadoCarpeta(ruta):
        cont = 1;
        rutaNueva = ruta
        while(path.exists(rutaNueva)):
            rutaNueva = ruta+"("+cont.__str__()+")"
            cont+=1
        return rutaNueva
    
    def duplicadoArchivo(ruta):
        cont = 1;
        array = ruta.split(".")
        rutaNueva = array[0]
        extension = "."+array[1]
        while(path.exists(rutaNueva+extension)):
            rutaNueva = array[0]+"("+cont.__str__()+")"
            cont+=1 
        return rutaNueva+extension
        
    def moverArchivos(destino, origen):
        for element in listdir(destino):
            ruta = destino+"/"+element
            if not(path.exists(origen+"/"+element)):
                shutil.move(ruta, origen+"/"+element)
                
    def crearArchivo(archivo, ruta):
        archivos = ManejoArchivo.leerArchivos(ruta)
        archivos.append(archivo.__dict__)
        ManejoArchivo.guardarArchivos(archivos, ruta)

    def eliminarArchivo(ruta, archivo):
        archivos = ManejoArchivo.leerArchivos(ruta)
        iterator = []
        for i in archivos:#Borrado iterativo en el JSON
            if not(archivo.id == i['id']):#Si no esta contenido
                iterator.append(i)#Se agrega
        ManejoArchivo.guardarArchivos(iterator, ruta)#Se guarda el arreglo
        if path.isdir(archivo.ruta):
            ManejoArchivo.eliminarHijos(ruta, archivo)
        
    def eliminarHijos(ruta, archivo):
        direccionesHijos = ManejoArchivo.obtenerDirecciones(archivo.ruta)
        archivos = ManejoArchivo.leerArchivos(ruta)
        hijos = []
        for direccionHija in direccionesHijos:
            archivoHijo = ManejoArchivo.leerArchivo(ruta, "ruta", direccionHija)    
            if archivoHijo:
                hijos.append(archivoHijo)
        archivosNuevos = []
        
        for arch in archivos:
            estaContenido = False
            for hijo in hijos:
                if hijo.id == arch['id']:
                    estaContenido = True
                    break
            if not estaContenido:
                 archivosNuevos.append(arch)
        ManejoArchivo.guardarArchivos(archivosNuevos, ruta)
        
        
    def abrirArchivo(ruta):
        if(path.isfile(ruta)):
            subprocess.run(["open",ruta])
            
    #=======================
    #		Utilidades
    #=======================


    def obtenerDirecciones(ruta):
        paths = []
        for root, dirs, files in os.walk(ruta):
            for file in files:
                file_path = os.path.join(root, file)
                paths.append(file_path)
            for dir in dirs:
                dir_path = os.path.join(root, dir)
                paths.append(dir_path)
        return paths

    def obtenerRutaCarpeta(nombreCarpeta):
        return path.relpath(nombreCarpeta)
    
    def obtenerTipoArchivo(ruta):
        if (path.isdir(ruta)):
            tipoArchivo = "Carpeta"
        else:
            mime = MimeTypes()
            tipoArchivo = mime.guess_type(ruta)[0]
        return tipoArchivo
    
    