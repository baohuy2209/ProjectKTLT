# Form implementation generated from reading ui file 'C:\Users\ADMIN\PycharmProjects\ProjectKTLT\ui\PriceListWindow.ui'
#
# Created by: PyQt6 UI code generator 6.8.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1218, 859)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 0, 1201, 821))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("C:\\Users\\ADMIN\\PycharmProjects\\ProjectKTLT\\ui\\../assets/image/BẢNG GIÁ.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.pushButtonDatPhongNgay = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButtonDatPhongNgay.setGeometry(QtCore.QRect(390, 690, 431, 81))
        self.pushButtonDatPhongNgay.setStyleSheet("QPushButton {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"}")
        self.pushButtonDatPhongNgay.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:\\Users\\ADMIN\\PycharmProjects\\ProjectKTLT\\ui\\../assets/icons/Đặt phòng ngay.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButtonDatPhongNgay.setIcon(icon)
        self.pushButtonDatPhongNgay.setIconSize(QtCore.QSize(400, 400))
        self.pushButtonDatPhongNgay.setObjectName("pushButtonDatPhongNgay")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(-6, -5, 1231, 821))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("C:\\Users\\ADMIN\\PycharmProjects\\ProjectKTLT\\ui\\../assets/image/PRICE.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.pushButtonHome = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButtonHome.setGeometry(QtCore.QRect(580, 20, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButtonHome.setFont(font)
        self.pushButtonHome.setStyleSheet("QPushButton {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"    color: white;  /* Màu chữ */\n"
"}")
        self.pushButtonHome.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("C:\\Users\\ADMIN\\PycharmProjects\\ProjectKTLT\\ui\\../assets/icons/HOME.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButtonHome.setIcon(icon1)
        self.pushButtonHome.setIconSize(QtCore.QSize(65, 100))
        self.pushButtonHome.setObjectName("pushButtonHome")
        self.pushButtonPlayRoom = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButtonPlayRoom.setGeometry(QtCore.QRect(680, 20, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButtonPlayRoom.setFont(font)
        self.pushButtonPlayRoom.setStyleSheet("QPushButton {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"    color: white;  /* Màu chữ */\n"
"}")
        self.pushButtonPlayRoom.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("C:\\Users\\ADMIN\\PycharmProjects\\ProjectKTLT\\ui\\../assets/icons/PLAY ROOM.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButtonPlayRoom.setIcon(icon2)
        self.pushButtonPlayRoom.setIconSize(QtCore.QSize(120, 100))
        self.pushButtonPlayRoom.setObjectName("pushButtonPlayRoom")
        self.pushButtonOrder = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButtonOrder.setGeometry(QtCore.QRect(840, 20, 81, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButtonOrder.setFont(font)
        self.pushButtonOrder.setStyleSheet("QPushButton {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"    color: white;  /* Màu chữ */\n"
"}")
        self.pushButtonOrder.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("C:\\Users\\ADMIN\\PycharmProjects\\ProjectKTLT\\ui\\../assets/icons/ORDER.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButtonOrder.setIcon(icon3)
        self.pushButtonOrder.setIconSize(QtCore.QSize(75, 100))
        self.pushButtonOrder.setObjectName("pushButtonOrder")
        self.pushButtonPrice = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButtonPrice.setGeometry(QtCore.QRect(940, 20, 81, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButtonPrice.setFont(font)
        self.pushButtonPrice.setStyleSheet("QPushButton {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"    color: white;  /* Màu chữ */\n"
"}")
        self.pushButtonPrice.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("C:\\Users\\ADMIN\\PycharmProjects\\ProjectKTLT\\ui\\../assets/icons/PRICEBOLD.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButtonPrice.setIcon(icon4)
        self.pushButtonPrice.setIconSize(QtCore.QSize(65, 100))
        self.pushButtonPrice.setObjectName("pushButtonPrice")
        self.pushButtonContact = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButtonContact.setGeometry(QtCore.QRect(1040, 20, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButtonContact.setFont(font)
        self.pushButtonContact.setStyleSheet("QPushButton {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"    color: white;  /* Màu chữ */\n"
"}")
        self.pushButtonContact.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("C:\\Users\\ADMIN\\PycharmProjects\\ProjectKTLT\\ui\\../assets/icons/CONTACT.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButtonContact.setIcon(icon5)
        self.pushButtonContact.setIconSize(QtCore.QSize(95, 100))
        self.pushButtonContact.setObjectName("pushButtonContact")
        self.pushButtonMore = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButtonMore.setGeometry(QtCore.QRect(1140, 20, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButtonMore.setFont(font)
        self.pushButtonMore.setStyleSheet("QPushButton {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"    color: white;  /* Màu chữ */\n"
"}")
        self.pushButtonMore.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("C:\\Users\\ADMIN\\PycharmProjects\\ProjectKTLT\\ui\\../assets/icons/3 GẠCH.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButtonMore.setIcon(icon6)
        self.pushButtonMore.setIconSize(QtCore.QSize(50, 70))
        self.pushButtonMore.setObjectName("pushButtonMore")
        self.pushButtonBookingNow = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButtonBookingNow.setGeometry(QtCore.QRect(400, 700, 421, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButtonBookingNow.setFont(font)
        self.pushButtonBookingNow.setStyleSheet("QPushButton {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"    color: white;  /* Màu chữ */\n"
"}")
        self.pushButtonBookingNow.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("C:\\Users\\ADMIN\\PycharmProjects\\ProjectKTLT\\ui\\../assets/icons/BOOKNOW.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButtonBookingNow.setIcon(icon7)
        self.pushButtonBookingNow.setIconSize(QtCore.QSize(400, 400))
        self.pushButtonBookingNow.setObjectName("pushButtonBookingNow")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1218, 26))
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
