import webbrowser
from PyQt6.QtWidgets import QMessageBox, QMainWindow

from backend.InvoiceWindowExt import InvoiceWindowExt
from ui.DirectPaymentWindow import Ui_MainWindow

class DirectPaymentWindowExt(Ui_MainWindow):
    def __init__(self):
        self.booking_id_payment = 0
        self.total_price = 0
        self.payment_method = ""
        self.invoice_window = None
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow=MainWindow
        self.setupSignalAndSlot()
    def show(self):
        self.lineEditCashier.setText("Phan Hong Ngoc")
        self.lineEditAmountPaid.setText(str(self.total_price))
        self.MainWindow.show()
    def setupSignalAndSlot(self):
        self.pushButtonExit.clicked.connect(self.process_Exit)
        self.pushButtonFacebook.clicked.connect(self.process_open_Facebook)
        self.pushButtonMail.clicked.connect(self.process_Mail)
        self.pushButtonPhone.clicked.connect(self.process_Phone)
        self.pushButtonConfirmPayment.clicked.connect(self.confirm_payment)
    def confirm_payment(self):
        InvoiceWindow = QMainWindow()
        self.invoice_window = InvoiceWindowExt()
        self.invoice_window.setupUi(InvoiceWindow)
        self.invoice_window.booking_id_payment = self.booking_id_payment
        self.invoice_window.total_price = self.total_price
        self.invoice_window.payment_method = self.payment_method
        self.invoice_window.show()
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