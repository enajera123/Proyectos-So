from modelo.Mazo import Mazo
from modelo.Carta import Carta
import json
import random

class Partida:
    
    def __init__(self,nombre,clave):
        self.nombre = nombre
        self.clave = clave
        self.jugadores = [] #Se guardan objetos Usuario
        self.iniciado = False
        self.jugadorActual = None #Se guarda objeto Usuario
        self.mazo = Mazo("principal")
        self.arboles = ["blossom cherry", "celestial magnolia", "exotic tree", "giant sequoia", "golden mapple",
               "moonlit willow","quivering aspen", "purple fir", "tree of love", "whispering willow"]
    
    def generarMazo(self, cantidadJugadores):
        """Genera el mazo principal de acuerdo a la cantidad de jugadores"""
        #Se tiene una lista con los colores, revueltos con la funcion shuffle
        random.shuffle(self.arboles)
        #El comando ":" obtiene las primeras n posiciones definidas del arreglo
        self.arboles = self.arboles[:cantidadJugadores*2 + 2]
        cartas = []
        id = 0
        for color in self.arboles:
            for j in range(1, 9):
                cartas.append(Carta(id, color, j))
                id += 1
        #Se vuelve a llamar la funcion para revolver todas las cartas generadas
        random.shuffle(cartas)
        self.mazo.cartas = cartas
        
    def agregarJugador(self,jugador):
        for j in self.jugadores:
            if j.nombre == jugador.nombre:
                return False
        self.jugadores.append(jugador)
        return True
                
    def cambiarJugador(self):
        """Cambia el jugador actual y mueve el anterior al final"""
        self.jugadorActual = self.jugadores.pop(0)
        self.jugadores.append(self.jugadorActual)
        return True
            
    def asignarDerechosApuntuar(self):
        for arbol in self.arboles:
            ganadorTiene1 = False
            ganadorTiene8 = False
            puntosGanador = 0
            ganador = []
            for jugador in self.jugadores:
                gano = False
                empate = False
                puntos = 0
                tiene1 = False
                tiene8 = False
                for carta in jugador.cartas:
                    if carta.arbol == arbol:#Se comprueba si la carta es del tipo de arbol que se evalua
                        puntos += carta.numero
                        if carta.numero == 1:
                            tiene1 = True
                        elif carta.numero == 8:
                            tiene8 = True
                if ganadorTiene1 and tiene8:
                    if puntosGanador < puntos-8:
                        gano = True
                    elif puntosGanador == puntos-8:
                        empate = True
                elif ganadorTiene8 and tiene1:
                    if puntosGanador-8 < puntos:
                        gano = True
                    elif puntosGanador-8 == puntos:
                        empate = True
                elif puntosGanador < puntos:
                    gano = True
                elif puntosGanador == puntos:
                    empate = True
                if gano:
                    ganadorTiene1 = tiene1
                    ganadorTiene8 = tiene8
                    puntosGanador = puntos
                    ganador = [jugador]
                elif empate:
                    ganador.append(jugador)
            if len(ganador) != 0:
                for g in ganador:
                    if arbol not in g.tiposArbolPuntuable:
                        g.tiposArbolPuntuable.append(arbol)
            else:
                for j in self.jugadores:
                    if arbol not in j.tiposArbolPuntuable:
                        j.tiposArbolPuntuable.append(arbol)
        
    