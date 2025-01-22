<<<<<<< Updated upstream
from PyQt6.QtWidgets import QMainWindow

from ui.LoginWindow.LoginWindow import Ui_MainWindow
=======
from ui.LoginWindow import Ui_MainWindow
>>>>>>> Stashed changes


class LoginWindowExt(Ui_MainWindow):
    def __init__(self):
        pass
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow=MainWindow
    def show(self):
<<<<<<< Updated upstream
        self.MainWindow.show()


=======
        self.MainWindow.show()
>>>>>>> Stashed changes
