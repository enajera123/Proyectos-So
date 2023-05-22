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
    
    def obtenerIdCartasAdyacentes(self):
        '''Lados: (0)Izquierda, (1)Derecha, (2)Arriba, (3)Abajo'''
        return self.idCartasAdyacentes
    
    def buscarCaminos(self,camino,ruta):
        #Este metodo busca cada posible camino que comienza y termina con el mismo tipo de arbol y lo escribe en un Json
        #Con el formato arbol:n/arbol:n/arbol:n siendo n el numero de carta arbol el tipo de arbol 
        #Usando el caracter / separando cada carta del camino y : separando el numero del tipo de arbol
        '''Lado: Izquierda, Derecha, Arriba, Abajo  Ruta: ruta del Json donde se guardan los caminos'''
        cartaActual = self.arbol + ":" + str(self.numero)
        if (len(camino) == 0):#si esta vacio esta es la primer carta del camino por lo que se agrega
            camino = cartaActual
        else:#sino se busca si la carta es un borde al buscar si alguno de los lados de la carta no apunta a niguna carta
            borde = False
            for carta in self.cartasAdyacentes:
                if carta is None:#si es un borde "borde" se vuelve true y se sale del ciclo
                    borde = True
                    break
        #Se verifica que la carta no se encuentre en el camino asi se evita bucles
        #ya que si se encuentra quiere decir o que volvio a la carta inicia o se esta devolviendo por
        #una carta que ya paso
        cartas = camino.split('/') #se obtienen las cartas de carta separadas por /
        if cartaActual not in cartas:
            if borde:#si es un borde se desifra el camino y se obtine la primer carta
                #se obtinen los datos de la primera carta separada por :
                primerCarta = cartas[0].split(':')
                #Se revisa si son el mismo tipo de carta
                #Si son del mismo tipo se actualiza y guarda el camino
                if primerCarta[0] == self.arbol:
                    camino += "/" + cartaActual #Actualiza agregando la carta
                    Utilidades.guardarDato(camino,ruta)#Se guarda
            #Se recorren los adyacentes ejecutando el metodo para generar el resto de caminos
            #Como al comienzo se evaluo para que no se repitan cartas en un camino no importa si vuelve
            #a ejecutar en metodo en la carta anterior
            for carta in self.cartasAdyacentes:
                if not carta is None:
                    carta.buscarCaminos(camino,ruta)