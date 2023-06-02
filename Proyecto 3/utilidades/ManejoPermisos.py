from utilidades.Data import Data
from datetime import datetime
from utilidades.ManejoArchivo import ManejoArchivo
from os import listdir, path
from modelo.Archivo import Archivo
from utilidades.Alerta import Alerta
class ManejoPermisos:
    
    def __init__(self):
        super(ManejoPermisos, self).__init__()
        
    def commit():
        archivos = ManejoArchivo.deserializarJSONToArchivos(ManejoArchivo.leerArchivos(Data.rutaArchivos))#Se obtienen lo archivos
        for archivo in archivos:
            ManejoPermisos.comitLocal(archivo)
            
        archivos = ManejoPermisos.filtrado(archivos)
        #ManejoPermisos.filtrar_archivos_con_permisos_de_escritura(archivos)
        for archivo in archivos:
            #if ManejoPermisos.verificaPermiso(archivo,"[Escritura]"):
                    for i in range(len(archivo.listaUsuarios)):#Se recorren los usuarios que tienen permisos
                        if Data.nombre != archivo.listaUsuarios[i]:
                            ManejoPermisos.comitGeneral(archivo, i)#Se hacen comits generales a cada usuario        
            #else:
             #   ManejoPermisos.comitLocal(archivo)#Se hace un comit local al usuario            
    def filtrado(archivos):
        archivosSinPermisos = []
        for archivo in archivos:
            if not ManejoPermisos.verificaPermiso(archivo, "[Escritura]"):
                archivosSinPermisos.append(archivo)
                archivosSinPermisos.extend(ManejoPermisos.obtenerArchivos(ManejoArchivo.obtenerDirecciones(archivo.ruta)))
        rutas = set(map(lambda x: x.ruta, archivosSinPermisos))
        archivos[:] = [a for a in archivos if a.ruta not in rutas]
        return archivos
            
    def obtenerArchivos(rutas):
        archivos = []
        for ruta in rutas:
            archivo = ManejoArchivo.leerArchivo(Data.rutaArchivos, "ruta", ruta)
            if archivo:
                archivos.append(archivo)
        return archivos
    def comitLocal(archivo):
        rutaArchivosEnRaiz = "bin/"+Data.nombre+"/raiz/archivos.JSON"#Ruta del JSON en la carpeta raiz
        archivoExistente = ManejoArchivo.leerArchivo(rutaArchivosEnRaiz, "id", archivo.id)
        if archivoExistente:#Si existe se borra con el fin de sobreescribir
            ManejoPermisos.eliminarArchivoDeRaiz(rutaArchivosEnRaiz, archivoExistente)
        ManejoPermisos.crearArchivoEnRaiz(rutaArchivosEnRaiz, archivo, archivo.ruta)
        
    def comitGeneral(archivo, indiceUsuario):
        rutaUsuario = "bin/" + archivo.listaUsuarios[indiceUsuario] + "/temporal"#Ruta temporal de cada usuario
        rutaArchivosRaiz = "bin/" + archivo.listaUsuarios[indiceUsuario] + "/raiz/archivos.JSON"#Se obtiene la ruta del JSON en Raiz
        archivoExistente = ManejoArchivo.leerArchivo(rutaArchivosRaiz, "id", archivo.id)#Se verifica si ya existe el archivo en raiz
        if "[Lectura]" in archivo.listaPermisos[indiceUsuario]:#Todos los archivos manejan la ruta en temporal sin importar donde esten
            array = archivo.ruta.split("temporal")#Se modifica la ruta del archivo para acceder a su igual 
            array[0] = rutaUsuario#en los diferentes usuarios
            ruta = array[0] + array[1]    
            if archivoExistente:
                ManejoPermisos.eliminarArchivoDeRaiz(rutaArchivosRaiz, archivoExistente)
            nuevoArchivo = Archivo(archivo.id, ruta, archivo.tipoArchivo, archivo.listaUsuarios, archivo.listaPermisos)
            ManejoPermisos.crearArchivoEnRaiz(rutaArchivosRaiz, nuevoArchivo, archivo.ruta)
        elif archivoExistente:   
            ManejoPermisos.eliminarArchivoDeRaiz(rutaArchivosRaiz, archivoExistente)
        
    def verificaPermiso(archivo, permiso):
        """Verifica si el usuario tiene permisos de escritura
        """
        nombreUsuario = Data.nombre
        indice = archivo.listaUsuarios.index(nombreUsuario)
        permisos = archivo.listaPermisos[indice]
        if permiso in permisos:
            return True
        return False
    
        
        
    def eliminarArchivoDeRaiz(rutaArchivos, archivo):
        ManejoArchivo.eliminarArchivo(rutaArchivos, archivo)
        rutaFisica = archivo.ruta.replace("temporal","raiz")#Se obtiene la ruta fisica de la carpeta eliminada
        ManejoArchivo.eliminarCarpeta(rutaFisica)
        
    def crearArchivoEnRaiz(rutaArchivos, archivo, rutaAntigua):
        rutaFisica = archivo.ruta.replace("temporal","raiz")#Se obtiene la ruta fisica de la carpeta eliminada
        rutaAlternativa = ""#En caso de que exista una carpeta con ese nombre se debe cambiar la ruta
        if path.isdir(rutaAntigua):
            rutaAlternativa = ManejoArchivo.copiarCarpeta(rutaAntigua, rutaFisica)#Se crea un duplicado
        else:
            rutaAlternativa = ManejoArchivo.copiarArchivo2(rutaAntigua, rutaFisica)
        rutaAntigua = rutaFisica.replace("raiz","temporal")#Se obtiene la ruta antigua
        if not rutaAlternativa == rutaAntigua:#En caso de que se haya cambiado la ruta
            arch = ManejoArchivo.leerArchivo(rutaArchivos, "ruta", rutaAntigua)#Se debe leer el archivo para actualizar la ruta
            if arch:
                arch.ruta = rutaAlternativa
                ManejoArchivo.actualizar(rutaAntigua, arch, rutaArchivos)
        ManejoArchivo.crearArchivo(archivo, rutaArchivos)#Se ingresa el archivo al JSON
            
    def recuperarVersionCompleta(ruta):
        ManejoArchivo.eliminarCarpeta(Data.rutaPrincipal)
        ManejoArchivo.crearCarpeta_Archivo(Data.rutaPrincipal)
        ManejoArchivo.copiarContenidoCarpeta(ruta, Data.rutaPrincipal)
        return True
        
    def recuperarArchivo(ruta):
        """Recupera un archivo sin correr recursivamente, todos los recuperar usan los JSON
        """
        direcciones = [ruta]
        direcciones.extend(ManejoArchivo.obtenerDirecciones(ruta))#Se obtienen las rutas y sub-rutas
        exito = False
        archivos = ManejoPermisos.obtenerArchivos(direcciones)
        ManejoPermisos.modificarRuta(archivos[0].ruta, ManejoPermisos.definirRutaEnPrimerNivel(archivos[0].ruta), archivos)
        for i, direccion in enumerate(direcciones):#Recuperacion de cada ruta contenida
            #data = ManejoArchivo.leerArchivo(Data.rutaVersionRecuperar+"archivos.JSON", "ruta", ManejoPermisos.tratarRuta(direccion))
            #if data:
            if ManejoPermisos.ingresarInformacionJSON(Data.rutaArchivos, archivos[i]):#Se ingresa la informacion leida al JSON
                ManejoArchivo.sobreescribirArchivo(direccion, archivos[i].ruta)#Borra y elimina fisicamente
                exito = True
        return exito
    
    def modificarRuta(direccionAModificar, direccionNueva, archivos):
        for archivo in archivos:
            archivo.ruta = archivo.ruta.replace(direccionAModificar,direccionNueva)
            
    def obtenerArchivos(direcciones):
        archivos = []
        for direccion in direcciones:
            data = ManejoArchivo.leerArchivo(Data.rutaVersionRecuperar+"archivos.JSON", "ruta", ManejoPermisos.tratarRuta(direccion))
            if data:
                archivos.append(data)
        return archivos
                
           
        
    def ingresarInformacionJSON(JSONDestino, data):
        """Ingresa la informacion al JSON unicamente funciona para JSON con formato de clase Archivo
        Args:
            JSONDestino (_type_): Ruta del archivo.JSON
            data (_type_): Objeto a ingresar
        """
        archivo = ManejoArchivo.leerArchivo(JSONDestino, "id", data.id)
        
        if archivo:
            ManejoArchivo.eliminar(archivo.ruta, JSONDestino)
            #ManejoArchivo.eliminarArchivo(JSONDestino, archivo)
      
        elif not  path.exists(data.ruta):
            rutaNueva = ManejoPermisos.definirRutaEnPrimerNivel(data.ruta)
            if not path.exists(rutaNueva):
                data.ruta = rutaNueva
                data.id = ManejoArchivo.obtenerId()
            else:
                Alerta("Ya existe un archivo con ese nombre, por favor cambiar el nombre al archivo para poder recuperarlo", "error").mostrarAlerta()
                return False
            
        ManejoArchivo.crearArchivo(data, JSONDestino)
        return True
        
    def definirRutaEnPrimerNivel(ruta):
        rutaNueva = "bin/"+Data.nombre+"/temporal/"+path.basename(ruta)
        #if path.isfile(rutaNueva):
         #   rutaDuplicada = ManejoArchivo.duplicadoArchivo(rutaNueva)
        #else:
         #   rutaDuplicada = ManejoArchivo.duplicadoCarpeta(rutaNueva)
        return rutaNueva
    
    def crearVersion():
        nombre = Data.nombre+"("+datetime.now().strftime("%Y-%m-%d %H-%M-%S")+")"
        rutaVersion = "bin/"+Data.nombre+"/versiones"+"/"+nombre
        if(len(listdir(Data.rutaPermanente))>1):
            ManejoArchivo.crearCarpeta_Archivo(rutaVersion)
            ManejoArchivo.moverArchivos(Data.rutaPermanente, rutaVersion)
            
    def tratarRuta(ruta):
        """Ya que los archivos tienen el siguiente formato
        bin/{usuario}/versiones/{version}/...
        Se necesita buscar su similar en temporal para la recuperacion en JSON
        para eso se trata la ruta para que quede en formato
        /bin/{usuario}/temporal/...
        """
        array = ruta.split("/")
        array[2] = "temporal"#Se sustituye "versiones" por "temporal"
        array.pop(3)#Se elimina el nombre de la version
        rutaNueva = ""
        for i in array:
            rutaNueva += i + "/"
        rutaNueva = rutaNueva.rstrip("/")#Se le elimina el ultimo "/"
        return rutaNueva
            
         
    # =======================