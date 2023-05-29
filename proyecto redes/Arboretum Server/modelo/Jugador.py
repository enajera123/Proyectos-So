from modelo.Tablero import Tablero
# from modelo.Mazo import Mazo
class Jugador:
    def __init__(self,nombre):
        self.nombre = nombre
        self.cartas = []
        self.tablero = Tablero(nombre)
        self.descartes = []
        self.tiposArbolPuntuable = []
    
    def ponerCartaEnTablero(self, idCarta, posx,posy):
        """Agrega una carta a la lista y le asigna una pos x,y"""
        idCarta = int(idCarta)
        for c in self.cartas:
            if c.id == idCarta:
                c.posX = posx
                c.posY = posy
                self.cartas.remove(c)#Remueve de las cartas
                #self.tablero.cartas.append(c)#Agrega al tablero
                self.tablero.agregarCarta(c)
                return True
        return False
    
    def descartarCarta(self, idCarta):
        """Se descarta una carta y se agrega al mazo de descarte"""
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
        """Se saca una carta del mazo de descarte"""
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