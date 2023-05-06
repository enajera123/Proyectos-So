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
    def mostrarAlertaConBoton(self):
        alert = QMessageBox()
        alert.setText(self.mensaje)
        alert.setWindowTitle(self.tipo)
        alert.setIcon(QMessageBox.Warning)
        alert.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        return alert
    def validarBoton(opcion):
        if opcion == QMessageBox.Ok:
            return True
        return False
# Ejecutamos la ventana y esperamos a que el usuario presione un botón
    #button_pressed = alert.exec_()


        