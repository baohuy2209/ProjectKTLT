# Form implementation generated from reading ui file 'C:\Users\ADMIN\PycharmProjects\ProjectKTLT\ui\SignUpWindow.ui'
#
# Created by: PyQt6 UI code generator 6.8.0
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
        self.label.setPixmap(QtGui.QPixmap("C:\\Users\\ADMIN\\PycharmProjects\\ProjectKTLT\\ui\\../assets/image/SIGN UP (NEW).png"))
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
        icon.addPixmap(QtGui.QPixmap("C:\\Users\\ADMIN\\PycharmProjects\\ProjectKTLT\\ui\\../assets/icons/MAIL.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
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
        icon1.addPixmap(QtGui.QPixmap("C:\\Users\\ADMIN\\PycharmProjects\\ProjectKTLT\\ui\\../assets/icons/PHONE.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
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
        icon2.addPixmap(QtGui.QPixmap("C:\\Users\\ADMIN\\PycharmProjects\\ProjectKTLT\\ui\\../assets/icons/facebook-logo.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButtonFacebook.setIcon(icon2)
        self.pushButtonFacebook.setIconSize(QtCore.QSize(60, 60))
        self.pushButtonFacebook.setObjectName("pushButtonFacebook")
        self.lineEditName = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEditName.setGeometry(QtCore.QRect(320, 250, 251, 41))
        self.lineEditName.setStyleSheet("QLineEdit {\n"
"    border-radius: 15px;  /* Bo góc 15px */\n"
"    border: 2px solid gray;  /* Viền xám */\n"
"    padding: 5px;  /* Giúp chữ không bị dính vào viền */\n"
"    background-color: white;\n"
"    font-size: 16px;\n"
"}\n"
"")
        self.lineEditName.setText("")
        self.lineEditName.setObjectName("lineEditName")
        self.lineEditLastEmail = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEditLastEmail.setGeometry(QtCore.QRect(610, 250, 251, 41))
        self.lineEditLastEmail.setStyleSheet("QLineEdit {\n"
"    border-radius: 15px;  /* Bo góc 15px */\n"
"    border: 2px solid gray;  /* Viền xám */\n"
"    padding: 5px;  /* Giúp chữ không bị dính vào viền */\n"
"    background-color: white;\n"
"    font-size: 16px;\n"
"}\n"
"")
        self.lineEditLastEmail.setObjectName("lineEditLastEmail")
        self.lineEditPhone = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEditPhone.setGeometry(QtCore.QRect(320, 350, 251, 41))
        self.lineEditPhone.setStyleSheet("QLineEdit {\n"
"    border-radius: 15px;  /* Bo góc 15px */\n"
"    border: 2px solid gray;  /* Viền xám */\n"
"    padding: 5px;  /* Giúp chữ không bị dính vào viền */\n"
"    background-color: white;\n"
"    font-size: 16px;\n"
"}\n"
"")
        self.lineEditPhone.setObjectName("lineEditPhone")
        self.lineEditAddress = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEditAddress.setGeometry(QtCore.QRect(610, 350, 251, 41))
        self.lineEditAddress.setStyleSheet("QLineEdit {\n"
"    border-radius: 15px;  /* Bo góc 15px */\n"
"    border: 2px solid gray;  /* Viền xám */\n"
"    padding: 5px;  /* Giúp chữ không bị dính vào viền */\n"
"    background-color: white;\n"
"    font-size: 16px;\n"
"}\n"
"")
        self.lineEditAddress.setObjectName("lineEditAddress")
        self.lineEditUserName = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEditUserName.setGeometry(QtCore.QRect(320, 470, 541, 41))
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
        self.lineEditPassword.setGeometry(QtCore.QRect(320, 580, 541, 41))
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
        self.pushButtonGetStarted.setGeometry(QtCore.QRect(390, 740, 411, 61))
        self.pushButtonGetStarted.setStyleSheet("QPushButton {\n"
"    background-color: rgba(0, 0, 0, 0); /* Nền trong suốt */\n"
"    border: none;  /* Loại bỏ viền */\n"
"    color: white;  /* Màu chữ */\n"
"    font-size: 18px;\n"
"}\n"
"")
        self.pushButtonGetStarted.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("C:\\Users\\ADMIN\\PycharmProjects\\ProjectKTLT\\ui\\../assets/icons/Get Started.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButtonGetStarted.setIcon(icon3)
        self.pushButtonGetStarted.setIconSize(QtCore.QSize(400, 60))
        self.pushButtonGetStarted.setObjectName("pushButtonGetStarted")
        self.radioButtonTrial = QtWidgets.QRadioButton(parent=self.centralwidget)
        self.radioButtonTrial.setGeometry(QtCore.QRect(320, 650, 95, 20))
        self.radioButtonTrial.setText("")
        self.radioButtonTrial.setObjectName("radioButtonTrial")
        self.radioButtonStandard = QtWidgets.QRadioButton(parent=self.centralwidget)
        self.radioButtonStandard.setGeometry(QtCore.QRect(390, 650, 95, 20))
        self.radioButtonStandard.setText("")
        self.radioButtonStandard.setObjectName("radioButtonStandard")
        self.radioButtonVip = QtWidgets.QRadioButton(parent=self.centralwidget)
        self.radioButtonVip.setGeometry(QtCore.QRect(510, 650, 95, 20))
        self.radioButtonVip.setText("")
        self.radioButtonVip.setObjectName("radioButtonVip")
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
        self.lineEditName.setPlaceholderText(_translate("MainWindow", "ex: Nguyen Van A"))
        self.lineEditLastEmail.setPlaceholderText(_translate("MainWindow", "ex: huynguyen002311@gmail.com"))
        self.lineEditPhone.setPlaceholderText(_translate("MainWindow", "ex: 0375686583"))
        self.lineEditAddress.setPlaceholderText(_translate("MainWindow", "ex: Binh Dinh"))
        self.lineEditUserName.setPlaceholderText(_translate("MainWindow", "ex: baohuy2209"))
