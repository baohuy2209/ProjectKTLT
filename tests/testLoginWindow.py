from PyQt6.QtWidgets import QApplication, QMainWindow

<<<<<<< Updated upstream:tests/testLogin.py
from ui.LoginWindow.LoginWindowExt import LoginWindowExt
=======
from backend.LoginWindowExt import LoginWindowExt
>>>>>>> Stashed changes:tests/testLoginWindow.py

app=QApplication([])
myWindow=LoginWindowExt()
myWindow.setupUi(QMainWindow())
myWindow.show()
app.exec()