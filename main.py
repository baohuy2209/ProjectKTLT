from PyQt6.QtWidgets import QApplication, QMainWindow
from backend.LoginWindowExt import LoginWindowExt
if __name__ == "__main__":
    app = QApplication([])
    myWindow = LoginWindowExt()
    myWindow.setupUi(QMainWindow())
    myWindow.show()
    app.exec()
