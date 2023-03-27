import os
import shutil


class ManejoArchivo:
    def __init__(self):
        super(ManejoArchivo, self).__init__()

    def crearCarpeta(nombreCarpeta):
        if (os.path.exists("bin/"+nombreCarpeta)):
            shutil.rmtree("bin/"+nombreCarpeta)
        os.mkdir("bin/"+nombreCarpeta)
        
