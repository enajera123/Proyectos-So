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
    def generarMazo(self):
        numJugadores = len(self.jugadores)
        numColorDescart = 10-(2+(2*numJugadores)) #Calcula el numero de tipos de arbole a descartar y se guarda
        colorDescart = [] #Guarda los tipos de arbol descartados
        cartas = [] #Guarda las cartas que se van generando
        #Se hace un ciclo hasta que se descarten la cantidad de tipos necesaria
        while len(colorDescart) == numColorDescart:
            color = random.choice(Partida.Arboles) #Se saca un tipo Random de los tipos de arbol
            if colorDescart.count(color) == 0: #Se comprueba que no este descartado ya ese tipo
                colorDescart.append(color) # Se descarta
        #Se recorren todos los tipos genrando las 8 cartas de cada tipo que no este descartado
        for arbol in Partida.Arboles:
            if colorDescart.count(arbol) == 0: #Se comprueba que el tipo no este descartado
                for i in range(1,9): #Se hace un ciclo de 8 vueltas para generar las cartas
                    cartas.append(Carta(arbol,i))#Se crea y guarda la carta
        random.shuffle(cartas)#Se mesclan las cartas
        mazo = Mazo("MazoPrincipal")
        mazo.agregarCartas(cartas)
        self.mazos.append(mazo)
        
        
        
        
    