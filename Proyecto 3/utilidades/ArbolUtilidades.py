from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QTreeWidgetItem
from utilidades.ManejoArchivo import ManejoArchivo
from os import path, listdir

class ArbolUtilidades:
    def __init__(self):
        super(ArbolUtilidades, self).__init__()
        
    def listar_carpetas(ruta, parent):
        """
        Args:
            path (string): Ruta Absoluta
            parent (QTreeWidgetItem): item del tree
        """
        # Verificar si la ruta es un directorio
        if path.isdir(ruta):
            # Obtener una lista de todos los archivos y carpetas en el directorio
            files = listdir(ruta)
            # Recorrer todos los archivos y carpetas
            for file in files:
                if(file !="archivos.JSON"):
                    # Obtener la ruta completa del archivo o carpeta
                    full_path = path.join(ruta, file)
                    # Si es una carpeta, agregarla al árbol
                    if path.isdir(full_path):
                        item = QTreeWidgetItem(parent)
                        ArbolUtilidades.bindQTreeWidgetItem(item, file, "Carpeta", path.relpath(full_path))
                        # Listar todas las subcarpetas recursivamente
                        ArbolUtilidades.listar_carpetas(full_path, item)
                    # Si es un archivo, agregarlo al árbol
                    elif path.isfile(full_path):
                        archivo = QTreeWidgetItem(parent)
                        tipoArchivo = ManejoArchivo.obtenerTipoArchivo(full_path)
                        ArbolUtilidades.bindQTreeWidgetItem(archivo, file, tipoArchivo, path.relpath(full_path))
                        
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
                    fila = [nombre, tipoArchivo, path.relpath(archivo)]
                    item = QTreeWidgetItem(arbol, fila)
                    arbol.insertTopLevelItems(0, [item])
                    ArbolUtilidades.listar_carpetas(ruta+"/"+item.text(0), item)

    def obtenerItemSeleccionado(arbol, opcion):
        """
            opcion (int): 
            -1:retorna el item
            0:nombre
            2:ruta
        """
        selected_item = arbol.selectedItems()  # Obtiene la linea seleccionada
        if opcion == -1:
            return selected_item
        if len(selected_item) > 0:
            return ManejoArchivo.obtenerRutaCarpeta(selected_item[0].text(opcion))
        return ""     
    def desplegarItem(item,opcion):
        for i in item:
            i.setExpanded(opcion)
            
    def buscarItem(tree, text, llaveBusqueda):
        """Busca un item en el QTreeWidget por su llave"""
        items = tree.findItems(text, Qt.MatchRecursive, llaveBusqueda)
        if items:
            return items[0]
        return None
        
    def obtenerDatosColumna(arbol,key):
        valores = []
        for i in range(arbol.topLevelItemCount()):
            item = arbol.topLevelItem(i)
            valores.append(item.text(key))
        return valores
    
    def colapsarItem(tree, items):
        tree.setCurrentItem(items[0])
        
    def agregarItem(arbol, datos):
        item = QTreeWidgetItem(arbol, datos)
        arbol.addTopLevelItem(item)
        
    def eliminarItem(arbol, items):
        for item in items: 
            arbol.takeTopLevelItem(arbol.indexOfTopLevelItem(item))
            
    def modificarItem(cadena,item,key):
        cadena = cadena.replace("[None]","")
        if(cadena!=""):
            item.setText(key,cadena)
        else:
            item.setText(key,"[None]")
    