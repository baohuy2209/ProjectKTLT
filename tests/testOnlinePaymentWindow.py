from PyQt6.QtWidgets import QApplication, QMainWindow

from backend.OnlinePaymentExt import OnlinePaymentWindowExt

app=QApplication([])
myWindow= OnlinePaymentWindowExt()
myWindow.setupUi(QMainWindow())
myWindow.show()
app.exec()