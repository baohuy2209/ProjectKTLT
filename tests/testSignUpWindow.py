from PyQt6.QtWidgets import QApplication, QMainWindow

from backend.SignUpWindowExt import SignUpWindowExt

app=QApplication([])
myWindow=SignUpWindowExt()
myWindow.setupUi(QMainWindow())
myWindow.show()
app.exec()