from PyQt6.QtWidgets import QMainWindow, QMessageBox

from data_access_layer.UserDAL import UserDAL
from ui.LoginWindow import Ui_MainWindow


class LoginWindowExt(Ui_MainWindow):
    def __init__(self):
        self.user_dal = UserDAL()
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow=MainWindow
        self.setupSignalAndSlots()
    def setupSignalAndSlots(self):
        self.pushButtonLogin.clicked.connect(self.login)
    def login(self):
        email = self.lineEditUserName.text()
        password = self.lineEditPassWord.text()
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
        else:
            content = "Login successfully !!!"
            window_title = "Announcement !!!"
        msgBox = QMessageBox()
        msgBox.setText(content)
        msgBox.setWindowTitle(window_title)
        msgBox.exec()
    def show(self):
        self.MainWindow.show()
