class RadioButonUtilidades:
    def __init__(self):
        super(RadioButonUtilidades, self).__init__()
        
    def leerRadioButons(*args):
        cadena = ""
        lectura = args[0]
        escritura = args[1]
        ejecucion = args[2]
        if (lectura.isChecked()):
            cadena += "[Lectura]"
        if (escritura.isChecked()):
            cadena += "[Escritura]"
        if (ejecucion.isChecked()):
            cadena += "[Ejecucion]"
        if not (lectura.isChecked() or escritura.isChecked() or ejecucion.isChecked()):
            cadena += "[None]"
        return cadena
    def reiniciarRadioButons(*args):
        for arg in args:
            arg.setChecked(False)
            
        
    def llenarRadioButtons(self,permisos):
        if("Lectura" in permisos):
            self.rbtnLectura.setChecked(True)
        else:
            self.rbtnLectura.setChecked(False)
        if("Ejecucion" in permisos):
            self.rbtnEjecucion.setChecked(True)
        else:
            self.rbtnEjecucion.setChecked(False)
        if("Escritura" in permisos):
            self.rbtnEscritura.setChecked(True)
        else:
            self.rbtnEscritura.setChecked(False)