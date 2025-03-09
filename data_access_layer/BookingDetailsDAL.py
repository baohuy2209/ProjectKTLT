import os

from IO.JSONFileFactory import JSONFileFactory
from model.BookingDetails import BookingDetails


class BookingDetailsDAL:
    def __init__(self):
        self.list_book_detail = []
        self.json_factory = JSONFileFactory()
    def get_filepath(self, path):
        current_dir = os.path.dirname(__file__)
        filepath = os.path.join(current_dir, path)
        return str(filepath)
    def get_all_booking_detail(self):
        filepath = self.get_filepath("../data/booking_details.json")
        self.list_book_detail = self.json_factory.read_file(filepath, "r")
        list_booking_detail= []
        for bd in self.list_book_detail:
            temp_bd = BookingDetails(booking_details_id=bd["booking_details_id"], booking_id=bd["booking_id"], room_id=bd["room_id"], quantity=bd["quantity"], unit_price=bd["unit_price"], total_price=bd["total_price"])
            list_booking_detail.append(temp_bd)
        self.list_book_detail = list_booking_detail
        return self.list_book_detail
    def booking_detail_order(self, booking_details):
        filepath = self.get_filepath("../data/booking_details.json")
        self.json_factory.write_file(filepath, "w", booking_details.__dict__)