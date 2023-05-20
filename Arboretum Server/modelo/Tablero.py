#En esta clase se pueden hacer los metodos que involucran la obtencion de caminos y el conteo de puntos
#por ejemplo puede aver un metodo al que se le ingrese los tipos de arboles que son validos para el conteo
#entonces se buscan las cartas de esos tipos en la lista de cartas del tablero y se ejecuta el bucar caminos en cada carta
#ya con eso tados los posibles caminos entre cartas del mismo tipo de arbol quedan mapeados en la json
#Luego otro metodo que decifre el Json y examine camino por camino si cumplen las condiciones para que cuenten como
#camino valido (lo de que tienen que ser numeros asendentes y eso) luego estos se escriben en otro Json
#y ya en otro metodo se lee el Json con los caminos validos y se las condicones para contar los puntos de cada camino
class Tablero:
    def __init__(self,nombre):
        self.nombre = nombre
        self.cartas = []
