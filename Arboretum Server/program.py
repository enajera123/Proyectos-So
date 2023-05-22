import sys
from utilidades.servidor import Servidor
from controlador.juegoControlador import juegoControlador
from modelo.Partida import Partida
from modelo.Jugador import Jugador
# =======================
# Main
# =======================
print("===============================")
print("BIENVENIDO A ARBORETUM SERVER")
print("===============================")
puerto = input("Debes ingresar un numero de puerto para levantar el servidor\n")

puerto = int (puerto)
servidor = Servidor(puerto)
servidor.levantarServidor()
# game = juegoControlador()
# game.partida = Partida("a","123")
# game.partida.jugadores.append(Jugador("a"))
# game.partida.jugadores.append(Jugador("a"))
# game.partida.jugadores.append(Jugador("a"))
# game.partida.jugadores.append(Jugador("a"))
# game.asignarCartasToJugadores()
