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