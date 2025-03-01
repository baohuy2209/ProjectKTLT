from PyQt6.QtWidgets import QApplication, QMainWindow

from backend.PriceListWindowExt import PriceListWindowExt

app=QApplication([])
myWindow= PriceListWindowExt()
myWindow.setupUi(QMainWindow())
myWindow.show()
app.exec()