from PyQt6.QtWidgets import QMessageBox

from data_access_layer.InvoiceDAL import InvoiceDAL
from ui.InvoiceWindow import Ui_MainWindow


class InvoiceWindowExt(Ui_MainWindow):
    def __init__(self):
        self.invoice = None
        self.invoice_dal = InvoiceDAL()
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.setupSignalsAndSlot()
        self.display_invoice()
    def show(self):
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
        if self.invoice==None:
            return
        self.invoice_dal.store_invoices(self.invoice)

    def display_invoice(self):
        if self.invoice==None:
            return
        self.lineEditInvoiceID.setText(self.invoice.invoice_id)
