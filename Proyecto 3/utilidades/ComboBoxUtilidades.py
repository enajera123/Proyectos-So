class ComboBoxUtilidades:
    def __init__(self):
        super(ComboBoxUtilidades, self).__init__()
        
    def obtenerValorComboBox(comboBox):
        indice = comboBox.currentIndex()
        valor = comboBox.itemText(indice)
        return valor
    def llenarComboBox(comboBox,usuarios):
        for usuario in usuarios:
            comboBox.addItem(usuario.nombre)
        