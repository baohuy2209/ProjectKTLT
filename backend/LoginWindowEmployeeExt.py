from PyQt6.QtWidgets import QMessageBox, QMainWindow

from backend.HomeWindowExt import HomeWindowExt
from data_access_layer.UserDAL import UserDAL
from ui.LoginWindowEmployee import Ui_MainWindow


class LoginWindowEmployeeExt(Ui_MainWindow):
    def __init__(self):
        self.user_dal = UserDAL()
        self.home_window = None
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.setupSignalAndSlots()
    def setupSignalAndSlots(self):
        self.pushButtonFacebook.clicked.connect(self.show_facebook_info)
        self.pushButtonMail.clicked.connect(self.show_mail)
        self.pushButtonPhone.clicked.connect(self.show_phonenumber)
        self.pushButtonIForgotMyPassword.clicked.connect(self.show_recover_password)
        self.pushButtonSubmit.clicked.connect(self.login_employee)
    def login_employee(self):
        username = self.lineEditUserName.text()
        password = self.lineEditPassword.text()
        list_user = self.user_dal.get_all_users()
        is_found = False
        login_emp = None
        for user in list_user:
            if user.username == username and user.password==password :
                is_found = True
                login_emp = user
                break
        content = ""
        window_title = ""
        if not is_found or login_emp.role != "Employee":
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
            button = msgBox.exec()
            if button == QMessageBox.StandardButton.Ok:
                HomeWindow = QMainWindow()
                self.home_window = HomeWindowExt()
                self.home_window.current_user = login_emp
                self.home_window.setupUi(HomeWindow)
                self.home_window.show()
    def show_recover_password(self):
        pass
    def show_facebook_info(self):
        pass
    def show_mail(self):
        pass
    def show_phonenumber(self):
        pass
    def show(self):
        self.MainWindow.show()