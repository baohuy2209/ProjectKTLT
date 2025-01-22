from PyQt6.QtWidgets import QApplication, QMainWindow

<<<<<<< Updated upstream
from backend.TestWindowExt import TestWindowExt
=======
from backend.LoginWindowExt import LoginWindowExt
>>>>>>> Stashed changes

app = QApplication([])
myWindow = TestWindowExt()
myWindow.setupUi(QMainWindow())
myWindow.show()
app.exec()