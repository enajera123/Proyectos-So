from utilidades.Utilidades import Utilidades

class Carta:
    # =======================
    # Constantes que se usa temporalmente
    # para indicar donde guardarde el Json con los caminos
    # =======================
    #rutaJson = "bin/caminos.Json"  
    def __init__(self,id,arbol,numero):
        self.id = id
        self.posX = -1;
        self.posY = -1;
        self.arbol = arbol
        self.numero = numero
        self.cartasAdyacentes = [None,None,None,None] #Lados: (0)Izquierda, (1)Derecha, (2)Arriba, (3)Abajo
        #Las id son para uso en el lado cliente o esa es la idea lo voy a poner temporalmente sino se quita
        #asi cuando se envia y comparte cartas con el cliente se usan estos id para ubicar la posicion
        #self.idCartasAdyacentes = [None,None,None,None] #Lados: (0)Izquierda, (1)Derecha, (2)Arriba, (3)Abajo
     
    def agregarCartaAdyacente(self,carta,lado):
        '''Lado: Izquierda, Derecha, Arriba, Abajo '''
        if (lado == "Izquierda"):
            self.cartasAdyacentes[0] = carta.id
        elif (lado == "Derecha"):
            self.cartasAdyacentes[1] = carta.id
        elif (lado == "Arriba"):
            self.cartasAdyacentes[2] = carta.id
        elif (lado == "Abajo"):
            self.cartasAdyacentes[3] = carta.id
    
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
        
    def buscarCaminos(self,camino,listCaminos,listaCartas):
        #Este metodo busca cada posible camino que comienza y termina con el mismo tipo de arbol y lo escribe en un Json
        #Con el formato arbol:n/arbol:n/arbol:n siendo n el numero de carta arbol el tipo de arbol 
        #Usando el caracter / separando cada carta del camino y : separando el numero del tipo de arbol
        #Se verifica que la carta no se encuentre en el camino asi se evita bucles ya que si 
        #se encuentra quiere decir o que volvio a la carta inicia o se esta devolviendo por una carta que ya paso
        cartas = camino.split('/') #se obtienen las cartas de carta separadas por /
        cartaActual = self.arbol + ":" + str(self.numero)#Se crea la carta actual            
        if cartaActual not in cartas:#A:10     B:10
            borde = False
            # if (len(camino) == 0):#si esta vacio esta es la primer carta del camino por lo que se agrega
            #     camino = cartaActual
            # else:#sino se busca si la carta es un borde al buscar si alguno de los lados de la carta no apunta a niguna carta
            for carta in self.cartasAdyacentes:
                if carta is None:#si es un borde "borde" se vuelve true y se sale del ciclo
                    borde = True
                    break
                
            if len(camino) == 0:
                camino = cartaActual
            else:
                camino += "/" + cartaActual #Actualiza agregando la carta
                
            if borde:#si es un borde se desifra el camino y se obtine la primer carta
                #se obtinen los datos de la primera carta separada por :
                primerCarta = cartas[0].split(':')
                #Se revisa si son el mismo tipo de carta
                #Si son del mismo tipo se actualiza y guarda el camino
                if primerCarta[0] == self.arbol:
                    listCaminos.append(camino)#Se guarda
            
            #Se recorren los adyacentes ejecutando el metodo para generar el resto de caminos
            #Como al comienzo se evaluo para que no se repitan cartas en un camino no importa si vuelve
            #a ejecutar en metodo en la carta anterior
            for carta in listaCartas:
                if carta.id in self.cartasAdyacentes:
                    carta.buscarCaminos(camino[:],listCaminos, listaCartas)