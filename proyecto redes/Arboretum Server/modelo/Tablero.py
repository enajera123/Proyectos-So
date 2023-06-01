

class Tablero:
    def __init__(self,nombre):
        self.nombre = nombre
        self.cartas = []
        #self.rutaCaminos = "/bin/Tablero_"+nombre+".json"
    def encontrarCaminos(self,tiposArboles,listCaminos):
        #Busca las cartas que sean de los colores permitidos a contar y ejecuta el metodo buscar caminos de lal cartas
        #ingresando "" vacio el camino para que se genere y se escriba en el documento del atributo rutaCaminos
        for carta in self.cartas:
            if carta.arbol in tiposArboles:
                carta.buscarCaminos("",listCaminos,self.cartas)
                
    def obtenerPuntuacionTablero(self,arbolesPuntuables):
        caminos = []
        self.encontrarCaminos(arbolesPuntuables,caminos)
        caminosValidos = []
        numCartas = []
        print("------------------------------------------------------------")
        print("Caminos sin filtrar:")
        print("\n".join(caminos))
        #---------Filtra caminos acendentes--------
        for camino in caminos:
            cartas = camino.split("/")
            numCartas = []
            #Hacemos un ciclo que recorre todas las cartas obteniendo los numeros y los guarde en un vector
            for carta in cartas:
                numCartas.append(int(carta.split(":")[1]))
            valido = True #Guarda true si es acendente y false si es desendente
            #Recorremos el vector de numeros comprobando que se una secuencia acendente
            for i in range(0,len(numCartas)-1):
                if not numCartas[i] < numCartas[i+1]:
                    valido = False
                    break
            #Si es una secuencia acendente la agregamos a la lista de validos
            if valido:
                caminosValidos.append(camino)
        #Remplazamos la lista de caminos por los caminos ya filtrados
        caminos = caminosValidos
        print("------------------------------------------------------------")
        print("Filtro secuencia acendente:")
        print("\n".join(caminos))
        #---------Filtra caminos repetidos--------
        #Hacemos un ciclo que recorra todos los cominos y elimine los que tienen mismo origen y destino
        #Dejando solo uno el mde mayor puntuacion
        caminosValidos = []
        caminosDescartados = []
        #Recorremos los caminos
        for camino in caminos:
            #Se comprueba que no sea un camino descartado
            if camino not in caminosDescartados and camino not in caminosValidos:
                valido = camino #Se guarda el camino como valido
                puntuacion_Valido = self.puntuarCaminos(valido) #se guarda la puntuacion del camino valido
                validoOrigen = valido.split("/")[0] #se guardan los extremos del camino
                validoDestino = valido.split("/")[-1]
                #Se vuelven a recorrer los caminos comparando los extremos y la puntuacion para guardar
                #en valido el de mayor putuacion
                for opcion in caminos:
                    cartas = opcion.split("/")#Se optienen las cartas del camino
                    if cartas[0] == validoOrigen and cartas[-1] == validoDestino: #Si tienen mismo origen y destino
                        puntuacion = self.puntuarCaminos(opcion) #Se saca la puntuacion del camino
                        #Se compara con las puntuaciones del valido
                        if puntuacion > puntuacion_Valido: #si es mayor se actualiza el valido y la puntuacion del valido
                            caminosDescartados.append(valido)
                            valido = opcion
                            puntuacion_Valido = puntuacion
                        else:#Si no se descarta
                            caminosDescartados.append(opcion)
                caminosValidos.append(valido) #Se agrega el camino validado a la lista de caminos validos
        caminos = caminosValidos#Se actualiza la lista de caminos
        print("------------------------------------------------------------")
        print("Filtro que no se repitan origen y destino:")
        print("\n".join(caminos))
        #---------Filtra caminos que estan contenidos en otro camino--------
        caminosValidos = []
        caminosDescartados = []
        for camino in caminos:
            if camino not in caminosDescartados and camino not in caminosValidos:
                valido = camino
                for opcion in caminos:
                    if opcion in valido:
                        caminosDescartados.append(opcion)
                    elif valido in opcion:
                        caminosDescartados.append(valido)
                        valido = opcion
                caminosValidos.append(valido)
        caminos = list(set(caminosValidos))
        
        print("------------------------------------------------------------")
        print("Filtro que no esten contenidos en otro camino:")
        print("\n".join(caminos))
        #---------Se obtinen las puntuaciones de los caminos--------
        puntuacion_Total = []
        #Como ya se tiene la lista de caminos que se pueden puntuar en el tablero se puntuan y se suman
        #las puntuaciones para retornarlas 
        for camino in caminos:
            puntuacion_Total.append(camino + "=" + str(self.puntuarCaminos(camino))) 
        print("------------------------------------------------------------")
        print("Caminos puntuados:")
        print("\n".join(puntuacion_Total))
        return puntuacion_Total
    
    def puntuarCaminos(self,camino):
        cartas = camino.split("/")
        #Primero se agrega un punto por cada carta que forma el camino
        puntos = len(cartas) 
        #Se hace una lista de listas donde la primer lista continene una lista con el numero y tipo de arbol de cada carta
        for i in range(len(cartas)):
            cartas[i] = cartas[i].split(":")
        #Segundo se agregan los puntos extra por carta si son del mismo tipo todas las cartas y tiene al menos 4 cartas
        arbolCamino = cartas[0][0] #Se obtiene el tipo de arbol que es el camino
        mismoTipo = True #Si todas las cartas son del mismo tipo es true para contar los puntos adicionales
        for carta in cartas:
            if carta[0] != arbolCamino:
                mismoTipo = False
                break
        if mismoTipo and len(cartas) >= 4:
            puntos += len(cartas) #Un punto extra por carta si son del mismo tipo y tiene almenos 4 cartas
        #Tercero si inicia en 1 se le agrega un punto adicional
        if cartas[0][1] == "1":
            puntos += 1
        #Cuarto si termina en 8 se le agrega dos puntos adicionales
        if cartas[-1][1] == "8":
            puntos += 2
        return puntos
    def agregarCarta(self,cartaNueva):
        #Se asignan punteros a las cartas adyacentes
        #El formato de agregarCartaAdyacente(carta,Lado) Lado: Izquierda, Derecha, Arriba, Abajo
        nPosX = int(cartaNueva.posX)
        nPosY = int(cartaNueva.posY)
        for carta in self.cartas:
            posX = int(carta.posX)
            posY = int(carta.posY)
            if posX == nPosX-1 and posY == nPosY:
                carta.agregarCartaAdyacente(cartaNueva,"Derecha")
                cartaNueva.agregarCartaAdyacente(carta,"Izquierda")
            elif posX == nPosX+1 and posY == nPosY:
                carta.agregarCartaAdyacente(cartaNueva,"Izquierda")
                cartaNueva.agregarCartaAdyacente(carta,"Derecha")
            elif posX == nPosX and posY == nPosY-1:
                carta.agregarCartaAdyacente(cartaNueva,"Abajo")
                cartaNueva.agregarCartaAdyacente(carta,"Arriba")
            elif posX == nPosX and posY == nPosY+1:
                carta.agregarCartaAdyacente(cartaNueva,"Arriba")
                cartaNueva.agregarCartaAdyacente(carta,"Abajo")
        self.cartas.append(cartaNueva)# Se agrega la carta nueva a las cartas
        
    def modificarPosicionCarta(self, idCarta, posx, posy):
        """Modifica la posicion de la carta en el tablero"""
        idCarta = int(idCarta)#Se sanitizan los datos
        posx = int(posx)
        posy = int(posy)
        for c in self.cartas:#Busqueda por id
          if c.id == idCarta:
            c.posX = posx#Cambio de posicion
            c.posY = posy
            return True
        return False

        
        
                

        
                            
                
            