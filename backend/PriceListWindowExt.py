from ui.PriceListWindow import Ui_MainWindow


class PriceListWindowExt(Ui_MainWindow):
    def __init__(self):
        pass
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow=MainWindow
    def show(self):
        self.MainWindow.show()