import socket
import threading
import json
from modelo.Partida import Partida
from modelo.Usuario import Usuario


class Servidor:
    def __init__(self, puerto):
        self.listaConectados = []
        self.puerto = puerto

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
        pass
            
    def escuchar(self, s):
        while True:
            conn, addr = s.accept()
            cliente = threading.Thread(target=self.hilo_cliente, args=(conn,))#Se crea el hilo
            cliente.start()
            print("hola")
            
            
    def conectarUsuario(self, usuario, ip, conexion):
        if not self.exists(self.listaConectados, ip):
            self.listaConectados.append(Usuario(usuario, ip, conexion))
            conexion.sendall(json.dumps("Conectado Correctamente").encode("utf-8"))

    def procesarConsulta(self, message, conn):
        array = message.split("+")
        print(message)
        if "conectar" in array[0]:
            self.conectarUsuario(array[1], conn.getpeername()[0], conn)
        else:
            conn.sendall("Code: 101".encode());

    def exists(self, array, value):
        for i in array:
            if i.ip == value:
                return True
        return False
