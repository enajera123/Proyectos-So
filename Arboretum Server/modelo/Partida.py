from modelo.Mazo import Mazo
from modelo.Carta import Carta
import json
import random

class Partida:
    def __init__(self,nombre,clave):
        self.arboles = ["blossom cherry", "celestial magnolia", "exotic tree", "giant sequoia","golden mapple",
                    "moonlit willow","quivering aspen", "purple fir", "tree of love", "whispering willow"]
        self.nombre = nombre
        self.clave = clave
        self.jugadores = [] #Se guardan objetos Usuario
        self.iniciado = False
        self.jugadorActual = None #Se guarda objeto Usuario
        self.mazo = Mazo("principal")

    def generarMazo(self, cantidadJugadores):
        """Genera el mazo principal de acuerdo a la cantidad de jugadores"""
        #Se tiene una lista con los Arboles, revueltos con la funcion shuffle
        random.shuffle(self.arboles)
        #El comando ":" obtiene las primeras n posiciones definidas del arreglo
        self.arboles = self.arboles[:cantidadJugadores*2 + 2]
        cartas = []
        id = 0
        for arbol in self.arboles:
            for j in range(1, 9):
                cartas.append(Carta(id, arbol, j))
                id += 1
        #Se vuelve a llamar la funcion para revolver todas las cartas generadas
        random.shuffle(cartas)
        self.mazo.cartas = cartas
        
    def asignarDerechosApuntuar(self):
        barajas = []
        #Se obtinen las barajas de los jugadores
        for jugador in self.jugadores:
            mazo = Mazo(jugador.nombre)
            mazo.cartas = jugador.cartas
            barajas.append(mazo)
            
        #Se calculan derechos de arboles
        for arbol in self.arboles:#Se recorren los tipos de arboles
            ganadorTiene1 = False
            ganadorTiene8 = False
            puntosGanador = 0
            ganador = ""
            for baraja in barajas:#Se recorren las barajas
                puntos = 0
                tiene1 = False
                tiene8 = False
                for carta in baraja.cartas:#Se recorren las cartas de la baraja
                    if carta.arbol == arbol:#Se comprueba si la carta es del tipo de arbol que se evalua
                        puntos += carta.numero
                        if carta.numero == 1:
                            tiene1 = True
                        elif carta.numero == 8:
                            tiene8 = True
                #Se compara con el ganador
                if ganadorTiene1 and tiene8: #Si ganador tiene 1 y en la baraja actual hay 8
                    if puntosGanador < puntos-8: #Se evalua restandole 8 puntos a la baraja actual ya que se anula el 8
                        ganador = baraja.nombre #La baraja tiene el nobre del jugador al que pertenece
                        ganadorTiene1 = tiene1
                        ganadorTiene8 = tiene8
                elif ganadorTiene8 and tiene1: #La inversa del caso anterior
                    if puntosGanador-8 < puntos:
                        ganador = baraja.nombre
                        ganadorTiene1 = tiene1
                        ganadorTiene8 = tiene8
                elif puntosGanador < puntos: #No se modifican los puntages
                    ganador = baraja.nombre
                    ganadorTiene1 = tiene1
                    ganadorTiene8 = tiene8
            if len(ganador) != 0:#Si alguien gano
                for jugador in self.jugadores: #Se busca al ganador y se le agrega el arbol que gano
                    if jugador.nombre == ganador:
                        jugador.arbolesPuntuables.append(arbol)
            else:#Sino 
                for jugador in self.jugadores: #Se les dan derechos a todos
                    jugador.arbolesPuntuables.append(arbol)
      
        
        
    