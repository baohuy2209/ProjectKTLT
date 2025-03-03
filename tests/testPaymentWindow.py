from PyQt6.QtWidgets import QApplication, QMainWindow

from backend.PaymentWindowExt import PaymentWindowExt

app=QApplication([])
myWindow= PaymentWindowExt()
myWindow.setupUi(QMainWindow())
myWindow.show()
app.exec()