class Archivo:
    ruta = ""
    tipoArchivo = ""
    listaUsuarios = []#[esteban],[],[],[],[],[]
    listaPermisos = []#[],[],[],[],[],[]

    def __init__(self, ruta, tipoArchivo, listaUsuarios, listaPermisos):
        super(Archivo, self).__init__()
        self.ruta = ruta 
        self.tipoArchivo = tipoArchivo
        self.listaUsuarios = listaUsuarios
        self.listaPermisos = listaPermisos

   