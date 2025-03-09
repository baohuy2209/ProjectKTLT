import webbrowser

from PyQt6.QtCore import QDate
from PyQt6.QtWidgets import QMessageBox

from data_access_layer.FeedbackDAL import FeedbackDAL
from model.Feedback import Feedback
from ui.FeedBackWindow import Ui_MainWindow


class FeedBackWindowExt(Ui_MainWindow):
    def __init__(self):
        self.current_user = None
        self.feedback_dal = FeedbackDAL()
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow=MainWindow
        self.setupSignalAndSlot()
    def show(self):
        self.lineEditUserName.setText(self.current_user.name)
        self.dateEditDateRate.setDate(QDate.currentDate())
        self.MainWindow.show()
    def setupSignalAndSlot(self):
        self.pushButtonExit.clicked.connect(self.process_Exit)
        self.pushButtonFacebook.clicked.connect(self.process_open_Facebook)
        self.pushButtonMail.clicked.connect(self.process_Mail)
        self.pushButtonPhone.clicked.connect(self.process_Phone)
        self.pushButtonSendFeedback.clicked.connect(self.feedback)
    def feedback(self):
        list_feedback = self.feedback_dal.get_all_feedback()
        feedback_id = len(list_feedback) + 1
        content = self.textEditContent.toPlainText()
        rating = float(self.lineEditRate.text())
        date = QDate.currentDate().toString("dd/MM/yyyy")
        room_id = self.lineEditIDRoom.text()
        new_feedback = Feedback(feedback_id=feedback_id, content=content, rating=rating, date=date, user_id=self.current_user.userid, room_id=room_id)
        self.feedback_dal.store_feedback(new_feedback)
        self.MainWindow.close()
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