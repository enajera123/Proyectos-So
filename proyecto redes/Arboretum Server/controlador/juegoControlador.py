
from modelo.Mazo import Mazo


class juegoControlador:
    def __init__(self):
        self.partida = None

    def cambiarTurno(self):
        if self.partida.cambiarJugador():
            return True
        return False
        
    def asignarCartasToJugadores(self,nombreJugador):
        if self.partida != None:
            self.partida.generarMazo(len(self.partida.jugadores))  # Se genera el mazo
            for jugador in self.partida.jugadores:
                # Se asignan 7 cartas por cada jugador y luego se eliminan del mazo
                jugador.cartas = self.partida.mazo.cartas[:7]
                del self.partida.mazo.cartas[:7]
                if jugador.nombre != nombreJugador:
                    jugador.descartes.append(self.partida.mazo.cartas.pop())

    def ponerCartaTablero(self, nombreJugador, idCarta, posx, posy):
        for i in self.partida.jugadores:
            if i.nombre == nombreJugador:
                if i.ponerCartaEnTablero(idCarta, posx, posy):
                    return True
        return False

    def modificarPosicionCartaTablero(self, nombreJugador, idCarta, posx, posy):
        for j in self.partida.jugadores:
            if j.nombre == nombreJugador:
                return j.modificarPosicionCartaTablero(idCarta, posx, posy)
        return False

    def agregarCartaJugador(self, nombreJugador, idCarta):
        for j in self.partida.jugadores:
            if j.nombre == nombreJugador:
                carta = self.partida.mazo.popCarta()
                print(carta.id)
                print(idCarta)
                j.cartas.append(carta)
                return True
        return False

    def descartarCarta(self, nombreJugador, idCarta):
        for j in self.partida.jugadores:
            if j.nombre == nombreJugador:
                j.descartarCarta(idCarta)
                return True
        return False

    def sacarCartaDescarte(self, nombreJugador, idCarta):
        for j in self.partida.jugadores:
            if j.nombre == nombreJugador:
                jugador = j
            carta = j.sacarCartaDescarte(idCarta)
            if carta != None:
                jugador.cartas.append(carta)
                return True
        return False
    def terminarJuego(self):
        #Se le asigna a cada jugador que arboles del tablero puede puntuar al comparar barajas
        self.partida.asignarDerechosApuntuar()
        #Se obtiene la puntacion del tablero de cada jugador y se guarda en un string junto con el nombre del jugador
        #en esta estructura jugador:puntuacion
        puntuaciones = []
        for jugador in self.partida.jugadores:
            puntuacion = jugador.nombre + ":" + str(jugador.tablero.obtenerPuntuacionTablero(jugador.tiposArbolPuntuable))
            puntuaciones.append(puntuacion)
        return puntuaciones