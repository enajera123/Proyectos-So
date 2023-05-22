# Se puede usar tanto para el mazo principal como para los de descartes
# Para el mazo principal las cartas se pueden generar en el objeto paratida y luego se ingresan
# Pienso que tambien se puede usar para la baraja si se le hacen algunos metodos especificamente para eso
import random
from modelo.Carta import Carta


class Mazo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.cartas = []

    def generarMazo(self, cantidadJugadores):
        """Genera el mazo principal de acuerdo a la cantidad de jugadores"""
        #Se tiene una lista con los colores, revueltos con la funcion shuffle
        colores = ["blossom cherry", "celestial magnolia", "exotic tree", "giant sequoia",
                   "golden mapple", "moonlit willow","quivering aspen", "purple fir", "tree of love", "whispering willow"]
        random.shuffle(colores)
        #El comando ":" obtiene las primeras n posiciones definidas del arreglo
        coloresFiltrados = colores[:cantidadJugadores*2 + 2]
        id = 0
        for color in coloresFiltrados:
            for j in range(1, 9):
                self.cartas.append(Carta(id, color, j))
                id += 1
        #Se vuelve a llamar la funcion para revolver todas las cartas generadas
        random.shuffle(self.cartas)

    def agregarCarta(self, carta):
        self.cartas.append(carta)
        
    def setCartas(self,cartas):
        self.cartas = cartas
            
    def getNombre(self):
        return self.nombre
    
    def getCartas(self):
        return self.cartas

    def agregarCartas(self, cartas):
        for carta in cartas:
            self.cartas.append(carta)

    def popCarta(self):
        '''Elimina la ultima carta ingresada'''
        if (len(self.cartas) != 0):
            self.cartas.pop()

    def topCarta(self):
        '''Obtiene la ultima carta ingresada'''
        if (len(self.cartas) != 0):
            return self.cartas[-1]
        else:
            return None
