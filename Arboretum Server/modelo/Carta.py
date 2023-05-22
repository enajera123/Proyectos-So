from utilidades.Utilidades import Utilidades

class Carta:
    # =======================
    # Constantes que se usa temporalmente
    # para indicar donde guardarde el Json con los caminos
    # =======================
    rutaJson = "bin/caminos.Json"  
    def __init__(self,id,arbol,numero):
        self.id = id
        self.arbol = arbol
        self.numero = numero
        self.cartasAdyacentes = [None,None,None,None] #Lados: (0)Izquierda, (1)Derecha, (2)Arriba, (3)Abajo
        #Las id son para uso en el lado cliente o esa es la idea lo voy a poner temporalmente sino se quita
        #asi cuando se envia y comparte cartas con el cliente se usan estos id para ubicar la posicion
        self.idCartasAdyacentes = [None,None,None,None] #Lados: (0)Izquierda, (1)Derecha, (2)Arriba, (3)Abajo
    def obtenerId(self):
         return self.id
    def obtenerNumero(self):
         return self.numero   
    def obtenerArbol(self):
         return self.arbol   
    def agregarCartaAdyacente(self,carta,lado):
        '''Lado: Izquierda, Derecha, Arriba, Abajo '''
        if (lado == "Izquierda"):
            self.cartasAdyacentes[0] = carta
            self.idCartasAdyacentes[0] = carta.obtenerId()
        elif (lado == "Derecha"):
            self.cartasAdyacentes[1] = carta
            self.idCartasAdyacentes[0] = carta.obtenerId()
        elif (lado == "Arriba"):
            self.cartasAdyacentes[2] = carta
            self.idCartasAdyacentes[0] = carta.obtenerId()
        elif (lado == "Abajo"):
            self.cartasAdyacentes[3] = carta
            self.idCartasAdyacentes[0] = carta.obtenerId()
    def obtenerCartaAdyacente(self,lado):
        '''Lado: Izquierda, Derecha, Arriba, Abajo '''
        if (lado == "Izquierda"):
            return self.cartasAdyacentes[0]
        elif (lado == "Derecha"):
            return self.cartasAdyacentes[1]
        elif (lado == "Arriba"):
            return self.cartasAdyacentes[2]
        elif (lado == "Abajo"):
            return self.cartasAdyacentes[3]
        else:
            return None
    #Este metodo busca cada posible camino que comienza y termina con el mismo tipo de arbol y lo escribe en un Json
    #Con el formato arbol:n/arbol:n/arbol:n siendo n el numero de carta arbol el tipo de arbol el / separando cada carta
    #del camino y : separando el numero del tipo de arbol
    def buscarCaminos(self,camino,ruta):
        '''Lado: Izquierda, Derecha, Arriba, Abajo  Ruta: ruta del Json donde se guardan los caminos'''
        if (len(camino) == 0):#si esta vacio esta es la primer carta del camino por lo que se agrega
            camino = self.arbol + ":" + self.numero
        else:#sino se busca si la carta es un borde al buscar si alguno de los lados de la carta no apunta a niguna carta
            for carta in self.cartasAdyacentes:
                if carta is None:#si es un borde se desifra el camino y se obtine la primer carta
                    #se obtienen las cartas de carta separadas por /
                    partes = camino.split('/')
                    #se obtinen los datos de la primera carta separada por :
                    primerCarta = partes[0].split(':')
                    #Se revisa si son el mismo tipo de carta pero diferente numero caminos en bucle
                    #y si son del mismo tipo se actualiza y guarda el camino
                    if primerCarta[0] == self.arbol and primerCarta[1] != self.numero:
                        camino += "/" + self.arbol + ":" + self.numero #Actualiza agregando la carta
                        Utilidades.guardarDato(camino,ruta)#Se guarda
                    break
        #Se verifica que la carta de inicio del camino y l actual no sean la misma para no generar bucles
        #Si no son la misma se vuelve a ejecutar el metodo en todas las cartas adyacentes
        partes = camino.split('/')
        if not (primerCarta[0] == self.arbol and primerCarta[1] == self.numero):
            for carta in self.cartasAdyacentes:
                if not carta is None:
                    #se obtinen los datos de la ultima carta separada por :
                    ultimaCarta = partes[-1].split(':')
                    #Si la carta adyacente actual es igual a la ultima no se ejecuta el metodo para no generar bucles
                    if not ultimaCarta[0] == carta.obtenerArbol() and ultimaCarta[1] == carta.obtenerNumero():
                        carta.buscarCaminos(camino,ruta)