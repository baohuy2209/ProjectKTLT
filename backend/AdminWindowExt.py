from PyQt6.QtCore import QDate

from data_access_layer.InvoiceDAL import InvoiceDAL
from data_access_layer.PromotionDAL import PromotionDAL
from data_access_layer.RoomDAL import RoomDAL
from data_access_layer.UserDAL import UserDAL
from model.Promotion import Promotion
from model.Room.RoomCatharsis import RoomCatharsis
from model.Room.RoomGenii import RoomGenii
from model.Room.RoomMutiny import RoomMutiny
from model.Room.RoomOasis import RoomOasis
from model.User.Employee.CustomerServiceStaff import CustomerServiceStaff
from model.User.Employee.PsyConsultant import PsyConsultant
from model.User.Employee.RoomManager import RoomManager
from ui.AdminWindow import Ui_MainWindow
from PyQt6.QtWidgets import QMessageBox, QTableWidget, QTableWidgetItem


class AdminWindowExt(Ui_MainWindow):
    def __init__(self):
        self.current_user = None
        self.user_dal = UserDAL()
        self.invoice_dal = InvoiceDAL()
        self.room_dal = RoomDAL()
        self.promotion_dal = PromotionDAL()
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.setupSignalAndSlots()
        self.display_all_employee()
        self.display_all_customer()
        self.display_all_invoice()
        self.is_completed = True
    def setupSignalAndSlots(self):
        self.listWidget_sidebar.itemClicked.connect(self.switch_page_main)
        self.listWidget_invoicelist.itemClicked.connect(self.switch_page_invoice_manager)
        self.listWidget_createinvoice.itemClicked.connect(self.switch_page_createinvoice)
        self.listWidget_listofemployees.itemClicked.connect(self.switch_page_listofemployees)
        self.listWidget_accountregistration.itemClicked.connect(self.switch_page_accountregistration)

        # Khi trang được chuyển sang page_1, page_4, page_5, page_6, các lineEdit sẽ hiển thị giá trị tương ứng
        self.stackedWidget.currentChanged.connect(self.on_page_changed)

        # Cho phép nhấn vào stackedWidget để chuyển trang
        self.stackedWidget.mousePressEvent = self.next_page

        # # Kiểm tra radioButton trước khi nhấn pushButton_createroom
        # self.pushButton_createroom.clicked.connect(self.create_room)

        # Khi nhấn pushButton_cancel_createnewroom, xóa nội dung các lineEdit
        self.pushButton_cancel_createnewroom.clicked.connect(self.clear_room_fields)
        self.pushButton_logout.clicked.connect(self.close_admin_window)
        self.pushButton_signup.clicked.connect(self.create_new_employee)
        self.pushButton_createroom.clicked.connect(self.create_new_room)
        self.pushButton_create.clicked.connect(self.create_promotion)
        self.pushButton_reset.clicked.connect(self.reset_promotion)
    def reset_promotion(self):
        self.lineEdit_discount_2.setText("")
        self.lineEdit_name_2.setText("")
        self.dateEdit_startday.setDate(QDate.currentDate())
        self.dateEdit_enddate.setDate(QDate.currentDate())
        self.textEdit_conditions.setText("")
    def create_promotion(self):
        name_promotion = self.lineEdit_name_2.text()
        discount = float(self.lineEdit_discount_2.text())
        start_day = self.dateEdit_startday.date().toString("dd/MM/yyyy")
        end_day =self.dateEdit_enddate.date().toString("dd/MM/yyyy")
        conditions = self.textEdit_conditions.toPlainText()
        promotion_id = len(self.promotion_dal.get_all_promotion()) + 1
        new_promotion = Promotion(promotion_id=promotion_id, name=name_promotion, discount=discount, conditions=conditions, start_date=start_day, end_date=end_day)
        self.promotion_dal.store_new_promotion(new_promotion)
    def create_new_room(self):
        room_name = self.lineEdit_roomname.text()
        room_type = self.lineEdit_roomtype.text()
        quantity = int(self.lineEdit_capacity.text())
        unit_price = int(self.lineEdit_priceperhour.text())
        status = self.lineEdit_roomstatus.text()
        match room_type:
            case "Catharsis":
                for i in range(quantity):
                    room_id = f"catharsis{len(self.room_dal.get_all_catharsis_room()) + 1}"
                    description = "Quiet environment with nature sounds and relaxing images helps to soothe the mood and reduce stress."
                    picture = ""
                    natural_sound_effects=""
                    room_catharsis = RoomCatharsis(room_id=room_id, name=room_name, description=description, picture=picture, status=status, unit_price=unit_price, room_type=room_type,natural_sound_effects=natural_sound_effects)
                    self.room_dal.store_new_room(room_catharsis)
            case "Oasis":
                for i in range(quantity):
                    room_id = f"oasis{len(self.room_dal.get_all_oasis_room()) + 1}"
                    description = "Private, quiet environment, suitable for introverts and gentle."
                    picture = ""
                    journal_customization = True
                    room_oasis = RoomOasis(room_id=room_id, name=room_name, description=description, picture=picture,status=status, unit_price=unit_price, room_type=room_type, journal_customization=journal_customization)
                    self.room_dal.store_new_room(room_oasis)
            case "Mutiny":
                for i in range(quantity):
                    room_id = f"mutiny{len(self.room_dal.get_all_mutiny_room()) + 1}"
                    description = "An environment where players can experience thrilling games to relieve their frustrations."
                    picture = ""
                    game_equipment = "VR Headset, Joystick"
                    mutiny_room = RoomMutiny(room_id=room_id, name=room_name, description=description, picture=picture, status=status, unit_price=unit_price, room_type="Mutiny", game_equipment=game_equipment)
                    self.room_dal.store_new_room(mutiny_room)
            case "Genii":
                for i in range(quantity):
                    room_id = f"genii{len(self.room_dal.get_all_genii_room()) + 1}"
                    description = "The environment allows freedom of creativity, turning 'crazy' ideas into reality."
                    picture = ""
                    music_instruments = "Guitar, Piano, Drum"
                    mutiny_room = RoomGenii(room_id=room_id, name=room_name, description=description, picture=picture,
                                             status=status, unit_price=unit_price, room_type=room_type,
                                             musical_instruments=music_instruments)
                    self.room_dal.store_new_room(mutiny_room)
        if self.radioButton_approvedbymanager.isChecked():
            QMessageBox.information(None, "Thông báo", "Bạn đã tạo phòng thành công")
        else:
            QMessageBox.warning(None, "Cảnh báo", "Bạn cần được sự chấp thuận từ cấp trên")
    def create_new_employee(self):
        list_user = self.user_dal.get_all_users()
        user_id = f"user{len(list_user) + 1}"
        name = self.lineEdit_name.text()
        phone = self.lineEdit_phone.text()
        username = self.lineEdit_username.text()
        password = self.lineEdit_password.text()
        emp_type = self.comboBox_employeetype.currentText()
        salary = int(self.lineEdit_salary.text())
        email = self.lineEdit_email.text()
        address = self.lineEdit_address.text()
        hire_date = self.lineEdit_hireddate.text()
        work_shift = self.comboBox_workshift.currentText()
        new_emp = None
        match emp_type:
            case "Room Manager":
                new_emp = RoomManager(userid=user_id, name=name, username=username, password=password, email=email, phone=phone, address=address, role="Employee", position="Room Manager", salary=salary, work_shift=work_shift, hired_date=hire_date,room_id=[])
            case "Psychology Consultants":
                new_emp = PsyConsultant(userid=user_id, name=name, username=username, password=password, email=email, phone=phone, address=address, role="Employee", position="Psychological Consultant", salary=salary, work_shift=work_shift, hired_date=hire_date, year_of_experience=1, billing_rate=5, room_id=[])
            case "Customer Staff Service":
                new_emp = CustomerServiceStaff(userid=user_id, name=name, username=username, password=password, email=email, phone=phone, address=address, role="Employee", position="Customer service staff", salary=salary, work_shift=work_shift, hired_date=hire_date, customer_id=[])
        self.user_dal.sign_up(new_emp.__dict__)
        msg = QMessageBox()
        msg.setText("Create New Employee Successfully")
        msg.setWindowTitle("Announcement")
        msg.setStandardButtons(QMessageBox.StandardButton.Close)
        button = msg.exec()
        if button == QMessageBox.StandardButton.Close:
            msg.close()
    def close_admin_window(self):
        self.MainWindow.close()
    def echo_passsword(self, password):
        return "*"*len(password)
    def display_all_invoice(self):
        list_invoice = self.invoice_dal.get_all_invoices()
        self.tableWidget_invoicemanagement.setRowCount(0)
        for i in range(len(list_invoice)):
            self.tableWidget_invoicemanagement.insertRow(i)
            column_id = QTableWidgetItem(str(list_invoice[i].invoice_id))
            column_date = QTableWidgetItem(str(list_invoice[i].invoice_date))
            column_tax_amount = QTableWidgetItem(str(list_invoice[i].tax_amount))
            column_discount_amount = QTableWidgetItem(str(list_invoice[i].discount_amount))
            column_total_payable = QTableWidgetItem(str(list_invoice[i].total_payable))
            self.tableWidget_invoicemanagement.setItem(i, 0, column_id)
            self.tableWidget_invoicemanagement.setItem(i, 1, column_date)
            self.tableWidget_invoicemanagement.setItem(i, 2, column_tax_amount)
            self.tableWidget_invoicemanagement.setItem(i, 3, column_discount_amount)
            self.tableWidget_invoicemanagement.setItem(i, 4, column_total_payable)
    def display_all_customer(self):
        list_customer= self.user_dal.get_all_customer()
        self.tableWidget_customermanagement.setRowCount(0)
        for i in range(len(list_customer)):
            self.tableWidget_customermanagement.insertRow(i)
            column_id = QTableWidgetItem(list_customer[i].userid)
            column_name = QTableWidgetItem(list_customer[i].name)
            column_password = QTableWidgetItem(self.echo_passsword(list_customer[i].password))
            column_email = QTableWidgetItem(list_customer[i].email)
            column_phone = QTableWidgetItem(list_customer[i].phone)
            column_address = QTableWidgetItem(list_customer[i].address)
            column_role = QTableWidgetItem(list_customer[i].role)
            column_loyalty_points = QTableWidgetItem(str(list_customer[i].loyalty_points))
            column_customer_type = QTableWidgetItem(list_customer[i].customer_type)
            self.tableWidget_customermanagement.setItem(i, 0, column_id)
            self.tableWidget_customermanagement.setItem(i, 1, column_name)
            self.tableWidget_customermanagement.setItem(i, 2, column_password)
            self.tableWidget_customermanagement.setItem(i, 3, column_email)
            self.tableWidget_customermanagement.setItem(i, 4, column_phone)
            self.tableWidget_customermanagement.setItem(i, 5, column_address)
            self.tableWidget_customermanagement.setItem(i, 6, column_role)
            self.tableWidget_customermanagement.setItem(i, 7, column_loyalty_points)
            self.tableWidget_customermanagement.setItem(i, 8, column_customer_type)
    def display_all_employee(self):
        list_emp = self.user_dal.get_all_emp()
        self.is_completed = False
        self.tableWidget_listofemployee.setRowCount(0)
        for i in range(len(list_emp)):
            self.tableWidget_listofemployee.insertRow(i)
            column_id = QTableWidgetItem(str(list_emp[i].userid))
            column_name = QTableWidgetItem(list_emp[i].name)
            column_password = QTableWidgetItem(self.echo_passsword(list_emp[i].password))
            column_username = QTableWidgetItem(list_emp[i].username)
            column_email = QTableWidgetItem(list_emp[i].email)
            column_phone = QTableWidgetItem(list_emp[i].phone)
            column_address = QTableWidgetItem(list_emp[i].address)
            column_employee_type = QTableWidgetItem(list_emp[i].position)
            column_hired_date = QTableWidgetItem(list_emp[i].hired_date)
            column_salary = QTableWidgetItem(str(list_emp[i].salary))
            column_work_shift = QTableWidgetItem(list_emp[i].work_shift)
            self.tableWidget_listofemployee.setItem(i, 0, column_id)
            self.tableWidget_listofemployee.setItem(i, 1, column_name)
            self.tableWidget_listofemployee.setItem(i, 2, column_username)
            self.tableWidget_listofemployee.setItem(i, 3, column_password)
            self.tableWidget_listofemployee.setItem(i, 4, column_email)
            self.tableWidget_listofemployee.setItem(i, 5, column_phone)
            self.tableWidget_listofemployee.setItem(i, 6, column_address)
            self.tableWidget_listofemployee.setItem(i, 7, column_employee_type)
            self.tableWidget_listofemployee.setItem(i, 8, column_hired_date)
            self.tableWidget_listofemployee.setItem(i, 9, column_salary)
            self.tableWidget_listofemployee.setItem(i, 10, column_work_shift)
        pass
    def on_page_changed(self, index):
        current_widget = self.stackedWidget.widget(index)
        if current_widget == self.page_1:
            self.populate_room_fields("Mutiny 1", "Mutiny", "1", "32000", "available")
        elif current_widget == self.page_4:
            self.populate_room_fields("Catharsis 1", "Catharsis", "1", "33000", "available")
        elif current_widget == self.page_5:
            self.populate_room_fields("Genii 1", "Genii", "1", "34000", "available")
        elif current_widget == self.page_6:
            self.populate_room_fields("Oasis 1", "Oasis", "1", "29000", "available")

    def next_page(self, event):
        current_index = self.stackedWidget.currentIndex()
        next_index = (current_index + 1) % self.stackedWidget.count()
        self.stackedWidget.setCurrentIndex(next_index)

    def populate_room_fields(self, name, room_type, capacity, price, status):
        self.lineEdit_roomname.setText(name)
        self.lineEdit_roomtype.setText(room_type)
        self.lineEdit_capacity.setText(capacity)
        self.lineEdit_priceperhour.setText(price)
        self.lineEdit_roomstatus.setText(status)

    def clear_room_fields(self):
        self.lineEdit_roomname.clear()
        self.lineEdit_roomtype.clear()
        self.lineEdit_capacity.clear()
        self.lineEdit_priceperhour.clear()
        self.lineEdit_roomstatus.clear()

    def switch_page_listofemployees(self, item):
        text_3 = item.text()
        if text_3 == "List of Employees":
            self.stackedWidget_quanlinhanvien.setCurrentWidget(self.page_listofemployees)

    def switch_page_accountregistration(self, item):
        text_4 = item.text()
        if text_4 == "Account Registration":
            self.stackedWidget_quanlinhanvien.setCurrentWidget(self.page_accountregistration)

    def switch_page_createinvoice(self, item):
        text_2=item.text()
        if text_2 == "CREATE INVOICE":
            self.stackedWidget_3.setCurrentWidget(self.page_2)

    def switch_page_invoice_manager(self, item):
        text_1= item.text()
        if text_1 == "INVOICE LIST":
            self.stackedWidget_3.setCurrentWidget(self.page)

    def switch_page_main(self, item):
        text = item.text()
        if text == "Customer Management":
            self.stackedWidget_main.setCurrentWidget(self.page_customermanagement)
        elif text == "Employee Management":
            self.stackedWidget_main.setCurrentWidget(self.page_employeemanagement)
        elif text == "Invoice Management":
            self.stackedWidget_main.setCurrentWidget(self.page_invoicemanagement)
        elif text == "Create New Room":
            self.stackedWidget_main.setCurrentWidget(self.page_createnewroom)
        elif text == "Create Promotion":
            self.stackedWidget_main.setCurrentWidget(self.page_createpromotion)

    def show(self):
        self.MainWindow.show()
