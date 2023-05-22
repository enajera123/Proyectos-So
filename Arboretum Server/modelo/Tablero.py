from utilidades.Utilidades import Utilidades

class Tablero:
    def __init__(self,nombre):
        self.nombre = nombre
        self.cartas = []
        self.rutaCaminos = "/bin/Tablero_"+nombre+".json"
    def encontrarCaminos(self,tiposArboles):
        #Busca las cartas que sean de los colores permitidos a contar y ejecuta el metodo buscar caminos de lal cartas
        #ingresando "" vacio el camino para que se genere y se escriba en el documento del atributo rutaCaminos
        for carta in self.cartas:
            if carta.obtenerArbol() in tiposArboles:
                carta.buscarCaminos("",self.rutaCaminos)
    def obtenerPuntuacionTablero(self):
        caminos = Utilidades.leerDatos(self.rutaCaminos)
        caminosValidos = []
        numCartas = []
        #Hacemos un ciclo que recorra todos los cominos y elimine los que no son de numeros acendentes de la lista
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
            #Si no es una secuencia acendente lo quitamos de la lista
            if not valido:
                caminosValidos.remove(camino)
        #Remplazamos la lista de caminos por los caminos ya filtrados
        caminos = caminosValidos
        #Hacemos un ciclo que recorra todos los cominos y elimine los que tienen mismo origen y destino
        #Dejando solo uno el mde mayor puntuacion
        extremos = []
        caminosValidos = []
        caminosDescartados = []
        #Recorremos los caminos
        for camino in caminos:
            #Se comprueba que no sea un camino descartado
            if camino not in caminosDescartados:
                valido = camino #Se guarda el camino como valido
                puntuacion_Valido = Tablero.puntuarCaminos(valido) #se guarda la puntuacion del camino valido
                extremos.append(valido.split("/")[0]) #se guardan los extremos del camino
                extremos.append(valido.split("/")[-1])
                #Se vuelven a recorrer los caminos comparando los extremos y la puntuacion para guardar
                #en valido el de mayor putuacion
                for opcion in caminos:
                    cartas = opcion.split("/")#Se optienen las cartas del camino
                    if cartas[0] == extremos[0] and cartas[-1] == extremos[1]: #Si tienen mismo origen y destino
                        puntuacion = Tablero.puntuarCaminos(opcion) #Se saca la puntuacion del camino
                        #Se compara con las puntuaciones del valido
                        if puntuacion > puntuacion_Valido: #si es mayor se actualiza el valido y la puntuacion del valido
                            caminosDescartados.append(valido)
                            valido = opcion
                            puntuacion_Valido = puntuacion
                        else:#Si no se descarta
                            caminosDescartados.append(opcion)
                caminosValidos.append(valido) #Se agrega el camino validado a la lista de caminos validos
        caminos = caminosValidos#Se actualiza la lista de caminos
        puntuacion_Total = 0
        #Como ya se tiene la lista de caminos que se pueden puntuar en el tablero se puntuan y se suman
        #las puntuaciones para retornarlas 
        Utilidades.limpiarDatos(self.rutaCaminos)
        for camino in caminos:
            puntuacion_Total += Tablero.puntuarCaminos(camino)
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
        #Obtiene las id de las cartas adyacentes de la nueva carta y las busca en la lista de cartas del tablero
        #Y actualiza las adyacentes ejemplo a la carta de arriba se agrega a si mismo como la de abajo
        #El formato del vector que devuelve obtenerIdCartasAdyacentes es (0)Izquierda, (1)Derecha, (2)Arriba, (3)Abajo
        #El formato de agregarCartaAdyacente(carta,Lado) Lado: Izquierda, Derecha, Arriba, Abajo
        for carta in self.cartas:
            cartasAdyacentesId = cartaNueva.obtenerIdCartasAdyacentes()
            if carta.obtenerId() == cartasAdyacentesId[0]:
                carta.agregarCartaAdyacente(cartaNueva,"Derecha")
            elif carta.obtenerId() == cartasAdyacentesId[1]:
                carta.agregarCartaAdyacente(cartaNueva,"Izquierda")
            elif carta.obtenerId() == cartasAdyacentesId[2]:
                carta.agregarCartaAdyacente(cartaNueva,"Abajo")
            elif carta.obtenerId() == cartasAdyacentesId[3]:
                carta.agregarCartaAdyacente(cartaNueva,"Arriba")
        self.cartas.append(cartaNueva)# Se agrega la carta nueva a las cartas
        
        
        
                

        
                            
                
            