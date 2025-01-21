from PyQt6.QtWidgets import QApplication, QMainWindow

from backend.TestWindowExt import TestWindowExt

app = QApplication([])
myWindow = TestWindowExt()
myWindow.setupUi(QMainWindow())
myWindow.show()
app.exec()