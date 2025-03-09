from ui.AdminWindow import Ui_MainWindow


class AdminWindowExt(Ui_MainWindow):
    def __init__(self):
        self.current_user = None
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.setupSignalAndSlots()
    def setupSignalAndSlots(self):
        pass
    def show(self):
        self.MainWindow.show()
