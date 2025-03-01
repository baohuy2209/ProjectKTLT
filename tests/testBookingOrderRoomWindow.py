from PyQt6.QtWidgets import QApplication, QMainWindow

from backend.BookingOrderRoomWindowExt import BookingOrderRoomWindowExt

app=QApplication([])
myWindow= BookingOrderRoomWindowExt()
myWindow.setupUi(QMainWindow())
myWindow.show()
app.exec()