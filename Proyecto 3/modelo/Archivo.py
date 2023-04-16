from utilidades.ManejoArchivo import ManejoArchivo


class Archivo:
    ruta = ""
    listaUsuarios = []
    listaPermisos = []

    def __init__(self, ruta):
        super(Archivo, self).__init__()
        Archivo.ruta = ruta

   