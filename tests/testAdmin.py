from PyQt6.QtWidgets import QApplication, QMainWindow

from backend.AdminWindowExt import AdminWindowExt

app=QApplication([])
myWindow=AdminWindowExt()
myWindow.setupUi(QMainWindow())
myWindow.show()
app.exec()