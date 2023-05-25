# Se puede usar tanto para el mazo principal como para los de descartes
# Para el mazo principal las cartas se pueden generar en el objeto paratida y luego se ingresan
# Pienso que tambien se puede usar para la baraja si se le hacen algunos metodos especificamente para eso
import random
from modelo.Carta import Carta


class Mazo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.cartas = []

    def popCarta(self):
        '''Elimina la ultima carta ingresada'''
        if (len(self.cartas) != 0):
            return self.cartas.pop()
        else:
            return None

