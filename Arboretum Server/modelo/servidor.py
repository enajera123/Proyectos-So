import socket
class Servidor:
    def __init__(self, puerto):
        self.listaConectados = {}
        self.puerto = puerto

    def levantarServidor(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind(("", self.puerto))
            s.listen()
            print("Server iniciado, esperando conexiones en el puerto: ", self.puerto)

            self.entablarConexion(s)

    def entablarConexion(self, s):
        conn, addr = s.accept()
        with conn:
            self.listaConectados[addr] = conn
            conn.sendall("Conexion establecida".encode())

    def recibirInformacion(self, conexion):
        while True:
            data = conexion.recv(1024)
            if not data:
                break
            print("Datos recibidos ", data.decode())
