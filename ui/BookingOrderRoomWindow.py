# Form implementation generated from reading ui file 'C:\Users\ADMIN\PycharmProjects\ProjectKTLT\ui\BookingOrderRoomWindow.ui'
#
# Created by: PyQt6 UI code generator 6.8.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1227, 906)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 1221, 851))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("C:\\Users\\ADMIN\\PycharmProjects\\ProjectKTLT\\ui\\../assets/image/ORDER.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.dateTimeEditCheckIn = QtWidgets.QDateTimeEdit(parent=self.centralwidget)
        self.dateTimeEditCheckIn.setGeometry(QtCore.QRect(720, 330, 391, 41))
        self.dateTimeEditCheckIn.setStyleSheet("QDateTimeEdit {\n"
"    background-color: white;  /* Màu nền trắng */\n"
"    color: #2c3e50; /* Màu chữ xanh đậm */\n"
"    border: 2px solid #3498db; /* Viền xanh */\n"
"    border-radius: 15px; /* Bo góc */\n"
"    padding: 5px;\n"
"    font-size: 25px;\n"
"}\n"
"QDateTimeEdit::drop-down {\n"
"    border: none;\n"
"    background: transparent;\n"
"}\n"
"QDateTimeEdit::up-button, QDateTimeEdit::down-button {\n"
"    width: 20px;\n"
"    height: 20px;\n"
"    border-radius: 10px;\n"
"    background-color: #3498db;\n"
"}\n"
"QDateTimeEdit::up-button:hover, QDateTimeEdit::down-button:hover {\n"
"    background-color: #2980b9;\n"
"}\n"
"")
        self.dateTimeEditCheckIn.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.dateTimeEditCheckIn.setObjectName("dateTimeEditCheckIn")
        self.lineEditTotal = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEditTotal.setGeometry(QtCore.QRect(720, 530, 391, 41))
        self.lineEditTotal.setStyleSheet("QLineEdit {\n"
"    border: 2px solid #3498db;\n"
"    border-radius: 15px;  /* Điều chỉnh giá trị để bo góc nhiều hơn */\n"
"    padding: 5px;\n"
"    font-size: 25px;\n"
"    font-weight:bold;\n"
"}")
        self.lineEditTotal.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lineEditTotal.setObjectName("lineEditTotal")
        self.pushButtonContinue = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButtonContinue.setGeometry(QtCore.QRect(490, 690, 601, 71))
        self.pushButtonContinue.setStyleSheet("QPushButton {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"    color: white; /* Màu chữ */\n"
"    font-size: 16px;\n"
"}\n"
"QPushButton:hover {\n"
"    color: blue; /* Khi hover */\n"
"}\n"
"QPushButton:pressed {\n"
"    color: red; /* Khi nhấn */\n"
"}\n"
"")
        self.pushButtonContinue.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:\\Users\\ADMIN\\PycharmProjects\\ProjectKTLT\\ui\\../assets/icons/Continue.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButtonContinue.setIcon(icon)
        self.pushButtonContinue.setIconSize(QtCore.QSize(600, 500))
        self.pushButtonContinue.setObjectName("pushButtonContinue")
        self.lineEditQuantity = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEditQuantity.setGeometry(QtCore.QRect(720, 470, 391, 41))
        self.lineEditQuantity.setStyleSheet("QLineEdit {\n"
"    border: 2px solid #3498db;\n"
"    border-radius: 15px;  /* Điều chỉnh giá trị để bo góc nhiều hơn */\n"
"    padding: 5px;\n"
"    font-size: 25px;\n"
"    font-weight:bold;\n"
"}")
        self.lineEditQuantity.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lineEditQuantity.setObjectName("lineEditQuantity")
        self.pushButton_4 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(470, 610, 301, 61))
        self.pushButton_4.setStyleSheet("QPushButton {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"    color: white; /* Màu chữ */\n"
"    font-size: 16px;\n"
"}\n"
"QPushButton:hover {\n"
"    color: blue; /* Khi hover */\n"
"}\n"
"QPushButton:pressed {\n"
"    color: red; /* Khi nhấn */\n"
"}\n"
"")
        self.pushButton_4.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("C:\\Users\\ADMIN\\PycharmProjects\\ProjectKTLT\\ui\\../assets/icons/Choose PsyConsultant.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_4.setIcon(icon1)
        self.pushButton_4.setIconSize(QtCore.QSize(300, 500))
        self.pushButton_4.setObjectName("pushButton_4")
        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(450, 320, 231, 51))
        font = QtGui.QFont()
        font.setFamily("VNI-Swiss-Condense")
        font.setPointSize(-1)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("QLabel, QPushButton, QRadioButton {\n"
"    font-family: \"VNI-Swiss-Condense\"; /* Chọn font cố định */\n"
"    font-size: 35px;\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.label_3.setTextFormat(QtCore.Qt.TextFormat.AutoText)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(450, 390, 261, 51))
        font = QtGui.QFont()
        font.setFamily("VNI-Swiss-Condense")
        font.setPointSize(-1)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("QLabel, QPushButton, QRadioButton {\n"
"    font-family: \"VNI-Swiss-Condense\"; /* Chọn font cố định */\n"
"    font-size: 35px;\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.label_4.setTextFormat(QtCore.Qt.TextFormat.AutoText)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(450, 460, 161, 51))
        font = QtGui.QFont()
        font.setFamily("VNI-Swiss-Condense")
        font.setPointSize(-1)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("QLabel, QPushButton, QRadioButton {\n"
"    font-family: \"VNI-Swiss-Condense\"; /* Chọn font cố định */\n"
"    font-size: 35px;\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.label_5.setTextFormat(QtCore.Qt.TextFormat.AutoText)
        self.label_5.setObjectName("label_5")
        self.label_7 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(450, 250, 111, 51))
        font = QtGui.QFont()
        font.setFamily("VNI-Swiss-Condense")
        font.setPointSize(-1)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("QLabel, QPushButton, QRadioButton {\n"
"    font-family: \"VNI-Swiss-Condense\"; /* Chọn font cố định */\n"
"    font-size: 35px;\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.label_7.setTextFormat(QtCore.Qt.TextFormat.AutoText)
        self.label_7.setObjectName("label_7")
        self.comboBoxRoom = QtWidgets.QComboBox(parent=self.centralwidget)
        self.comboBoxRoom.setGeometry(QtCore.QRect(720, 260, 391, 41))
        self.comboBoxRoom.setStyleSheet("QComboBox {\n"
"    background-color: white;  /* Màu nền */\n"
"    color: black;  /* Màu chữ */\n"
"    font-size: 25px;\n"
"    border: 2px solid #3498db; /* Viền xanh */\n"
"    border-radius: 15px; /* Bo góc */\n"
"    padding: 5px;\n"
"}")
        self.comboBoxRoom.setObjectName("comboBoxRoom")
        self.comboBoxRoom.addItem("")
        self.comboBoxRoom.addItem("")
        self.comboBoxRoom.addItem("")
        self.comboBoxRoom.addItem("")
        self.comboBoxRoom.addItem("")
        self.dateTimeEditCheckOut = QtWidgets.QDateTimeEdit(parent=self.centralwidget)
        self.dateTimeEditCheckOut.setGeometry(QtCore.QRect(720, 400, 391, 41))
        self.dateTimeEditCheckOut.setStyleSheet("QDateTimeEdit {\n"
"    background-color: white;  /* Màu nền trắng */\n"
"    color: #2c3e50; /* Màu chữ xanh đậm */\n"
"    border: 2px solid #3498db; /* Viền xanh */\n"
"    border-radius: 15px; /* Bo góc */\n"
"    padding: 5px;\n"
"    font-size: 25px;\n"
"}\n"
"QDateTimeEdit::drop-down {\n"
"    border: none;\n"
"    background: transparent;\n"
"}\n"
"QDateTimeEdit::up-button, QDateTimeEdit::down-button {\n"
"    width: 20px;\n"
"    height: 20px;\n"
"    border-radius: 10px;\n"
"    background-color: #3498db;\n"
"}\n"
"QDateTimeEdit::up-button:hover, QDateTimeEdit::down-button:hover {\n"
"    background-color: #2980b9;\n"
"}\n"
"")
        self.dateTimeEditCheckOut.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.dateTimeEditCheckOut.setObjectName("dateTimeEditCheckOut")
        self.label_6 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(450, 530, 101, 41))
        font = QtGui.QFont()
        font.setFamily("VNI-Swiss-Condense")
        font.setPointSize(-1)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("QLabel, QPushButton, QRadioButton {\n"
"    font-family: \"VNI-Swiss-Condense\"; /* Chọn font cố định */\n"
"    font-size: 35px;\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.label_6.setTextFormat(QtCore.Qt.TextFormat.AutoText)
        self.label_6.setObjectName("label_6")
        self.lineEditChoosePsyConsultant = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEditChoosePsyConsultant.setGeometry(QtCore.QRect(790, 610, 291, 41))
        self.lineEditChoosePsyConsultant.setStyleSheet("QLineEdit {\n"
"    border: 2px solid #3498db;\n"
"    border-radius: 15px;  /* Điều chỉnh giá trị để bo góc nhiều hơn */\n"
"    padding: 5px;\n"
"    font-size: 25px;\n"
"    font-weight:bold;\n"
"}")
        self.lineEditChoosePsyConsultant.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lineEditChoosePsyConsultant.setObjectName("lineEditChoosePsyConsultant")
        self.pushButtonHome = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButtonHome.setGeometry(QtCore.QRect(560, 40, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButtonHome.setFont(font)
        self.pushButtonHome.setStyleSheet("QPushButton {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"    color: white;  /* Màu chữ */\n"
"}")
        self.pushButtonHome.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("C:\\Users\\ADMIN\\PycharmProjects\\ProjectKTLT\\ui\\../assets/icons/HOMEBOLD.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButtonHome.setIcon(icon2)
        self.pushButtonHome.setIconSize(QtCore.QSize(65, 100))
        self.pushButtonHome.setObjectName("pushButtonHome")
        self.pushButtonPlayRoom = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButtonPlayRoom.setGeometry(QtCore.QRect(660, 40, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButtonPlayRoom.setFont(font)
        self.pushButtonPlayRoom.setStyleSheet("QPushButton {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"    color: white;  /* Màu chữ */\n"
"}")
        self.pushButtonPlayRoom.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("C:\\Users\\ADMIN\\PycharmProjects\\ProjectKTLT\\ui\\../assets/icons/PLAY ROOM.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButtonPlayRoom.setIcon(icon3)
        self.pushButtonPlayRoom.setIconSize(QtCore.QSize(120, 100))
        self.pushButtonPlayRoom.setObjectName("pushButtonPlayRoom")
        self.pushButtonOrder = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButtonOrder.setGeometry(QtCore.QRect(830, 40, 81, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButtonOrder.setFont(font)
        self.pushButtonOrder.setStyleSheet("QPushButton {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"    color: white;  /* Màu chữ */\n"
"}")
        self.pushButtonOrder.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("C:\\Users\\ADMIN\\PycharmProjects\\ProjectKTLT\\ui\\../assets/icons/ORDER.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButtonOrder.setIcon(icon4)
        self.pushButtonOrder.setIconSize(QtCore.QSize(75, 100))
        self.pushButtonOrder.setObjectName("pushButtonOrder")
        self.pushButtonPrice = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButtonPrice.setGeometry(QtCore.QRect(940, 40, 81, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButtonPrice.setFont(font)
        self.pushButtonPrice.setStyleSheet("QPushButton {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"    color: white;  /* Màu chữ */\n"
"}")
        self.pushButtonPrice.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("C:\\Users\\ADMIN\\PycharmProjects\\ProjectKTLT\\ui\\../assets/icons/PRICE.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButtonPrice.setIcon(icon5)
        self.pushButtonPrice.setIconSize(QtCore.QSize(65, 100))
        self.pushButtonPrice.setObjectName("pushButtonPrice")
        self.pushButtonContact = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButtonContact.setGeometry(QtCore.QRect(1030, 40, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButtonContact.setFont(font)
        self.pushButtonContact.setStyleSheet("QPushButton {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"    color: white;  /* Màu chữ */\n"
"}")
        self.pushButtonContact.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("C:\\Users\\ADMIN\\PycharmProjects\\ProjectKTLT\\ui\\../assets/icons/CONTACT.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButtonContact.setIcon(icon6)
        self.pushButtonContact.setIconSize(QtCore.QSize(95, 100))
        self.pushButtonContact.setObjectName("pushButtonContact")
        self.pushButtonMore = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButtonMore.setGeometry(QtCore.QRect(1130, 40, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButtonMore.setFont(font)
        self.pushButtonMore.setStyleSheet("QPushButton {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"    color: white;  /* Màu chữ */\n"
"}")
        self.pushButtonMore.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("C:\\Users\\ADMIN\\PycharmProjects\\ProjectKTLT\\ui\\../assets/icons/3 GẠCH.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButtonMore.setIcon(icon7)
        self.pushButtonMore.setIconSize(QtCore.QSize(50, 70))
        self.pushButtonMore.setObjectName("pushButtonMore")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1227, 21))
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
        self.label_3.setText(_translate("MainWindow", "Check-in Time:"))
        self.label_4.setText(_translate("MainWindow", "Check-out Time:"))
        self.label_5.setText(_translate("MainWindow", "Quantity:"))
        self.label_7.setText(_translate("MainWindow", "Room:"))
        self.comboBoxRoom.setItemText(0, _translate("MainWindow", "Select Room"))
        self.comboBoxRoom.setItemText(1, _translate("MainWindow", "Catharsis"))
        self.comboBoxRoom.setItemText(2, _translate("MainWindow", "Oasis"))
        self.comboBoxRoom.setItemText(3, _translate("MainWindow", "Genii"))
        self.comboBoxRoom.setItemText(4, _translate("MainWindow", "Mutiny"))
        self.label_6.setText(_translate("MainWindow", "Total:"))
