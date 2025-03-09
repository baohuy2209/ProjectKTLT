from PyQt6.QtWidgets import QApplication, QMainWindow

from backend.InvoiceWindowExt import InvoiceWindowExt

app = QApplication([])
myWindow = InvoiceWindowExt()
myWindow.setupUi(QMainWindow())
myWindow.show()
app.exec()