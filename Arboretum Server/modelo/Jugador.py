from modelo.Tablero import Tablero
# from modelo.Mazo import Mazo
class Jugador:
    def __init__(self,nombre):
        self.nombre = nombre
        self.cartas = []
        self.tablero = Tablero(nombre)
        self.descartes = []
        # self.baraja = Mazo(nombre)
        # self.tiposArbolPuntuable = []
    
    def ponerCartaEnTablero(self, idCarta, posx,posy):
        idCarta = int(idCarta)
        for c in self.cartas:
            if c.id == idCarta:
                c.posX = posx
                c.posY = posy
                self.cartas.remove(c)
                self.tablero.cartas.append(c)
                #Este es el funcional el que se debe usar para que se haga correctamente pero no se puede probar
                #sino hasta se agregen los turnos y demas pero deberia estar bien
                #self.tablero.agregarCarta(c) 
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
        
    def agregarArbolePuntuable(self,tiposArbol):
        self.tiposArbolPuntuable.append(tiposArbol)
        
    def getNombre(self):
        return self.nombre
    
    def setBaraja(self,cartas):
        return self.baraja.setCartas(cartas)
    
    def getBaraja(self):
        return self.baraja
    
    def cartaDescartar(self,carta):
        return self.descartes.agregarCarta(carta)
    
    def cartaJugada(self,carta):
        self.tablero.agregarCarta(carta)
    
    def cartaDescartadaTop(self):
        '''Obtiene la ultima carta ingresada'''
        return self.descartes.topCarta()
    
    def cartaDescartadaPop(self):
        '''Elimina la ultima carta ingresada'''
        self.descartes.popCarta()