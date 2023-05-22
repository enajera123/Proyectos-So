from modelo import Mazo
from modelo import Carta
import random

class Partida:
    Arboles = ["Rojo","Verde","Azul","Naranja","Amarillo","Celeste","Marron","Morado","Blanco","Gris",]
    def __init__(self,nombre,clave):
        self.nombre = nombre
        self.clave = clave
        self.jugadores = []
        #Estos 3 les agregue atributo nombre con la idea de darles el nombre del usuario al que pertenecen 
        #Yo pienso que asi son mas faciles de manejar ademas estos pueden ir en el usuario tambien
        #de momento los deje aqui porque pense que era mejor pero se puede ver de cual manera es mas facil de manejar
        self.tableros = [] #Cuando se crea el tablero se le da un nombre el del jugador asi se identifican facil
        self.mazos = [] #Tambien se les da un nombre para idenficarlos mas facil puede ser el del jugador tambien
        self.barajas = [] #Tambien se les da un nombre para idenficarlos mas facil puede ser el del jugador tambien
    
        
        
        
    