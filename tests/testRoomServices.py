from PyQt6.QtWidgets import QApplication, QMainWindow

from backend.RoomServicesExt import RoomServicesExt

app=QApplication([])
myWindow= RoomServicesExt()
myWindow.setupUi(QMainWindow())
myWindow.show()
app.exec()