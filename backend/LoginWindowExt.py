import webbrowser
from PyQt6.QtWidgets import QMessageBox

from ui.LoginWindow import Ui_MainWindow


class LoginWindowExt(Ui_MainWindow):
    def __init__(self):
        pass
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow=MainWindow
        self.setupSignalAndSlot()
    def show(self):
        self.MainWindow.show()
    def setupSignalAndSlot(self):
        self.pushButtonFacebook.clicked.connect(self.process_open_Facebook)
        self.pushButtonMail.clicked.connect(self.process_Mail)
        self.pushButtonPhone.clicked.connect(self.process_Phone)
    def process_open_Facebook(self):
        webbrowser.open('https://www.facebook.com/share/19VBgaQ5s8/')
    def process_Mail(self):
        dlg = QMessageBox(self.MainWindow)
        dlg.setWindowTitle("Email")
        dlg.setText("Panacea@gmail.com")
        button = dlg.exec()
        button = QMessageBox.StandardButton(button)
    def process_Phone(self):
        dlg = QMessageBox(self.MainWindow)
        dlg.setWindowTitle("Phone")
        dlg.setText("09006464")
        button = dlg.exec()
        button = QMessageBox.StandardButton(button)