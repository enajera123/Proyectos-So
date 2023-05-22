import os
# Manejo Archivos
import json
# path funciones de rutas
from modelo.Jugador import Jugador
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
    def limpiarDatos(ruta):
        with open(ruta, 'r') as f:
            json.dump({}, f)
            
    def deserializarJugador(jugador):
        jugador_dict = json.loads(jugador)
        jugador = Jugador(jugador_dict['nombre'])
        jugador.cartas = jugador_dict['cartas']
        return jugador










            
    
    