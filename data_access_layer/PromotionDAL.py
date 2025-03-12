import os

from IO.JSONFileFactory import JSONFileFactory
from model.Promotion import Promotion


class PromotionDAL:
    def __init__(self):
        self.list_promotion = []
        self.json_factory = JSONFileFactory()
    def get_filepath(self, path):
        current_dir = os.path.dirname(__file__)
        filepath = os.path.join(current_dir, path)
        return str(filepath)
    def get_all_promotion(self):
        filepath = self.get_filepath("../data/promotion.json")
        self.list_promotion = self.json_factory.read_file(filepath, "r")
        list_promotion = []
        for promotion in self.list_promotion:
            list_promotion.append(Promotion(promotion_id=promotion["promotion_id"], name=promotion["name"], discount=promotion["discount"], conditions=promotion["conditions"], start_date=promotion["start_date"], end_date=promotion["end_date"]))
        self.list_promotion = list_promotion
        return self.list_promotion
    def store_new_promotion(self, new_promotion):
        filepath = self.get_filepath("../data/promotion.json")
        self.json_factory.write_file(filepath, "w", new_promotion.__dict__)