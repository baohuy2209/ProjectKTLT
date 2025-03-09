from PyQt6.QtCore import QDate
from PyQt6.QtWidgets import QMessageBox

from data_access_layer.InvoiceDAL import InvoiceDAL
from model.Invoice import Invoice
from ui.InvoiceWindow import Ui_MainWindow


class InvoiceWindowExt(Ui_MainWindow):
    def __init__(self):
        self.booking_id_payment = 0
        self.total_price = 0
        self.payment_method = ""
        self.invoice_dal = InvoiceDAL()
        self.discount_amount = 0
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.setupSignalsAndSlot()
    def show(self):
        self.display_invoice()
        self.MainWindow.show()
    def setupSignalsAndSlot(self):
        self.pushButtonExit.clicked.connect(self.processExit)
        self.pushButtonPay.clicked.connect(self.processPay)
    def processExit(self):
        dlg = QMessageBox(self.MainWindow)
        dlg.setWindowTitle("Exit confirmation")
        dlg.setIcon(QMessageBox.Icon.Question)
        dlg.setText("Are you sure to exit?")
        dlg.setStandardButtons(QMessageBox.StandardButton.Yes|
                               QMessageBox.StandardButton.No)
        rs = dlg.exec()
        if rs == QMessageBox.StandardButton.Yes:
            self.MainWindow.close()
    def processPay(self):
        invoice_id = int(self.lineEditInvoiceID.text())
        booking_id = int(self.lineBookingID.text())
        invoice_date = self.dateEditInvoiceDate.date().toString("dd/MM/yyyy")
        tax_amount = float(self.lineTaxAmount.text())
        discount_amount = float(self.lineDiscountAmount.text())
        total_payable = float(self.lineTotalPayable.text())
        invoice = Invoice(invoice_id=invoice_id, booking_id=booking_id, invoice_date=invoice_date, tax_amount=tax_amount, discount_amount=discount_amount, total_payable=total_payable)
        self.invoice_dal.store_invoices(invoice)
        self.MainWindow.close()
    def display_invoice(self):
        list_invoice = self.invoice_dal.get_all_invoices()
        invoice_id = len(list_invoice) + 1
        tax_amount = 0
        if self.discount_amount != 0:
            total_payable = (self.total_price - tax_amount)*(1-self.discount_amount)
        else:
            total_payable = self.total_price - tax_amount
        self.lineEditInvoiceID.setText(str(invoice_id))
        self.linePaymentAmount.setText(str(self.total_price))
        self.lineTaxAmount.setText(str(tax_amount))
        self.lineDiscountAmount.setText(str(self.discount_amount))
        self.lineBookingID.setText(str(self.booking_id_payment))
        self.lineTotalPayable.setText(str(total_payable))
        self.comboBoxPaymentMethod.setCurrentText(str(self.payment_method))
        self.dateEditInvoiceDate.setDate(QDate.currentDate())
