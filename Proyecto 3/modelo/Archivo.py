from utilidades.ManejoArchivo import ManejoArchivo


class Archivo:
    ruta = ""
    tipoArchivo = ""
    listaUsuarios = []#[esteban],[],[],[],[],[]
    listaPermisos = []#[],[],[],[],[],[]

    def __init__(self, ruta, tipoArchivo):
        super(Archivo, self).__init__()
        self.ruta = ruta 
        self.tipoArchivo = tipoArchivo

   