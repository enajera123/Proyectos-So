#Se puede usar tanto para el mazo principal como para los de descartes
#Para el mazo principal las cartas se pueden generar en el objeto paratida y luego se ingresan
#Pienso que tambien se puede usar para la baraja si se le hacen algunos metodos especificamente para eso
class Mazo:
    def __init__(self,nombre):
        self.nombre = nombre
        self.cartas = []
    #append() agrega al final de la lista
    def agregarCarta(self,carta):
        self.cartas.append(carta)
        
    def setCartas(self,cartas):
        self.cartas = cartas
            
    def getNombre(self):
        return self.nombre
    
    def getCartas(self):
        return self.cartas
        
    def popCarta(self):
        '''Elimina la ultima carta ingresada'''
        if (len(self.cartas)!=0):
            self.cartas.pop()
            
    def topCarta(self):
        '''Obtiene la ultima carta ingresada'''
        if (len(self.cartas)!=0):
            return self.cartas[-1]
        else:
            return None