from modelo.Mazo import Mazo
from modelo.Carta import Carta
import json
import random

class Partida:
   # Arboles = ["Rojo","Verde","Azul","Naranja","Amarillo","Celeste","Marron","Morado","Blanco","Gris",]
    def __init__(self,nombre,clave):
        self.nombre = nombre
        self.clave = clave
        self.jugadores = [] #Se guardan objetos Usuario
        self.iniciado = False
    #   self.jugadorActual = None #Se guarda objeto Usuario
        self.mazo = Mazo("principal")
        
    def agregarJugador(self,jugador):
        self.jugadores.append(jugador)
                
    def cartaJugada(self,carta):
        #Se asume que ya se filtro y solo se juega cuando es el jugador actual
        self.jugadorActual.cartaJugada(carta)
        
    def cartaDescartar(self,carta):
        #Se asume que ya se filtro y solo se juega cuando es el jugador actual
        self.jugadorActual.cartaDescartar(carta)
        
    def mazoTop(self):
        '''Obtiene la ultima carta del mazo'''
        return self.mazo.topCarta()
    
    def mazoPop(self):
        '''Elimina la ultima carta del mazo'''
        return self.mazo.PopCarta()
    
    def cartaDescartadaTop(self,jugador):
        '''Obtiene la ultima carta del mazo de descartes de jugador'''
        for j in self.jugadores:
            if j.getNombre() == jugador.getNombre():
                return j.cartaDescartadaTop()
        return None
    
    def cartaDescartadaPop(self,jugador):
        '''Elimina la ultima carta del mazo de descartes de jugador'''
        for j in self.jugadores:
            if j.getNombre() == jugador.getNombre():
                j.cartaDescartadaPop()
                
    def cambiarJugadorActual(self,jugador):
        for j in self.jugadores:
            if j.getNombre() == jugador.getNombre():
                self.jugadorActual = j
                
    def asignarDerechosApuntuar(self):
        barajas = []
        #Se obtinen las barajas de los jugadores
        for jugador in self.jugadores:
            barajas.append(jugador.getBaraja())
        #Se calculan derechos de arboles
        for arbol in self.Arboles:#Se recorren los tipos de arboles
            ganadorTiene1 = False
            ganadorTiene8 = False
            puntosGanador = 0
            ganador = ""
            for baraja in barajas:#Se recorren las barajas
                cartas = baraja.getCartas()
                puntos = 0
                tiene1 = False
                tiene8 = False
                for carta in cartas:#Se recorren las cartas de la baraja
                    if carta.obtenerArbol() == arbol:#Se comprueba si la carta es del tipo de arbol que se evalua
                        puntos += carta.obtenerNumero()
                        if carta.obtenerNumero() == 1:
                            tiene1 = True
                        elif carta.obtenerNumero() == 8:
                            tiene8 = True
                #Se compara con el ganador
                if ganadorTiene1 and tiene8: #Si ganador tiene 1 y en la baraja actual hay 8
                    if puntosGanador < puntos-8: #Se evalua restandole 8 puntos a la baraja actual ya que se anula el 8
                        ganador = baraja.getNombre() #La baraja tiene el nobre del jugador al que pertenece
                        ganadorTiene1 = tiene1
                        ganadorTiene8 = tiene8
                elif ganadorTiene8 and tiene1: #La inversa del caso anterior
                    if puntosGanador-8 < puntos:
                        ganador = baraja.getNombre()
                        ganadorTiene1 = tiene1
                        ganadorTiene8 = tiene8
                elif puntosGanador < puntos: #No se modifican los puntages
                    ganador = baraja.getNombre()
                    ganadorTiene1 = tiene1
                    ganadorTiene8 = tiene8
            if len(ganador) != 0:#Si alguien gano
                for jugador in self.jugadores: #Se busca al ganador y se le agrega el arbol que gano
                    if jugador.getNombre() == ganador:
                        jugador.agregarArbolePuntuable(arbol)
            else:#Sino 
                for jugador in self.jugadores: #Se les dan derechos a todos
                    jugador.agregarArbolePuntuable(arbol)
                
                
    def terminarJuego(self):
        self.jugadorActual
        
        
    