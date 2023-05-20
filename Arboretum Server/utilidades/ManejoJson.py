import os
# Manejo Archivos
import json
# path funciones de rutas
from os import path, listdir

#De momento le di el nombre de manejoJson pero en realidad le puede quedar mejor el de Utilidades y meter aqui cosas varias

class ManejoJson:
    def __init__(self):
        super(ManejoJson, self).__init__()
# =======================
# Control de Json
# =======================
    def guardarDato(dato, ruta):
        datos = ManejoJson.leerDatos()
        datos.append(dato)
        ManejoJson.guardarDatos(datos,ruta)
    def guardarDatos(datos, ruta):
        with open(ruta, 'w') as f:
            json.dump(datos, f)

    def leerDatos(ruta):
        if not os.path.exists(ruta):
            return []
        with open(ruta, 'r') as f:
            return json.load(f)
    










            
    
    