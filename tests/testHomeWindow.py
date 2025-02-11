from PyQt6.QtWidgets import QApplication, QMainWindow

from backend.HomeWindowExt import HomeWindowExt

app=QApplication([])
myWindow= HomeWindowExt()
myWindow.setupUi(QMainWindow())
myWindow.show()
app.exec()