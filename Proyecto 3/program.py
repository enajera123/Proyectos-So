import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication
from controlador.login import LoginView
# from controlador.main import Main
# from controlador.modificar import Modificar
# =======================
# Main
# =======================
app = QApplication(sys.argv)
main = LoginView()
main.show()
sys.exit(app.exec_())
