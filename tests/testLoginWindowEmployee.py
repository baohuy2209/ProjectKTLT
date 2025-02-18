from PyQt6.QtWidgets import QApplication, QMainWindow

from backend.LoginWindowEmployeeExt import LoginWindowEmployeeExt

app=QApplication([])
myWindow=LoginWindowEmployeeExt()
myWindow.setupUi(QMainWindow())
myWindow.show()
app.exec()