class Archivo:
    id = ""
    ruta = ""
    tipoArchivo = ""
    listaUsuarios = []#[esteban],[],[],[],[],[]
    listaPermisos = []#[],[],[],[],[],[]

    def __init__(self, id, ruta, tipoArchivo, listaUsuarios, listaPermisos):
        super(Archivo, self).__init__()
        self.id = id
        self.ruta = ruta 
        self.tipoArchivo = tipoArchivo
        self.listaUsuarios = listaUsuarios
        self.listaPermisos = listaPermisos

   