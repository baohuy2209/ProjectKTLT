from PyQt6.QtWidgets import QMainWindow

from ui.LoginWindow.LoginWindow import Ui_MainWindow


class LoginWindowExt(Ui_MainWindow):
    def __init__(self):
        pass
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow=MainWindow
        self.homeWindow = None
        self.setupSignalAndSlot()
    def show(self):
        self.MainWindow.show()
    def setupSignalAndSlot(self):
        self.pushButtonLogin.clicked.connect(self.open_homeWindow)
    def open_homeWindow(self):
        if self.homeWindow==None or self.qmainWindow.isVisible()==False:
            self.qmainWindow = QMainWindow()
            self.homeWindow = self.homeWindow(self)
            self.homeWindow.setupUi(self.qmainWindow)
            self.qmainWindow.show()
