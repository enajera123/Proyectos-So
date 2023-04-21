class Usuario:
    def __init__(self, id, nombre, clave):
        self.id = id
        self.nombre = nombre
        self.clave = clave
        
    def to_dict(self):
        return {'id': self.id, 'nombre': self.nombre, 'correo': self.correo}
    