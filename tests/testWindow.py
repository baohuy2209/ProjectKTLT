from PyQt6.QtWidgets import QApplication, QMainWindow

from backend.TestWindowExt import TestWindowExt

app = QApplication([])
myWindow = TestWindowExt()
MainWindow = QMainWindow()
myWindow.setupUi(MainWindow)
myWindow.show()
app.exec()