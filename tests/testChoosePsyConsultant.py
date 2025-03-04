from PyQt6.QtWidgets import QApplication, QMainWindow

from backend.ChoosePsyConsultantExt import ChoosePsyConsultantExt

app=QApplication([])
myWindow=ChoosePsyConsultantExt()
myWindow.setupUi(QMainWindow())
myWindow.show()
app.exec()