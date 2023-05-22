
from modelo.Mazo import Mazo
class juegoControlador:
    def __init__(self):
        self.partida = None;
        
        #self.mazo.generarMazo(len(self.partida.jugadores))
    
    def asignarCartasToJugadores(self):
        if self.partida != None:
            self.partida.mazo.generarMazo(len(self.partida.jugadores))#Se genera el mazo
            for jugador in self.partida.jugadores:
                #Se asignan 8 cartas por cada jugador y luego se eliminan del mazo
                jugador.cartas = self.partida.mazo.cartas[:8]
                del self.partida.mazo.cartas[:8]
                # for i in jugador.cartas:
                #     print("Carta")
                #     print(i.arbol)
                #     print(i.numero)
                
        
    