class Registro:
    #tipo = ""
    #rutaPrimaria = ""
    #rutaSecundaria = ""
    def __init__(self, tipo, rutaPrimaria, rutaSecundaria=None):
        """
        tipo: Mover,Renombrar,Eliminar,Crear
        rutaPrimaria: Guarda la ruta original se usa en Eliminar, Crear
        rutaSecundaria: Guarda la ruta modificada se usa en Mover, Renombrar
        """
        self.tipo = tipo
        self.rutaPrimaria = rutaPrimaria
        self.rutaSecundaria = rutaSecundaria
    def getTipo(self):
        return self.tipo
    def getRutaPrimaria(self):
        return self.RutaPrimaria
    def getRutaSecundaria(self):
        return self.rutaSecundaria