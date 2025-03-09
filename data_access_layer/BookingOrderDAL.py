import os

from IO.JSONFileFactory import JSONFileFactory
from model.BookingOrder import BookingOrder


class BookingOrderDAL:
    def __init__(self):
        self.list_booking_order = []
        self.file_factory = JSONFileFactory()
    def get_filepath(self, path):
        current_dir = os.path.dirname(__file__)
        filepath = os.path.join(current_dir, path)
        return str(filepath)
    def get_all_booking_order(self):
        filepath = self.get_filepath("../data/booking_order.json")
        self.list_booking_order = self.file_factory.read_file(filepath, 'r')
        list_booking_order = []
        for booking_order in self.list_booking_order:
            temp_bo = BookingOrder(booking_id = booking_order["booking_id"], check_in_date=booking_order["check_in_date"], check_out_date=booking_order["check_out_date"], customer_id=booking_order["customer_id"], employee_id=booking_order["employee_id"], promotion_id=booking_order["promotion_id"])
            list_booking_order.append(temp_bo)
        self.list_booking_order = list_booking_order
        return self.list_booking_order
    def book_room(self, booking_order):
        filepath = self.get_filepath("../data/booking_order.json")
        self.file_factory.write_file(filepath, "w", booking_order.__dict__)