import os

from IO.JSONFileFactory import JSONFileFactory
from model.Feedback import Feedback


class FeedbackDAL:
    def __init__(self):
        self.list_feedback = []
        self.json_factory = JSONFileFactory()
    def get_filepath(self, filepath):
        current_dir = os.path.dirname(__file__)
        filepath = os.path.join(current_dir, filepath)
        return str(filepath)
    def get_all_feedback(self):
        filepath = self.get_filepath("../data/feedback.json")
        self.list_feedback = self.json_factory.read_file(filepath, "r")
        list_feedback = []
        for fb in self.list_feedback:
            temp_fb = Feedback(feedback_id=fb["feedback_id"], content=fb["content"], rating=fb["rating"], date=fb["date"], user_id=fb["userid"], room_id=fb["room_id"])
            list_feedback.append(temp_fb)
        self.list_feedback = list_feedback
        return self.list_feedback
    def store_feedback(self, nf):
        filepath = self.get_filepath("../data/feedback.json")
        self.json_factory.write_file(filepath, "w", nf.__dict__)
