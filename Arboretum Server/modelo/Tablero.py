from utilidades.Utilidades import Utilidades

class Tablero:
    def __init__(self,nombre):
        self.nombre = nombre
        self.cartas = []
        self.rutaCaminos = "/bin/Tablero_"+nombre+".json"
    #Busca las cartas que sean de los colores permitidos a contar y ejecuta el metodo buscar caminos de lal cartas
    #ingresando "" vacio el camino para que se genere y se escriba en el documento del atributo rutaCaminos
    def encontrarCaminos(self,tiposArboles):
        for carta in self.cartas:
            if tiposArboles.count(carta.ObtenerArbol) != 0:
                carta.buscarCaminos("",self.rutaCaminos)
    def obtenerPuntuacionTablero(self):
        caminos = Utilidades.leerDatos(self.rutaCaminos)
        caminosValidos = []
        numCartas = []
        #Hacemos un ciclo que recorra todos los cominos y elimine los que no son de numeros acendentes de la lista
        for camino in caminos:
            cartas = camino.split("/")
            #Hacemos un ciclo que recorre todas las cartas obteniendo los numeros y los guarde en un vector
            for carta in cartas:
                numCartas.append(carta.split(":")[1])
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
            if caminosDescartados.count(camino) == 0:
                valido = camino #Se guarda el camino como valido
                puntuacion_Valido = Tablero.puntuarCaminos(valido) #se guarda la puntuacion del camino valido
                extremos.append(valido.split("/")[0],valido.split("/")[-1]) #se guardan los extremos del camino
                #Se vuelven a recorrer los caminos comparando los extremos y la puntuacion para guardar
                #en valido el de mayor putuacion
                for opcion in caminos:
                    cartas = opcion.split("/")#Se optienen las cartas del camino
                    if cartas[0] == extremos[0] and cartas[-1] == extremos[1]: #Si tienen mismo origen y destino
                        puntuacion = Tablero.puntuarCaminos(opcion) #Se saca la puntuacion del camino
                        #Se compara con las puntuaciones del valido
                        if puntuacion > puntuacion_Valido: #si es mayor se actualiza el valido y la puntuacion del valido
                            caminosDescartados.appendI(valido)
                            valido = opcion
                            puntuacion_Valido = puntuacion
                        else:#Si no se descarta
                            caminosDescartados.appendI(opcion)
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
        #Hay que hacer la logica de si es uno al principio o 8 al final y todo eso
        cartas = camino.split("/")
                            
                
            