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

   
