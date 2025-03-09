import random
import traceback

from PyQt6.QtWidgets import QMainWindow, QMessageBox

from backend.ChoosePsyConsultantExt import ChoosePsyConsultantExt
from backend.PaymentWindowExt import PaymentWindowExt
from data_access_layer.BookingDetailsDAL import BookingDetailsDAL
from data_access_layer.BookingOrderDAL import BookingOrderDAL
from data_access_layer.RoomDAL import RoomDAL
from data_access_layer.UserDAL import UserDAL
from model.BookingDetails import BookingDetails
from model.BookingOrder import BookingOrder
from ui.BookingOrderRoomWindow import Ui_MainWindow


class BookingOrderRoomWindowExt(Ui_MainWindow):
    def __init__(self):
        self.choose_psy_window = None
        self.current_user = None
        self.chosen_psy = None
        self.booking_order_dal = BookingOrderDAL()
        self.booking_details_dal = BookingDetailsDAL()
        self.room_dal = RoomDAL()
        self.user_dal = UserDAL()
        self.payment_window = None
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow=MainWindow
        self.setupSignalAndSlots()
    def setupSignalAndSlots(self):
        self.pushButton_4.clicked.connect(self.choose_psy)
        self.pushButtonContinue.clicked.connect(self.order_room)
    def choose_psy(self):
        ChooseWindow = QMainWindow()
        self.choose_psy_window = ChoosePsyConsultantExt()
        self.choose_psy_window.setupUi(ChooseWindow)
        self.choose_psy_window.class_chosen_psy.connect(self.update_psy)
        self.choose_psy_window.show()
    def update_psy(self, psy):
        self.lineEditChoosePsyConsultant.setText(f"{psy.name}")
    def random_multi_number(self, start, end, n):
        return random.sample(range(start, end), n)
    def random_one_number(self, start, end):
        return random.randint(start, end)
    def order_room_general(self, room_type, check_in_date, check_out_date, quantity, psy_name, list_room, list_booking_order, list_bd, list_customer_staff, list_room_manager):
        if quantity < len(list_room):
            second_difference = check_in_date.secsTo(check_out_date)
            hours_difference = round(second_difference/3600,2)
            check_in_date = check_in_date.toString("dd/MM/yyyy HH:mm:ss")
            check_out_date = check_out_date.toString("dd/MM/yyyy HH:mm:ss")
            booking_id = len(list_booking_order) + 1
            customer_id = self.current_user.userid
            emp_css_id = list_customer_staff[self.random_one_number(0, len(list_customer_staff) -1)].userid
            emp_rm_id = list_room_manager[self.random_one_number(0, len(list_room_manager) - 1)].userid
            self.user_dal.assign_customer_service_staff_to_customer(emp_css_id, customer_id)
            promotion_id = ""
            new_booking_order = BookingOrder(booking_id=booking_id, check_in_date=check_in_date,
                                             check_out_date=check_out_date, customer_id=customer_id,
                                             employee_id=emp_css_id, promotion_id=promotion_id)
            self.booking_order_dal.book_room(new_booking_order)
            bd_id = len(list_bd) + 1
            room_id = []
            rd_id = self.random_multi_number(0, len(list_room), quantity)
            for i in rd_id:
                room_id.append(list_room[i].room_id)
                self.room_dal.update_status_room(list_room[i].room_id, "full")
            unit_price = self.room_dal.get_unit_price_by_room_type(room_type)
            total_price = unit_price * quantity * hours_difference
            new_booking_detail = BookingDetails(booking_details_id=bd_id, booking_id=booking_id, room_id=room_id,
                                                quantity=quantity, unit_price=unit_price, total_price=total_price)
            self.user_dal.assign_room_manager_to_customer(emp_rm_id, room_id)
            self.booking_details_dal.booking_detail_order(new_booking_detail)
            if psy_name != "":
                self.user_dal.assign_psy_to_customer(psy_name, room_id)
            match self.current_user.customer_type:
                case "Trial":
                    self.user_dal.update_loyalty_point_user(customer_id, 1)
                case "Standard":
                    self.user_dal.update_loyalty_point_user(customer_id, 2)
                case "Vip":
                    self.user_dal.update_loyalty_point_user(customer_id, 3)
            PaymentWindow = QMainWindow()
            self.payment_window = PaymentWindowExt()
            self.payment_window.setupUi(PaymentWindow)
            self.payment_window.booking_id_payment = booking_id
            self.payment_window.total_price = total_price
            self.payment_window.show()
        else:
            msg = QMessageBox()
            msg.setText("All catharsis room aren't empty")
            msg.setWindowTitle("Announcement")
            msg.setIcon(QMessageBox.Icon.Warning)
            msg.exec()
    def order_room(self):
        try:
            room_type = self.comboBoxRoom.currentText()
            check_in_date = self.dateTimeEditCheckIn.dateTime()
            check_out_date = self.dateTimeEditCheckOut.dateTime()
            quantity = int(self.lineEditQuantity.text())
            psy_name = self.lineEditChoosePsyConsultant.text()
            list_catharsis_room = self.room_dal.check_catharsis_empty()
            list_oasis_room = self.room_dal.check_oasis_empty()
            list_genii_room = self.room_dal.check_genii_empty()
            list_mutiny_room = self.room_dal.check_mutiny_empty()
            list_booking_order = self.booking_order_dal.get_all_booking_order()
            list_bd = self.booking_details_dal.get_all_booking_detail()
            list_customer_staff = self.user_dal.get_customer_service_staff()
            list_room_manager = self.user_dal.get_all_room_manager()
            match room_type:
                case "Catharsis":
                    self.order_room_general(room_type, check_in_date, check_out_date, quantity, psy_name, list_catharsis_room, list_booking_order, list_bd, list_customer_staff, list_room_manager)
                case "Oasis":
                    self.order_room_general(room_type, check_in_date, check_out_date, quantity, psy_name, list_oasis_room, list_booking_order, list_bd, list_customer_staff, list_room_manager)
                case "Genii":
                    self.order_room_general(room_type, check_in_date, check_out_date, quantity, psy_name, list_genii_room, list_booking_order, list_bd, list_customer_staff, list_room_manager)
                case "Mutiny":
                    self.order_room_general(room_type, check_in_date, check_out_date, quantity, psy_name, list_mutiny_room, list_booking_order, list_bd, list_customer_staff, list_room_manager)
        except:
            traceback.print_exc()

    def show(self):
        self.MainWindow.show()