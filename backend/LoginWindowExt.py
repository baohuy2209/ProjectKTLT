from PyQt6.QtWidgets import QMainWindow, QMessageBox

from backend.HomeWindowExt import HomeWindowExt
from data_access_layer.UserDAL import UserDAL
from ui.LoginWindow import Ui_MainWindow


class LoginWindowExt(Ui_MainWindow):
    def __init__(self):
        self.user_dal = UserDAL()
        self.home_window = None
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow=MainWindow
        self.setupSignalAndSlots()
    def setupSignalAndSlots(self):
        self.pushButtonContinue.clicked.connect(self.login)
        self.pushButtonSignUp.clicked.connect(self.signup)
    def signup(self):
        pass
    def login(self):
        email = self.lineEditUserName.text()
        password = self.lineEditPassword.text()
        list_user = self.user_dal.get_all_users()
        print(list_user)
        is_found = False
        for user in list_user:
            if user.email == email and password == user.password:
                is_found = True
        content = ""
        window_title = ""
        if not is_found:
            content = "This account doesn't exist !!!"
            window_title = "Error !!!"
            msgBox = QMessageBox()
            msgBox.setText(content)
            msgBox.setWindowTitle(window_title)
            msgBox.exec()
        else:
            content = "Login successfully !!!"
            window_title = "Announcement !!!"
            msgBox = QMessageBox()
            msgBox.setText(content)
            msgBox.setWindowTitle(window_title)
            msgBox.setStandardButtons(QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.Cancel)
            button=msgBox.exec()
            if button == QMessageBox.StandardButton.Ok:
                HomeWindow = QMainWindow()
                self.home_window = HomeWindowExt()
                self.home_window.setupUi(HomeWindow)
                self.home_window.show()

    def show(self):
        self.MainWindow.show()