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
    def agregarCartas(self,cartas):
        for carta in cartas:
            self.cartas.append(carta)
    #Saca y elimina la ultima carata ingresada
    def sacarCarta(self):
        if (len(self.cartas)!=0):
            return self.cartas.pop()
        else:
            return None