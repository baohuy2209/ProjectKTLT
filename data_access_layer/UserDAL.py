from IO.JSONFileFactory import JSONFileFactory
from model.User.User import User


class UserDAL:
    def __init__(self):
        self.list_user = []
    def get_all_users(self):
        json_factory = JSONFileFactory()
        self.list_user = json_factory.read_file("../data/user.json", "r")
        list_user = []
        for user in self.list_user:
            element_user = User(user["userid"], user["name"], user["password"], user["email"], user["phone"], user["address"], user["role"])
            list_user.append(element_user)
        return list_user
    def get_user_by_id(self, userId):
        json_factory = JSONFileFactory()
        self.list_user = json_factory.read_file("../data/user.json", "r")
        for user in self.list_user:
            if (user.userid == userId):
                element_user = User(user["userid"], user["name"], user["password"], user["email"], user["phone"],
                                user["address"], user["role"])
        return element_user