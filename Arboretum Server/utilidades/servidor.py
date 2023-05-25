import socket
import threading
import json
from modelo.Partida import Partida
from modelo.Usuario import Usuario
from controlador.juegoControlador import juegoControlador
from modelo.Jugador import Jugador
from modelo.Carta import Carta
from utilidades.Utilidades import Utilidades


class Servidor:
    def __init__(self, puerto):
        self.listaConectados = []
        self.puerto = puerto
        self.juegoControlador = juegoControlador()

    def levantarServidor(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind(("", self.puerto))
        s.listen()
        print("Server iniciado, esperando conexiones en el puerto: ", self.puerto)
        self.escuchar(s)

    def hilo_cliente(self, conexion):
        data = conexion.recv(1024)
        if data:
            self.procesarConsulta(data.decode(), conexion)

    def escuchar(self, s):
        while True:
            conn, addr = s.accept()
            if (conn and addr):
                cliente = threading.Thread(
                    target=self.hilo_cliente, args=(conn,))  # Se crea el hilo
                cliente.daemon = True
                cliente.start()

    def conectarUsuario(self, usuario, ip, conexion):
        if not self.exists(self.listaConectados, usuario):
            self.listaConectados.append(Usuario(usuario, ip, conexion))
            conexion.sendall(json.dumps(
                "Conectado Correctamente").encode("utf-8"))
        else:
            conexion.sendall(json.dumps("Ya existe conexion").encode("utf-8"))

    def procesarConsulta(self, message, conn):
        array = message.split("+")
        print(message)
        if "conectar" in array[0]:
            self.conectarUsuario(array[1], conn.getpeername()[0], conn)
        elif "crear" in array[0]:
            conn.sendall(self.crearPartida(array[1], array[2]))
        elif "unirse" in array[0]:
            conn.sendall(self.unirsePartida(array[1], array[2], array[3]))
        elif "empezar" in array[0]:
            conn.sendall(self.empezarPartida(array[1]))
        elif "modificarCartaTablero" in array[0]:
            conn.sendall(self.modificarCartaTablero(
                array[1], array[2], array[3], array[4]))
        elif "agregarCartaTablero" in array[0]:
            conn.sendall(self.agregarCartaTablero(
                array[1], array[2], array[3], array[4]))
        elif "agregarCartaJugador" in array[0]:
            conn.sendall(self.agregarCartaJugador(array[1], array[2]))
        elif "descartaCarta" in array[0]:
            conn.sendall(self.descartaCarta(array[1], array[2]))
        elif "sacarCartaDescarte" in array[0]:
            conn.sendall(self.sacarCartaDescarte(array[1], array[2]))
        # elif "partida" in array[0]:
        #     conn.sendall(self.Partida())
        elif "getPartida" in array[0]:
            conn.sendall(self.getPartida())
        elif "salir" in array[0]:
            conn.sendall(json.dumps(
                self.salirPartida(array[1])).encode("utf-8"))
        else:
            conn.sendall("Code: 101".encode())

 # =======================
 # Funciones Partida
 # =======================
    def sacarCartaDescarte(self, nombreJugador, idCarta):
        if self.juegoControlador.sacarCartaDescarte(nombreJugador, idCarta):
            return json.dumps(self.juegoControlador.partida, default=lambda o: o.__dict__).encode("utf-8")
        return json.dumps("error").encode("utf-8")

    def modificarCartaTablero(self, nombreJugador, idCarta, posx, posy):
        if self.juegoControlador.modificarPosicionCartaTablero(nombreJugador, idCarta, posx, posy):
            return json.dumps(self.juegoControlador.partida, default=lambda o: o.__dict__).encode("utf-8")
        return json.dumps("error").encode("utf-8")

    def descartaCarta(self, nombreJugador, idCarta):
        if self.juegoControlador.descartarCarta(nombreJugador, idCarta):
            return json.dumps(self.juegoControlador.partida, default=lambda o: o.__dict__).encode("utf-8")
        return json.dumps("error").encode("utf-8")

    def agregarCartaJugador(self, nombreJugador, idCarta):
        idCarta = int(idCarta)
        if self.juegoControlador.agregarCartaJugador(nombreJugador, idCarta):
            return json.dumps(self.juegoControlador.partida, default=lambda o: o.__dict__).encode("utf-8")
        return json.dumps("error").encode("utf-8")

    def empezarPartida(self,jugadorActual):
        self.juegoControlador.asignarCartasToJugadores(jugadorActual)
        self.juegoControlador.partida.iniciado = True
        # return json.dumps(self.juegoControlador.partida,default=lambda o: o.__dict__)
        return json.dumps("Empezado").encode("utf-8")

    def agregarCartaTablero(self, nombreJugador, idCarta, posx, posy):
        if self.juegoControlador.ponerCartaTablero(nombreJugador, idCarta, posx, posy):
            return json.dumps(self.juegoControlador.partida, default=lambda o: o.__dict__).encode("utf-8")
        return json.dumps("error").encode("utf-8")
    # def getCarta(self):
    #     return json.dumps(Carta(1,"a",20), default=lambda o:o.__dict__).encode("utf-8")
    # def Partida(self):
    #     self.juegoControlador.partida = Partida("a", "a")
    #     self.juegoControlador.partida.mazo.generarMazo(4)
    #     jugador = Jugador("nombre")
    #     self.juegoControlador.partida.jugadores.append(jugador)
    #     self.juegoControlador.asignarCartasToJugadores()

    #     return json.dumps(self.juegoControlador.partida, default=lambda o:o.__dict__).encode("utf-8")

    # def getMazo(self):
    #     self.juegoControlador.mazo.generarMazo(4)
    #     return json.dumps(self.juegoControlador.mazo, default=lambda o:o.__dict__).encode("utf-8")
    # def getJugador(self):
    #     self.juegoControlador.mazo.generarMazo(4)
    #     self.juegoControlador.partida = Partida("a", "a")
    #     jugador = Jugador("nombre")

    #     self.juegoControlador.partida.jugadores.append(jugador)
    #     self.juegoControlador.asignarCartasToJugadores()
    #     return json.dumps(self.juegoControlador.partida.jugadores[0], default=lambda o:o.__dict__).encode("utf-8")

    #     #return json.dumps(Carta(1,"a",20).__dict__).encode("utf-8")

    def getPartida(self):
        if self.juegoControlador.partida != None:
            return json.dumps(self.juegoControlador.partida, default=lambda o: o.__dict__).encode("utf-8")
        return json.dumps("error").encode("utf-8")

    def crearPartida(self, nombre, clave):
        partida = self.juegoControlador.partida
        if partida == None:
            partida = Partida(nombre, clave)
            # partida.mazo.generarMazo(cantidadJugadores)
            self.juegoControlador.partida = partida

            return json.dumps(partida, default=lambda o: o.__dict__).encode("utf-8")
        return json.dumps("Hay una partida existente").encode("utf")

    def salirPartida(self, nombre):
        partida = self.juegoControlador.partida
        if partida != None:
            for i in partida.jugadores:
                if i.nombre == nombre:
                    partida.jugadores.remove(i)
                    if len(partida.jugadores) == 0:
                        self.juegoControlador.partida = None
                    return "Exito"
            return "No se encontro jugador"
        return "No se encontro partida"

    def unirsePartida(self, nombreJugador, nombrePartida, clave):
        # jugador = Utilidades.deserializarJugador(jugador)
        partida = self.juegoControlador.partida
        if partida != None and partida.nombre == nombrePartida and partida.clave == clave:
            for i in self.listaConectados:
                if i.nombre == nombreJugador:
                    self.juegoControlador.partida.jugadores.append(
                        Jugador(nombreJugador))
                    return json.dumps(self.juegoControlador.partida, default=lambda o: o.__dict__).encode("utf-8")
            return json.dumps("No se pudo unir").encode("utf-8")
        return json.dumps("No se encontro partida").encode("utf-8")

    def exists(self, array, value):
        for i in array:
            if i.nombre == value:
                return True
        return False
