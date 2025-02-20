import os

from Demos.win32ts_logoff_disconnected import username

from IO.JSONFileFactory import JSONFileFactory
from model.User.Customer.CustomerStandard import CustomerStandard
from model.User.Customer.CustomerTrial import CustomerTrial
from model.User.Customer.CustomerVIP import CustomerVIP
from model.User.Employee.CustomerServiceStaff import CustomerServiceStaff
from model.User.Employee.PsyConsultant import PsyConsultant
from model.User.Employee.RoomManager import RoomManager
from model.User.User import User


class UserDAL:
    def __init__(self):
        self.list_user = []
        self.json_factory = JSONFileFactory()
    def get_filepath(self, path):
        current_dir = os.path.dirname(__file__)
        filepath = os.path.join(current_dir, path)
        return str(filepath)
    def get_all_users(self):
        filepath = self.get_filepath("../data/user.json")
        self.list_user = self.json_factory.read_file(filepath, "r")
        list_user = []
        for user in self.list_user:
            element_user = ""
            if user["role"] == "Customer":
                match user["customer_type"]:
                    case "Trial":
                        element_user = CustomerTrial(userid=user["userid"], name=user["name"], username=user["username"],
                                                       password=user["password"], email=user["email"], phone=user["phone"],
                                                       address=user["address"], role=user["role"], loyalty_points=user["loyalty_points"],
                                                       customer_type=user["customer_type"], trial_duration=["trial_duration"],
                                                       service_limitations=user["service_limitations"])
                    case "Standard":
                        element_user = CustomerStandard(userid=user["userid"], name=user["name"], username=user["username"],
                                                             password=user["password"], email=user["email"],
                                                             phone=user["phone"], address=user["address"], role=user["role"],
                                                             loyalty_points=["loyalty_points"], customer_type=user["customer_type"],
                                                             reward_points=user["reward_points"], discount_rate=user["discount_rate"])
                    case "Vip":
                        element_user = CustomerVIP(userid=user["userid"], name=user["name"], username=user["username"], password=user["password"],
                                                   email=user["email"], phone=user["phone"], address=user["address"],
                                                   role=user["role"], loyalty_points=user["loyalty_points"],
                                                   customer_type=user["customer_type"],
                                                   free_services=user["free_services"])
                    case _:
                        print("Have some error !!!")
            else:
                match user["position"]:
                    case "Room Manager":
                        element_user = RoomManager(userid=user["userid"], name=user["name"], username=user["username"], password=user["password"], email=user["email"], phone=user["phone"], address=user["address"], role=user["role"], position=user["position"], salary=user["salary"], work_shift=user["work_shift"], hired_date=user["hired_date"], room_id=user["room_id"])
                    case "Psychological Consultant":
                        element_user = PsyConsultant(userid=user["userid"], name=user["name"], username=user["username"], password=user["password"], email=user["email"], phone=user["phone"], address=user["address"], role=user["role"], position=user["position"], salary=user["salary"], work_shift=user["work_shift"], hired_date=user["hired_date"], year_of_experience=user["year_of_experience"], billing_rate=user["billing_rate"], room_id=user["room_id"])
                    case "Customer service staff":
                        element_user = CustomerServiceStaff(userid=user["userid"], name=user["name"], username=user["username"], password=user["password"], email=user["email"], phone=user["phone"], address=user["address"], role=user["role"], position=user["position"], salary=user["salary"], work_shift=user["work_shift"], hired_date=user["hired_date"], customer_id=user["customer_id"])
            list_user.append(element_user)
        return list_user
    def get_user_by_id(self, user_id):
        filepath = self.get_filepath("../data/user.json")
        self.list_user = self.json_factory.read_file(filepath, "r")
        element_user = None
        for user in self.list_user:
            if user.userid == user_id:
                element_user = User(user["userid"], user["name"], user["password"], user["email"], user["phone"],
                                user["address"], user["role"])
                break
        return element_user
    def sign_up(self, new_user):
        file_path = self.get_filepath("../data/user.json")
        self.json_factory.write_file(file_path, "w",new_user)