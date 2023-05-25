from modelo.Tablero import Tablero
# from modelo.Mazo import Mazo
class Jugador:
    def __init__(self,nombre):
        self.nombre = nombre
        self.cartas = []
        self.tablero = Tablero(nombre)
        self.descartes = []
        self.arbolesPuntuables = []
        # self.baraja = Mazo(nombre)
    
    def ponerCartaEnTablero(self, idCarta, posx,posy):
        idCarta = int(idCarta)
        for c in self.cartas:
            if c.id == idCarta:
                c.posX = posx
                c.posY = posy
                self.cartas.remove(c)
                #self.tablero.cartas.append(c)
                self.tablero.agregarCarta(c) 
                return True
        return False
    
    def descartarCarta(self, idCarta):
        idCarta = int(idCarta)
        for c in self.cartas:
            if c.id == idCarta:
                c.posX = -2#Se pone en -2 para identificar que esta en un mazo descarte
                c.posY = -2
                self.cartas.remove(c)
                self.descartes.append(c)
                return True
        return False
    
    def sacarCartaDescarte(self, idCarta):
        idCarta = int(idCarta)
        for c in self.descartes:
            if c.id == idCarta:
                c.posX = -1#Se pone en -1 para identificar que esta en la mano
                c.posY = -1
                self.descartes.remove(c)
                return c
        return None
    
    def modificarPosicionCartaTablero(self, idCarta, posx,posy):
        return self.tablero.modificarPosicionCarta(idCarta, posx, posy)
    