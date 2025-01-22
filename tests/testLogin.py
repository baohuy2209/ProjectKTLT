from PyQt6.QtWidgets import QApplication, QMainWindow

from ui.LoginWindow.LoginWindowExt import LoginWindowExt

app=QApplication([])
myWindow=LoginWindowExt()
myWindow.setupUi(QMainWindow())
myWindow.show()
app.exec()