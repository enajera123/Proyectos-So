import sys
from modelo.servidor import Servidor
# =======================
# Main
# =======================
print("===============================")
print("BIENVENIDO A ARBORETUM SERVER")
print("===============================")
puerto = input("Debes ingresar un numero de puerto para levantar el servidor\n")
try:
    puerto = int (puerto)
    servidor = Servidor(puerto)
    servidor.levantarServidor()
except:
    print("El puerto debe ser un numero")

