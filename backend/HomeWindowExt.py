from ui.HomeWindow import Ui_MainWindow


class HomeWindowExt(Ui_MainWindow):
    def __init__(self):
        self.current_user = None
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow=MainWindow
    def show(self):
        self.MainWindow.show()