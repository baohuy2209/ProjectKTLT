import traceback
import webbrowser

from PyQt6.QtWidgets import QMessageBox

from constant.constant import phone, email, facebook_link
from data_access_layer.UserDAL import UserDAL
from model.User.Customer.CustomerStandard import CustomerStandard
from model.User.Customer.CustomerTrial import CustomerTrial
from model.User.Customer.CustomerVIP import CustomerVIP
from ui.SignUpWindow import Ui_MainWindow


class SignUpWindowExt(Ui_MainWindow):
    def __init__(self):
        self.user_dal = UserDAL()
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow=MainWindow
        self.setupSignalAndSlots()
    def setupSignalAndSlots(self):
        self.pushButtonGetStarted.clicked.connect(self.sign_up)
        self.pushButtonMail.clicked.connect(self.show_mail)
        self.pushButtonPhone.clicked.connect(self.show_phone)
        self.pushButtonFacebook.clicked.connect(self.show_facebook)
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
    def get_customer_type(self):
        type_customer = ""
        if self.radioButtonStandard.isChecked():
            type_customer = "Standard"
        elif self.radioButtonVip.isChecked():
            type_customer = "Vip"
        elif self.radioButtonTrial.isChecked():
            type_customer = "Trial"
        else:
            type_customer = None
        return type_customer
    def sign_up(self):
        try:
            # The number of current user
            no_user = len(self.user_dal.get_all_users())+1
            new_user_id = "user"+str(no_user)
            name = self.lineEditName.text()
            email_sign_up = self.lineEditLastEmail.text()
            address = self.lineEditAddress.text()
            phone_sign_up = self.lineEditPhone.text()
            username = self.lineEditUserName.text()
            password = self.lineEditPassword.text()
            loyalty_point = 0
            type_customer = self.get_customer_type()
            new_user = None
            match type_customer:
                case "Trial":
                    # The customer has 2 two hours free trial. This is default value
                    trial_time = 2
                    # The services are limited when the customer using the type Trial
                    service_limitation = []
                    trial_customer = CustomerTrial(userid=new_user_id, name=name, username=username, password=password, email=email_sign_up, phone=phone_sign_up, address=address, role="Customer", loyalty_points=loyalty_point, customer_type=type_customer, trial_duration=2, service_limitations=service_limitation)
                    new_user = trial_customer.__dict__
                case "Standard":
                    # The default reward points when standard customer firstly register our service.
                    reward_points = 0
                    # The initial discount rate
                    discount_rate = 0
                    standard_customer = CustomerStandard(userid=new_user_id, name=name, username=username, password=password,email=email_sign_up,phone=phone_sign_up, address=address, role="Customer",
                    loyalty_points=loyalty_point, customer_type=type_customer, reward_points=reward_points, discount_rate=discount_rate)
                    new_user = standard_customer.__dict__
                case "Vip":
                    # The free services which vip will be served
                    free_services = []
                    vip_customer = CustomerVIP(userid=new_user_id, name=name, username=username, password=password,
                                                 email=email_sign_up, phone=phone_sign_up, address=address, role="Customer",loyalty_points=loyalty_point, customer_type=type_customer,
                                                 free_services=free_services)
                    new_user = vip_customer.__dict__
                case _:
                    print("Have some error !!!")
            if new_user != None:
                self.user_dal.sign_up(new_user)
                # The content in QMessageBox
                content = "Sign up successfully !!!"
                # Title
                window_title = "Announcement !!!"
                msg_box = QMessageBox()
                msg_box.setText(content)
                msg_box.setWindowTitle(window_title)
                msg_box.setStandardButtons(QMessageBox.StandardButton.Close)
                button = msg_box.exec()
                if button == QMessageBox.StandardButton.Close:
                    msg_box.close()
                    self.MainWindow.close()
        except:
            traceback.print_exc()
    def show_facebook(self):
        webbrowser.open(facebook_link)
    def show_phone(self):
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