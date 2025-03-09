import os
import webbrowser
from PyQt6.QtWidgets import QMessageBox, QMainWindow

from backend.BookingOrderRoomWindowExt import BookingOrderRoomWindowExt
from backend.FeedBackWindowExt import FeedBackWindowExt
from backend.PopUpRoomWindowExt import PopUpRoomWindowExt
from backend.PriceListWindowExt import PriceListWindowExt
from backend.RoomServicesExt import RoomServicesExt
from constant.constant import facebook_link, email, phone
from model.Feedback import Feedback
from model.Room.RoomCatharsis import RoomCatharsis
from model.Room.RoomGenii import RoomGenii
from model.Room.RoomMutiny import RoomMutiny
from model.Room.RoomOasis import RoomOasis
from ui.HomeWindow import Ui_MainWindow


class HomeWindowExt(Ui_MainWindow):
    def __init__(self):
        self.price_window = None
        self.room_service = None
        self.order_window = None
        self.pop_up_window = None
        self.current_user = None
        self.feedback_window = None
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow=MainWindow
        self.setupSignalAndSlot()
    def show(self):
        self.MainWindow.show()
    def setupSignalAndSlot(self):
        self.pushButtonFacebook.clicked.connect(self.process_open_Facebook)
        self.pushButtonMail.clicked.connect(self.process_Mail)
        self.pushButtonPhone.clicked.connect(self.process_Phone)
        self.pushButtonPrice.clicked.connect(self.show_price)
        self.pushButtonPlayRoom.clicked.connect(self.show_service)
        self.pushButtonGenii.clicked.connect(self.show_genii_room)
        self.pushButtonOrder.clicked.connect(self.show_order_window)
        self.pushButtonBookNow.clicked.connect(self.show_order_window)
        self.pushButtonOasis.clicked.connect(self.show_oasis_room)
        self.pushButtonMutiny.clicked.connect(self.show_mutiny_room)
        self.pushButtonCatharsis.clicked.connect(self.show_catharsis_room)
        self.pushButtonContact.clicked.connect(self.show_contact)
        self.pushButtonMore.clicked.connect(self.show_feedback)
    def show_feedback(self):
        FeedbackWindow = QMainWindow()
        self.feedback_window = FeedBackWindowExt()
        self.feedback_window.setupUi(FeedbackWindow)
        self.feedback_window.current_user = self.current_user
        self.feedback_window.show()
    def show_contact(self):
        pass
    def show_order_window(self):
        OrderWindow = QMainWindow()
        self.order_window = BookingOrderRoomWindowExt()
        self.order_window.current_user = self.current_user
        self.order_window.setupUi(OrderWindow)
        self.order_window.show()
    def show_detail_room(self, room):
        DetailRoom = QMainWindow()
        self.pop_up_window = PopUpRoomWindowExt()
        self.pop_up_window.room = room
        self.pop_up_window.setupUi(DetailRoom)
        self.pop_up_window.show()
    def get_image_path(self, path):
        current_dir = os.path.dirname(__file__)
        filepath = os.path.join(current_dir, path)
        return str(filepath)
    def show_oasis_room(self):
        room_id = "oasis1"
        name = "Oasis 1"
        description = "Private, quiet environment, suitable for introverts and gentle."
        picture = self.get_image_path("../assets/image/oasis_room_1.jpg")
        status = "available"
        unit_price = 29000
        room_type = "Oasis"
        journal_customization = True
        oasis_room = RoomOasis(room_id=room_id, name=name, description=description, picture=picture, status=status, unit_price=unit_price, room_type=room_type, journal_customization=journal_customization)
        self.show_detail_room(oasis_room)
    def show_genii_room(self):
        room_id = "genii1"
        name = "Genii 1"
        description = "The environment allows freedom of creativity, turning 'crazy' ideas into reality."
        picture = self.get_image_path("../assets/image/Genii.png")
        status = "available"
        unit_price = 34000
        room_type = "Genii"
        music_instruments = "Guitar, Piano, Drum"
        genii_room = RoomGenii(room_id=room_id, name=name, description=description, picture=picture, status=status,
                               unit_price=unit_price, room_type=room_type, musical_instruments=music_instruments)
        self.show_detail_room(genii_room)
    def show_mutiny_room(self):
        room_id = "mutiny1"
        name = "Mutiny 1"
        description = "An environment where players can experience thrilling games to relieve their frustrations."
        picture = self.get_image_path("../assets/image/Genii.png")
        status = "available"
        unit_price = 32000
        room_type = "Mutiny"
        game_equipment = "VR Headset, Joystick"
        mutiny_room = RoomMutiny(room_id=room_id, name=name, description=description, picture=picture, status=status,
                               unit_price=unit_price, room_type=room_type, game_equipment=game_equipment)
        self.show_detail_room(mutiny_room)
    def show_catharsis_room(self):
        room_id = "catharsis1"
        name = "Catharsis 1"
        description = "Quiet environment with nature sounds and relaxing images helps to soothe the mood and reduce stress."
        picture = self.get_image_path("../assets/image/Catharsis.png")
        status = "available"
        unit_price = 33000
        room_type = "Catharsis"
        natural_sound_effects = ""
        catharsis_room = RoomCatharsis(room_id=room_id, name=name, description=description, picture=picture, status=status,
                                 unit_price=unit_price, room_type=room_type, natural_sound_effects=natural_sound_effects)
        self.show_detail_room(catharsis_room)
    def show_service(self):
        ServiceWindow = QMainWindow()
        self.room_service = RoomServicesExt()
        self.room_service.setupUi(ServiceWindow)
        self.room_service.show()
    def show_price(self):
        PriceWindow = QMainWindow()
        self.price_window = PriceListWindowExt()
        self.price_window.setupUi(PriceWindow)
        self.price_window.show()
    def process_open_Facebook(self):
        webbrowser.open(facebook_link)
    def process_Mail(self):
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Icon.Information)
        msg_box.setText(
            f"Nếu bạn có hỗ trợ trong quá trình sử dụng ứng dụng thì hãy liên hiện chúng tôi thông qua email: {email}\n Chúng tôi xin chân thành cảm ơn.")
        msg_box.setWindowTitle("Contact us")
        msg_box.setStandardButtons(QMessageBox.StandardButton.Close)
        button = msg_box.exec()
        if button == QMessageBox.StandardButton.Close:
            msg_box.close()
    def process_Phone(self):
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Icon.Information)
        msg_box.setText(
            f"Nếu bạn có hỗ trợ trong quá trình sử dụng ứng dụng thì hãy liên hiện chúng tôi thông qua số điện thoại: {phone}\n Chúng tôi xin chân thành cảm ơn.")
        msg_box.setWindowTitle("Contact us")
        msg_box.setStandardButtons(QMessageBox.StandardButton.Close)
        button = msg_box.exec()
        if button == QMessageBox.StandardButton.Close:
            msg_box.close()