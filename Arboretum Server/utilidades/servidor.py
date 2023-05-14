import socket
import threading
import json
from modelo.Partida import Partida
from modelo.Usuario import Usuario
from controlador.juegoControlador import juegoControlador


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
                cliente = threading.Thread(target=self.hilo_cliente, args=(conn,))  # Se crea el hilo
                cliente.start()

    def conectarUsuario(self, usuario, ip, conexion):
        if not self.exists(self.listaConectados, usuario):
            self.listaConectados.append(Usuario(usuario, ip, conexion))
            conexion.sendall(json.dumps("Conectado Correctamente").encode("utf-8"))
        else:
            conexion.sendall(json.dumps("Ya existe conexion").encode("utf-8"))
    def getPartida(self):
        return self.juegoControlador.partida.__dict__
            
    def procesarConsulta(self, message, conn):
        array = message.split("+")
        print(message)
        if "conectar" in array[0]:
            self.conectarUsuario(array[1], conn.getpeername()[0], conn)
        elif "crear" in array[0]:
            conn.sendall(json.dumps(self.crearPartida(array[1], array[2])).encode("utf-8"))
        elif "unirse" in array[0]:
            conn.sendall(json.dumps(self.unirsePartida(array[1], array[2], array[3])).encode("utf-8"))
        elif "getPartida" in array[0]:
            conn.sendall(json.dumps(self.getPartida()).encode("utf-8"))
        else:
            conn.sendall("Code: 101".encode())

    def crearPartida(self, nombre, clave):
        partida = self.juegoControlador.partida
        if  partida == "":
            partida = Partida(nombre, clave)
            self.juegoControlador.partida = partida
            return partida.__dict__
        return "Hay una partida existente"
        
    def unirsePartida(self, nombre, nombrePartida, clave):
        partida = self.juegoControlador.partida
        if  partida != "" and partida.nombre == nombrePartida and partida.clave == clave:
            for i in self.listaConectados:
                if i.nombre == nombre:
                    self.juegoControlador.partida.jugadores.append(i.nombre)
                    return self.juegoControlador.partida.__dict__
            return "No se pudo unir"
        return "No se encontro partida"
                
    def exists(self, array, value):
        for i in array:
            if i.nombre == value:
                return True
        return False
