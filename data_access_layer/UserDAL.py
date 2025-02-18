import os


from IO.JSONFileFactory import JSONFileFactory
from model.User.User import User

class UserDAL:
    def __init__(self):
        self.list_user = []
    def get_file_to_read(self, path):
        current_dir = os.path.dirname(__file__)
        filepath = os.path.join(current_dir, path)
        return str(filepath)
    def get_all_users(self):
        json_factory = JSONFileFactory()
        filepath = self.get_file_to_read("../data/user.json")
        self.list_user = json_factory.read_file(filepath, "r")
        list_user = []
        for user in self.list_user:
            element_user = User(user["userid"], user["name"], user["password"], user["email"], user["phone"], user["address"], user["role"])
            list_user.append(element_user)
        return list_user
    def get_user_by_id(self, user_id):
        json_factory = JSONFileFactory()
        filepath = self.get_file_to_read("../data/user.json")
        self.list_user = json_factory.read_file(filepath, "r")
        element_user = None
        for user in self.list_user:
            if user.userid == user_id:
                element_user = User(user["userid"], user["name"], user["password"], user["email"], user["phone"],
                                user["address"], user["role"])
                break
        return element_user