import os
# Manejo Archivos
import json
# path funciones de rutas
from os import path, listdir

class Utilidades:
    def __init__(self):
        super(Utilidades, self).__init__()
# =======================
# Control de Json
# =======================
    def guardarDato(dato, ruta):
        datos = Utilidades.leerDatos()
        datos.append(dato)
        Utilidades.guardarDatos(datos,ruta)
        
    def guardarDatos(datos, ruta):
        with open(ruta, 'w') as f:
            json.dump(datos, f)

    def leerDatos(ruta):
        if not os.path.exists(ruta):
            return []
        with open(ruta, 'r') as f:
            return json.load(f)
    










            
    
    