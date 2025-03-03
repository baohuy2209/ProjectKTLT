from PyQt6.QtWidgets import QApplication, QMainWindow

from backend.FeedBackWindowExt import FeedBackWindowExt

app=QApplication([])
myWindow= FeedBackWindowExt()
myWindow.setupUi(QMainWindow())
myWindow.show()
app.exec()