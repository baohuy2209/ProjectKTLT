# Form implementation generated from reading ui file 'C:\Users\ADMIN\PycharmProjects\ProjectKTLT\ui\RoomServices.ui'
#
# Created by: PyQt6 UI code generator 6.8.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1063, 614)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 1051, 561))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("C:\\Users\\ADMIN\\PycharmProjects\\ProjectKTLT\\ui\\../assets/image/BG Home Window.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(parent=self.centralwidget)
        self.plainTextEdit.setEnabled(False)
        self.plainTextEdit.setGeometry(QtCore.QRect(60, 150, 931, 371))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.plainTextEdit.sizePolicy().hasHeightForWidth())
        self.plainTextEdit.setSizePolicy(sizePolicy)
        self.plainTextEdit.setStyleSheet("font-size: 13pt;\n"
"font-family: \"#9Slide03 Oswald\";\n"
"color: white;\n"
"background-color: rgba(255, 255, 255, 25);\n"
"border: 0.5px solid white;\n"
"border-radius: 7px;")
        self.plainTextEdit.setObjectName("plainTextEdit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1063, 25))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Panacea - Room Services"))
        self.plainTextEdit.setPlainText(_translate("MainWindow", "     Panacea – Vũ trụ giải trí mang đến cho khách hàng một loạt các dịch vụ độc đáo và sáng tạo, được thiết kế để giải tỏa căng thẳng và nâng cao sức khỏe tinh thần. Dưới đây là một số dịch vụ nổi tiếng tại Panacea: \n"
"    • Thiền định và Yoga: Dưới sự hướng dẫn tận tình từ các giáo viên chuyên nghiệp và công nghệ hỗ trợ hiện đại, bạn sẽ được trải nghiệm những phút giây hoàn toàn thư thái, tạm rời xa những áp lực công việc và cuộc sống. \n"
"     • Vẽ tranh: Nếu bạn là người yêu thích sự sáng tạo và muốn thỏa sức bộc lộ bản thân, Panacea chính là nơi dành cho bạn. Tại đây, bạn có thể thử sức với các hoạt động vẽ tranh, tạo ra những giai điệu âm nhạc riêng của mình, hoặc đơn giản là để cảm xúc dẫn lối.\n"
"     • Trò chơi giải trí: Tại Panacea, bạn sẽ được trải nghiệm những trò chơi cảm giác mạnh như bắn súng, ném rìu hay tham gia các trò chơi điện tử hấp dẫn. Hãy đến và thỏa sức thể hiện bản lĩnh, để mỗi phút giây vui chơi đều trở thành những khoảnh khắc giải tỏa căng thẳng tuyệt vời.\n"
"     • Tư vấn tâm lý: Cuộc sống bận rộn khiến chúng ta ít khi dành thời gian để lắng nghe chính mình. Dịch vụ Tư vấn tâm lý tại Panacea sẽ giúp bạn tìm lại sự tĩnh lặng trong tâm hồn. Dưới sự hỗ trợ chuyên nghiệp và tận tâm của các chuyên gia tâm lý, bạn sẽ được chia sẻ những lo âu, stress mà mình đang gặp phải. \n"
"     Hãy đến với Panacea, nơi không chỉ là dịch vụ giải trí, mà còn là hành trình tìm lại sự bình yên, sự sáng tạo và sự kết nối sâu sắc với chính mình!"))
