from PyQt6.QtWidgets import QApplication, QMainWindow

from backend.AdminWindowExt import AdminWindowExt
from assets.image import Images_rc
from assets import icons_rc

app=QApplication([])
myWindow=AdminWindowExt()
myWindow.setupUi(QMainWindow())
myWindow.show()
app.exec()