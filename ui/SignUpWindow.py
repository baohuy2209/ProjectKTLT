# Form implementation generated from reading ui file 'D:\KTLT PROJECT FINAL\ProjectKTLT\ui\SignUpWindow.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1216, 866)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 1211, 831))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("D:\\KTLT PROJECT FINAL\\ProjectKTLT\\ui\\../assets/image/BG SIGN UP.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.pushButtonMail = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButtonMail.setGeometry(QtCore.QRect(1110, 550, 81, 71))
        self.pushButtonMail.setStyleSheet("QPushButton {\n"
"    background-color: rgba(0, 0, 0, 0); /* Nền trong suốt */\n"
"    border: none;  /* Loại bỏ viền */\n"
"    color: white;  /* Màu chữ */\n"
"    font-size: 18px;\n"
"}\n"
"")
        self.pushButtonMail.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("D:\\KTLT PROJECT FINAL\\ProjectKTLT\\ui\\../assets/icons/MAIL.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButtonMail.setIcon(icon)
        self.pushButtonMail.setIconSize(QtCore.QSize(60, 60))
        self.pushButtonMail.setObjectName("pushButtonMail")
        self.pushButtonPhone = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButtonPhone.setGeometry(QtCore.QRect(1110, 640, 81, 71))
        self.pushButtonPhone.setStyleSheet("QPushButton {\n"
"    background-color: rgba(0, 0, 0, 0); /* Nền trong suốt */\n"
"    border: none;  /* Loại bỏ viền */\n"
"    color: white;  /* Màu chữ */\n"
"    font-size: 18px;\n"
"}\n"
"")
        self.pushButtonPhone.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("D:\\KTLT PROJECT FINAL\\ProjectKTLT\\ui\\../assets/icons/PHONE.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButtonPhone.setIcon(icon1)
        self.pushButtonPhone.setIconSize(QtCore.QSize(60, 60))
        self.pushButtonPhone.setObjectName("pushButtonPhone")
        self.pushButtonFacebook = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButtonFacebook.setGeometry(QtCore.QRect(1110, 730, 81, 71))
        self.pushButtonFacebook.setStyleSheet("QPushButton {\n"
"    background-color: rgba(0, 0, 0, 0); /* Nền trong suốt */\n"
"    border: none;  /* Loại bỏ viền */\n"
"    color: white;  /* Màu chữ */\n"
"    font-size: 18px;\n"
"}\n"
"")
        self.pushButtonFacebook.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("D:\\KTLT PROJECT FINAL\\ProjectKTLT\\ui\\../assets/icons/facebook-logo.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButtonFacebook.setIcon(icon2)
        self.pushButtonFacebook.setIconSize(QtCore.QSize(60, 60))
        self.pushButtonFacebook.setObjectName("pushButtonFacebook")
        self.lineEditFirstName = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEditFirstName.setGeometry(QtCore.QRect(320, 280, 251, 41))
        self.lineEditFirstName.setStyleSheet("QLineEdit {\n"
"    border-radius: 15px;  /* Bo góc 15px */\n"
"    border: 2px solid gray;  /* Viền xám */\n"
"    padding: 5px;  /* Giúp chữ không bị dính vào viền */\n"
"    background-color: white;\n"
"    font-size: 16px;\n"
"}\n"
"")
        self.lineEditFirstName.setObjectName("lineEditFirstName")
        self.lineEditLastName = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEditLastName.setGeometry(QtCore.QRect(610, 280, 251, 41))
        self.lineEditLastName.setStyleSheet("QLineEdit {\n"
"    border-radius: 15px;  /* Bo góc 15px */\n"
"    border: 2px solid gray;  /* Viền xám */\n"
"    padding: 5px;  /* Giúp chữ không bị dính vào viền */\n"
"    background-color: white;\n"
"    font-size: 16px;\n"
"}\n"
"")
        self.lineEditLastName.setObjectName("lineEditLastName")
        self.lineEditPhone = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEditPhone.setGeometry(QtCore.QRect(320, 390, 251, 41))
        self.lineEditPhone.setStyleSheet("QLineEdit {\n"
"    border-radius: 15px;  /* Bo góc 15px */\n"
"    border: 2px solid gray;  /* Viền xám */\n"
"    padding: 5px;  /* Giúp chữ không bị dính vào viền */\n"
"    background-color: white;\n"
"    font-size: 16px;\n"
"}\n"
"")
        self.lineEditPhone.setObjectName("lineEditPhone")
        self.lineEditEmail = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEditEmail.setGeometry(QtCore.QRect(610, 390, 251, 41))
        self.lineEditEmail.setStyleSheet("QLineEdit {\n"
"    border-radius: 15px;  /* Bo góc 15px */\n"
"    border: 2px solid gray;  /* Viền xám */\n"
"    padding: 5px;  /* Giúp chữ không bị dính vào viền */\n"
"    background-color: white;\n"
"    font-size: 16px;\n"
"}\n"
"")
        self.lineEditEmail.setObjectName("lineEditEmail")
        self.lineEditUserName = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEditUserName.setGeometry(QtCore.QRect(320, 510, 541, 41))
        self.lineEditUserName.setStyleSheet("QLineEdit {\n"
"    border-radius: 15px;  /* Bo góc 15px */\n"
"    border: 2px solid gray;  /* Viền xám */\n"
"    padding: 5px;  /* Giúp chữ không bị dính vào viền */\n"
"    background-color: white;\n"
"    font-size: 16px;\n"
"}\n"
"")
        self.lineEditUserName.setObjectName("lineEditUserName")
        self.lineEditPassword = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEditPassword.setGeometry(QtCore.QRect(320, 620, 541, 41))
        self.lineEditPassword.setStyleSheet("QLineEdit {\n"
"    border-radius: 15px;  /* Bo góc 15px */\n"
"    border: 2px solid gray;  /* Viền xám */\n"
"    padding: 5px;  /* Giúp chữ không bị dính vào viền */\n"
"    background-color: white;\n"
"    font-size: 16px;\n"
"}\n"
"")
        self.lineEditPassword.setObjectName("lineEditPassword")
        self.pushButtonGetStarted = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButtonGetStarted.setGeometry(QtCore.QRect(390, 730, 411, 61))
        self.pushButtonGetStarted.setStyleSheet("QPushButton {\n"
"    background-color: rgba(0, 0, 0, 0); /* Nền trong suốt */\n"
"    border: none;  /* Loại bỏ viền */\n"
"    color: white;  /* Màu chữ */\n"
"    font-size: 18px;\n"
"}\n"
"")
        self.pushButtonGetStarted.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("D:\\KTLT PROJECT FINAL\\ProjectKTLT\\ui\\../assets/icons/Get Started.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButtonGetStarted.setIcon(icon3)
        self.pushButtonGetStarted.setIconSize(QtCore.QSize(400, 60))
        self.pushButtonGetStarted.setObjectName("pushButtonGetStarted")
        self.checkBoxIAccept = QtWidgets.QCheckBox(parent=self.centralwidget)
        self.checkBoxIAccept.setGeometry(QtCore.QRect(330, 670, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.checkBoxIAccept.setFont(font)
        self.checkBoxIAccept.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("D:\\KTLT PROJECT FINAL\\ProjectKTLT\\ui\\../assets/icons/I accept.jpg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.checkBoxIAccept.setIcon(icon4)
        self.checkBoxIAccept.setIconSize(QtCore.QSize(400, 400))
        self.checkBoxIAccept.setObjectName("checkBoxIAccept")
        self.pushButtonTermsAndConditions = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButtonTermsAndConditions.setGeometry(QtCore.QRect(520, 670, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.pushButtonTermsAndConditions.setFont(font)
        self.pushButtonTermsAndConditions.setStyleSheet("QPushButton {\n"
"    background-color: rgba(0, 0, 0, 0); /* Nền trong suốt */\n"
"    border: none;  /* Loại bỏ viền */\n"
"    font-size: 18px;\n"
"    color: rgb(13, 169, 200);\n"
"}\n"
"")
        self.pushButtonTermsAndConditions.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("D:\\KTLT PROJECT FINAL\\ProjectKTLT\\ui\\../assets/icons/Terms and Conditions.jpg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButtonTermsAndConditions.setIcon(icon5)
        self.pushButtonTermsAndConditions.setIconSize(QtCore.QSize(300, 200))
        self.pushButtonTermsAndConditions.setObjectName("pushButtonTermsAndConditions")
        self.label_4 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(730, 670, 31, 31))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("D:\\KTLT PROJECT FINAL\\ProjectKTLT\\ui\\../assets/icons/and.jpg"))
        self.label_4.setObjectName("label_4")
        self.pushButtonPrivacyStatement = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButtonPrivacyStatement.setGeometry(QtCore.QRect(350, 700, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.pushButtonPrivacyStatement.setFont(font)
        self.pushButtonPrivacyStatement.setStyleSheet("QPushButton {\n"
"    background-color: rgba(0, 0, 0, 0); /* Nền trong suốt */\n"
"    border: none;  /* Loại bỏ viền */\n"
"    font-size: 18px;\n"
"    color: rgb(13, 169, 200);\n"
"}\n"
"")
        self.pushButtonPrivacyStatement.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("D:\\KTLT PROJECT FINAL\\ProjectKTLT\\ui\\../assets/icons/Privacy Statement.jpg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButtonPrivacyStatement.setIcon(icon6)
        self.pushButtonPrivacyStatement.setIconSize(QtCore.QSize(200, 200))
        self.pushButtonPrivacyStatement.setObjectName("pushButtonPrivacyStatement")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1216, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
