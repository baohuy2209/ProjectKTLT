from PyQt6.QtWidgets import QApplication, QMainWindow

from backend.DirectPaymentExt import DirectPaymentWindowExt

app=QApplication([])
myWindow= DirectPaymentWindowExt()
myWindow.setupUi(QMainWindow())
myWindow.show()
app.exec()