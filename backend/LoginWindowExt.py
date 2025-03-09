import webbrowser

from PyQt6.QtWidgets import QMainWindow, QMessageBox

from backend.HomeWindowExt import HomeWindowExt
from backend.LoginWindowEmployeeExt import LoginWindowEmployeeExt
from backend.SignUpWindowExt import SignUpWindowExt
from constant.constant import facebook_link, email, phone
from data_access_layer.UserDAL import UserDAL
from ui.LoginWindow import Ui_MainWindow


class LoginWindowExt(Ui_MainWindow):
    def __init__(self):
        self.user_dal = UserDAL()
        self.home_window = None
        self.sign_up_window = None
        self.login_emp_window = None
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow=MainWindow
        self.setupSignalAndSlots()
    def setupSignalAndSlots(self):
        self.pushButtonContinue.clicked.connect(self.login)
        self.pushButtonSignUp.clicked.connect(self.signup)
        self.pushButtonEmployeeAccount.clicked.connect(self.show_login_emp)
        self.pushButtonFacebook.clicked.connect(self.show_facebook_info)
        self.pushButtonTermsAndConditions.clicked.connect(self.show_term_condition)
        self.pushButtonMail.clicked.connect(self.show_mail)
        self.pushButtonPhone.clicked.connect(self.show_phonenumber)
        self.pushButtonPrivacyStatement.clicked.connect(self.show_privacy_statement)
        self.pushButtonIForgotMyPassword.clicked.connect(self.show_recover_password)
    def show_recover_password(self):
        pass
    def show_privacy_statement(self):
        pass
    def show_phonenumber(self):
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Icon.Information)
        msg_box.setText(
            f"Nếu bạn có hỗ trợ trong quá trình sử dụng ứng dụng thì hãy liên hiện chúng tôi thông qua số điện thoại: {phone}\n Chúng tôi xin chân thành cảm ơn.")
        msg_box.setWindowTitle("Contact us")
        msg_box.setStandardButtons(QMessageBox.StandardButton.Close)
        button = msg_box.exec()
        if button == QMessageBox.StandardButton.Close:
            msg_box.close()
    def show_mail(self):
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Icon.Information)
        msg_box.setText(f"Nếu bạn có hỗ trợ trong quá trình sử dụng ứng dụng thì hãy liên hiện chúng tôi thông qua email: {email}\n Chúng tôi xin chân thành cảm ơn.")
        msg_box.setWindowTitle("Contact us")
        msg_box.setStandardButtons(QMessageBox.StandardButton.Close)
        button = msg_box.exec()
        if button == QMessageBox.StandardButton.Close:
            msg_box.close()
    def show_term_condition(self):
        pass
    def show_facebook_info(self):
        webbrowser.open(facebook_link)
    def show_login_emp(self):
        LoginEmployeeWindow = QMainWindow()
        self.login_emp_window = LoginWindowEmployeeExt()
        self.login_emp_window.setupUi(LoginEmployeeWindow)
        self.login_emp_window.show()
        self.MainWindow.close()
    def signup(self):
        SignUpWindow = QMainWindow()
        self.sign_up_window = SignUpWindowExt()
        self.sign_up_window.setupUi(SignUpWindow)
        self.sign_up_window.show()
    def login(self):
        username = self.lineEditUserName.text()
        password = self.lineEditPassword.text()
        list_user = self.user_dal.get_all_users()
        is_found = False
        login_emp = None
        for user in list_user:
            if user.username == username and password == user.password and user.role=="Customer":
                is_found = True
                login_emp = user
                break
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
                self.home_window.current_user = login_emp
                self.home_window.setupUi(HomeWindow)
                self.home_window.show()
                self.MainWindow.close()
    def show(self):
        self.MainWindow.show()