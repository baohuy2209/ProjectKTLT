import webbrowser

from PyQt6.QtWidgets import QMessageBox, QMainWindow

from backend.AdminWindowExt import AdminWindowExt
from backend.HomeWindowExt import HomeWindowExt
from constant.constant import facebook_link, phone, email
from data_access_layer.UserDAL import UserDAL
from ui.LoginWindowEmployee import Ui_MainWindow


class LoginWindowEmployeeExt(Ui_MainWindow):
    def __init__(self):
        self.user_dal = UserDAL()
        self.admin_window = None
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
                self.admin_window = AdminWindowExt()
                self.admin_window.current_user = login_emp
                self.admin_window.setupUi(HomeWindow)
                self.admin_window.show()
    def show_recover_password(self):
        pass
    def show_facebook_info(self):
        webbrowser.open(facebook_link)
    def show_mail(self):
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Icon.Information)
        msg_box.setText(
            f"Nếu bạn có hỗ trợ trong quá trình sử dụng ứng dụng thì hãy liên hiện chúng tôi thông qua email: {email}\n Chúng tôi xin chân thành cảm ơn.")
        msg_box.setWindowTitle("Contact us")
        msg_box.setStandardButtons(QMessageBox.StandardButton.Close)
        button = msg_box.exec()
        if button == QMessageBox.StandardButton.Close:
            msg_box.close()
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
    def show(self):
        self.MainWindow.show()