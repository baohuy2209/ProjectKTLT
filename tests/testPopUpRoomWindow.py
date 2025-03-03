from PyQt6.QtWidgets import QApplication, QMainWindow

from backend.PopUpRoomWindowExt import PopUpRoomWindowExt

app=QApplication([])
myWindow= PopUpRoomWindowExt()
myWindow.setupUi(QMainWindow())
myWindow.show()
app.exec()