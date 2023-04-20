from utilidades.ComboBoxUtilidades import ComboBoxUtilidades
from utilidades.RadioButonUtilidades import RadioButonUtilidades
from utilidades.ArbolUtilidades import ArbolUtilidades
from utilidades.Alerta import Alerta
class Generalidades:
    def __init__(self):
        super(Generalidades, self).__init__()
    def agregarUsuario(*args):
        """Agrega usuario a un QTreeWidget
        arg0 = ComboBox con nombre de usuario
        arg1 = radioButon Lectura
        arg2 = radioButon Escritura
        arg3 = radioButon Ejecucion
        arg4 = QtreeWidget 
        """
        item = ComboBoxUtilidades.obtenerValorComboBox(args[0])
        permisos = RadioButonUtilidades.leerRadioButons(args[1],args[2],args[3])
        i = ArbolUtilidades.buscarItem(args[4], item,0) 
        if  i == None :
            ArbolUtilidades.agregarItem(args[4], [item, permisos])
            RadioButonUtilidades.reiniciarRadioButons(args[1],args[2],args[3])
        else:
            Alerta("Ya existe el usuario dentro de los permisos", "error").mostrarAlerta()