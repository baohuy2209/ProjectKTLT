import webbrowser
from PyQt6.QtWidgets import QMessageBox

from ui.PopUpRoomWindow import Ui_MainWindow


class PopUpRoomWindowExt(Ui_MainWindow):
    def __init__(self):
        self.room = None
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow=MainWindow
        self.setupSignalAndSlot()
        self.display()
    def show(self):
        self.MainWindow.show()
    def display(self):
        if self.room == None:
            return
        current_room = self.room
        self.lineEditRoomID.setText(str(current_room.room_id))
        self.lineEditRoomName.setText(current_room.name)
        self.textEditDescription.setText(current_room.description)
        self.lineEditUserPrice.setText(str(current_room.unit_price))
        self.lineEditQuantity.setText(str(10))
        self.lineEditUserStatus.setText(str(current_room
                                            .status))
    def setupSignalAndSlot(self):
        self.pushButtonExit.clicked.connect(self.process_Exit)
        self.pushButtonFacebook.clicked.connect(self.process_open_Facebook)
        self.pushButtonMail.clicked.connect(self.process_Mail)
        self.pushButtonPhone.clicked.connect(self.process_Phone)
    def process_Exit(self):
        dlg = QMessageBox(self.MainWindow)
        dlg.setWindowTitle("Exit Confirmation")
        dlg.setText("Are you sure you want to Exit?")
        dlg.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        dlg.setIcon(QMessageBox.Icon.Question)
        button = dlg.exec()
        button = QMessageBox.StandardButton(button)
        if button == QMessageBox.StandardButton.Yes:
            self.MainWindow.close()
        else:
            pass
    def process_open_Facebook(self):
        webbrowser.open('https://www.facebook.com/share/19VBgaQ5s8/')
    def process_Mail(self):
        dlg = QMessageBox(self.MainWindow)
        dlg.setWindowTitle("Email")
        dlg.setText("Panacea@gmail.com")
        button = dlg.exec()
        button = QMessageBox.StandardButton(button)
    def process_Phone(self):
        dlg = QMessageBox(self.MainWindow)
        dlg.setWindowTitle("Phone")
        dlg.setText("09006464")
        button = dlg.exec()
        button = QMessageBox.StandardButton(button)