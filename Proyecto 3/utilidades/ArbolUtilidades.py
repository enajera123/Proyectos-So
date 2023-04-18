from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QTreeWidgetItem
from utilidades.ManejoArchivo import ManejoArchivo
class ArbolUtilidades:
    def __init__(self):
        super(Data, self).__init__()
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
            
    def buscarItem(tree, text):
        """Busca un item en el QTreeWidget por su primera columna"""
        items = tree.findItems(text, Qt.MatchRecursive, 2)
        if items:
            tree.setCurrentItem(items[0])
    def agregarItem(arbol, datos):
        item = QTreeWidgetItem(arbol, datos)
        arbol.addTopLevelItem(item)
        
    def eliminarItem(arbol, items):
        for item in items: 
            arbol.takeTopLevelItem(arbol.indexOfTopLevelItem(item))
