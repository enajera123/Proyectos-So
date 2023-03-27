from PyQt5.QtWidgets import QMessageBox
class Alerta:
    def __init__(self,mensaje,tipo):
        self.tipo = tipo
        self.mensaje = mensaje
    def mostrarAlerta(self):
        alerta = QMessageBox()
        alerta.setWindowTitle(self.mensaje)
        if(self.tipo == "error"):
            alerta.setIcon(QMessageBox.Warning)
        else:
            alerta.setIcon(QMessageBox.Information)
        alerta.setText(self.mensaje)            
        alerta.exec_()
        