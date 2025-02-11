from PyQt6.QtWidgets import QApplication, QMainWindow

from backend.ChangePasswordWindowExt import ChangePasswordWindowExt

app=QApplication([])
myWindow= ChangePasswordWindowExt()
myWindow.setupUi(QMainWindow())
myWindow.show()
app.exec()