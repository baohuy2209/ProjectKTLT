import webbrowser
from PyQt6.QtWidgets import QMessageBox, QMainWindow

from backend.DirectPaymentExt import DirectPaymentWindowExt
from backend.OnlinePaymentExt import OnlinePaymentWindowExt
from ui.PaymentWindow import Ui_MainWindow


class PaymentWindowExt(Ui_MainWindow):
    def __init__(self):
        self.dp_window = None
        self.op_window = None
        self.booking_id_payment = 0
        self.total_price = 0
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow=MainWindow
        self.setupSignalAndSlot()
    def show(self):
        self.MainWindow.show()
    def setupSignalAndSlot(self):
        self.pushButtonExit.clicked.connect(self.process_Exit)
        self.pushButtonFacebook.clicked.connect(self.process_open_Facebook)
        self.pushButtonMail.clicked.connect(self.process_Mail)
        self.pushButtonPhone.clicked.connect(self.process_Phone)
        self.pushButtonDirectPayment. clicked.connect(self.direct_payment)
        self.pushButtonOnlinePayment.clicked.connect(self.online_payment)
    def direct_payment(self):
        DPWindow = QMainWindow()
        self.dp_window = DirectPaymentWindowExt()
        self.dp_window.setupUi(DPWindow)
        self.dp_window.booking_id_payment = self.booking_id_payment
        self.dp_window.total_price = self.total_price
        self.dp_window.payment_method = "Cash"
        self.dp_window.show()
        self.MainWindow.close()
    def online_payment(self):
        OPWindow = QMainWindow()
        self.op_window = OnlinePaymentWindowExt()
        self.op_window.setupUi(OPWindow)
        self.op_window.booking_id_payment = self.booking_id_payment
        self.op_window.total_price = self.total_price
        self.op_window.payment_method = "Credit Card"
        self.op_window.show()
        self.MainWindow.close()
    def process_Exit(self):
        dlg = QMessageBox(self.MainWindow)
        dlg.setWindowTitle("Exit Confirmation")
        dlg.setText("Are you sure you want to Exit?")
        dlg.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        dlg.setIcon(QMessageBox.Icon.Question)
        button = dlg.exec()
        button = QMessageBox.StandardButton(button)
        if button == QMessageBox.StandardButton.Yes:
            self.MainWindow.close()
        else:
            pass
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