# Form implementation generated from reading ui file 'D:\KTLT PROJECT FINAL\ProjectKTLT\ui\ChangePasswordWindow.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1226, 867)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 1221, 811))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("D:\\KTLT PROJECT FINAL\\ProjectKTLT\\ui\\../assets/image/BG CHANGE PASSWORD.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.lineEditCurrentPassword = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEditCurrentPassword.setGeometry(QtCore.QRect(390, 300, 431, 41))
        self.lineEditCurrentPassword.setStyleSheet("QLineEdit {\n"
"    border-radius: 15px;  /* Bo góc 15px */\n"
"    border: 2px solid gray;  /* Viền xám */\n"
"    padding: 5px;  /* Giúp chữ không bị dính vào viền */\n"
"    background-color: white;\n"
"    font-size: 16px;\n"
"}\n"
"")
        self.lineEditCurrentPassword.setObjectName("lineEditCurrentPassword")
        self.lineEditNewPassword = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEditNewPassword.setGeometry(QtCore.QRect(390, 430, 431, 41))
        self.lineEditNewPassword.setStyleSheet("QLineEdit {\n"
"    border-radius: 15px;  /* Bo góc 15px */\n"
"    border: 2px solid gray;  /* Viền xám */\n"
"    padding: 5px;  /* Giúp chữ không bị dính vào viền */\n"
"    background-color: white;\n"
"    font-size: 16px;\n"
"}\n"
"")
        self.lineEditNewPassword.setObjectName("lineEditNewPassword")
        self.lineEditConfirmPassword = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEditConfirmPassword.setGeometry(QtCore.QRect(390, 560, 431, 41))
        self.lineEditConfirmPassword.setStyleSheet("QLineEdit {\n"
"    border-radius: 15px;  /* Bo góc 15px */\n"
"    border: 2px solid gray;  /* Viền xám */\n"
"    padding: 5px;  /* Giúp chữ không bị dính vào viền */\n"
"    background-color: white;\n"
"    font-size: 16px;\n"
"}\n"
"")
        self.lineEditConfirmPassword.setObjectName("lineEditConfirmPassword")
        self.pushButtonSumit = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButtonSumit.setGeometry(QtCore.QRect(390, 640, 421, 61))
        self.pushButtonSumit.setStyleSheet("QPushButton {\n"
"    background-color: rgba(0, 0, 0, 0); /* Nền trong suốt */\n"
"    border: none;  /* Loại bỏ viền */\n"
"    color: white;  /* Màu chữ */\n"
"    font-size: 18px;\n"
"}\n"
"")
        self.pushButtonSumit.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("D:\\KTLT PROJECT FINAL\\ProjectKTLT\\ui\\../assets/icons/Submit.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButtonSumit.setIcon(icon)
        self.pushButtonSumit.setIconSize(QtCore.QSize(400, 2000))
        self.pushButtonSumit.setObjectName("pushButtonSumit")
        self.pushButtonMail = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButtonMail.setGeometry(QtCore.QRect(1100, 500, 101, 81))
        self.pushButtonMail.setStyleSheet("QPushButton {\n"
"    background-color: rgba(0, 0, 0, 0); /* Nền trong suốt */\n"
"    border: none;  /* Loại bỏ viền */\n"
"    color: white;  /* Màu chữ */\n"
"    font-size: 18px;\n"
"}\n"
"")
        self.pushButtonMail.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("D:\\KTLT PROJECT FINAL\\ProjectKTLT\\ui\\../assets/icons/MAIL.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButtonMail.setIcon(icon1)
        self.pushButtonMail.setIconSize(QtCore.QSize(70, 2000))
        self.pushButtonMail.setObjectName("pushButtonMail")
        self.pushButtonPhone = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButtonPhone.setGeometry(QtCore.QRect(1100, 600, 101, 81))
        self.pushButtonPhone.setStyleSheet("QPushButton {\n"
"    background-color: rgba(0, 0, 0, 0); /* Nền trong suốt */\n"
"    border: none;  /* Loại bỏ viền */\n"
"    color: white;  /* Màu chữ */\n"
"    font-size: 18px;\n"
"}\n"
"")
        self.pushButtonPhone.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("D:\\KTLT PROJECT FINAL\\ProjectKTLT\\ui\\../assets/icons/PHONE.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButtonPhone.setIcon(icon2)
        self.pushButtonPhone.setIconSize(QtCore.QSize(70, 2000))
        self.pushButtonPhone.setObjectName("pushButtonPhone")
        self.pushButtonFacebook = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButtonFacebook.setGeometry(QtCore.QRect(1100, 700, 101, 81))
        self.pushButtonFacebook.setStyleSheet("QPushButton {\n"
"    background-color: rgba(0, 0, 0, 0); /* Nền trong suốt */\n"
"    border: none;  /* Loại bỏ viền */\n"
"    color: white;  /* Màu chữ */\n"
"    font-size: 18px;\n"
"}\n"
"")
        self.pushButtonFacebook.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("D:\\KTLT PROJECT FINAL\\ProjectKTLT\\ui\\../assets/icons/facebook-logo.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButtonFacebook.setIcon(icon3)
        self.pushButtonFacebook.setIconSize(QtCore.QSize(70, 2000))
        self.pushButtonFacebook.setObjectName("pushButtonFacebook")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1226, 26))
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
