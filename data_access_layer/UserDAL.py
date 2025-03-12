import os


from IO.JSONFileFactory import JSONFileFactory
from model.User.Customer.CustomerStandard import CustomerStandard
from model.User.Customer.CustomerTrial import CustomerTrial
from model.User.Customer.CustomerVIP import CustomerVIP
from model.User.Employee.CustomerServiceStaff import CustomerServiceStaff
from model.User.Employee.PsyConsultant import PsyConsultant
from model.User.Employee.RoomManager import RoomManager


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
                                                       customer_type=user["customer_type"], trial_duration=user["trial_duration"],
                                                       service_limitations=user["service_limitations"])
                    case "Standard":
                        element_user = CustomerStandard(userid=user["userid"], name=user["name"], username=user["username"],
                                                             password=user["password"], email=user["email"],
                                                             phone=user["phone"], address=user["address"], role=user["role"],
                                                             loyalty_points=user["loyalty_points"], customer_type=user["customer_type"],
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
        self.list_user = list_user
        return list_user
    def get_all_customer(self):
        list_user = self.get_all_users()
        list_customer = []
        for user in list_user:
            if user.role == "Customer":
                list_customer.append(user)
        return list_customer
    def get_all_emp(self):
        list_user = self.get_all_users()
        list_emp = []
        for user in list_user:
            if user.role == "Employee":
                list_emp.append(user)
        return list_emp
    def get_all_psy(self):
        filepath = self.get_filepath("../data/user.json")
        self.list_user = self.json_factory.read_file(filepath, "r")
        list_psy = []
        for user in self.list_user:
            if user["role"] == "Employee" and user["position"] == "Psychological Consultant":
                list_psy.append(PsyConsultant(userid=user["userid"], name=user["name"],
                                             username=user["username"], password=user["password"],
                                             email=user["email"], phone=user["phone"], address=user["address"],
                                             role=user["role"], position=user["position"],
                                             salary=user["salary"], work_shift=user["work_shift"],
                                             hired_date=user["hired_date"],
                                             year_of_experience=user["year_of_experience"],
                                             billing_rate=user["billing_rate"], room_id=user["room_id"]))
        return list_psy
    def get_all_room_manager(self):
        self.list_user = self.get_all_users()
        list_room_manager = []
        for user in self.list_user:
            if user.role == "Employee" and user.position == "Room Manager":
                list_room_manager.append(user)
        return list_room_manager
    def get_all_trial_customer(self):
        self.list_user = self.get_all_users()
        list_trial_customer = []
        for user in self.list_user:
            if user.role == "Customer" and user.customer_type == "Trial":
                list_trial_customer.append(user)
        return list_trial_customer
    def get_all_standard_customer(self):
        self.list_user = self.get_all_users()
        list_standard_customer = []
        for user in self.list_user:
            if user.role == "Customer" and user.customer_type == "Standard":
                list_standard_customer.append()
        return list_standard_customer
    def get_all_vip_customer(self):
        self.list_user = self.get_all_users()
        list_vip_customer = []
        for user in self.list_user:
            if user.role == "Customer" and user.customer_type == "Vip":
                list_vip_customer.append(user)
        return
    def get_user_by_id(self, user_id):
        temp_user = None
        for user in self.list_user:
            if user == user_id:
                temp_user = user
        return temp_user
    def get_index_user_by_id(self, user_id):
        self.list_user = self.get_all_users()
        temp_index = None
        for i in range(len(self.list_user)):
            if user_id == self.list_user[i].userid:
                temp_index = i
        return temp_index
    def sign_up(self, new_user):
        file_path = self.get_filepath("../data/user.json")
        self.json_factory.write_file(file_path, "w",new_user)
    def update_loyalty_point_user(self, userid ,add_point):
        list_user = self.get_all_users()
        filepath = self.get_filepath("../data/user.json")
        temp_user = None
        for user in list_user:
            if user.userid == userid:
                temp_user = user
                break
        temp_user.loyalty_points += add_point
        ess_user_index = self.get_index_user_by_id(userid)
        self.list_user[ess_user_index] = temp_user
        list_diction = self.to_dictionary(self.list_user)
        self.json_factory.update_file(filepath, list_diction)
    def get_psy_by_id(self, psy_id):
        list_psy = self.get_all_psy()
        temp_psy = None
        for psy in list_psy:
            if psy.userid == psy_id:
                temp_psy = psy
                break
        return temp_psy
    def get_index_psy_by_id(self, psy_id):
        list_user = self.get_all_users()
        temp_index = 0
        for i in range(len(list_user)):
            if list_user[i].userid == psy_id:
                temp_index = i
                break
        return temp_index
    def get_psy_by_name(self, psy_name):
        list_user = self.get_all_psy()
        temp_psy = None
        for psy in list_user:
            if psy.name == psy_name:
                temp_psy = psy
                break
        return temp_psy
    def get_customer_service_staff_by_id(self, id):
        list_user = self.get_customer_service_staff()
        temp_css = None
        for css in list_user:
            if css.userid == id:
                temp_css = css
                break
        return temp_css
    def get_index_customer_service_staff_by_id(self, id):
        list_user = self.get_all_users()
        temp_index = None
        for i in range(len(list_user)):
            if list_user[i].userid == id:
                temp_index = i
                break
        return temp_index
    def get_rm_by_id(self, id):
        list_user = self.get_all_room_manager()
        temp_rm = None
        for rm in list_user:
            if rm.userid == id:
                temp_rm = rm
        return temp_rm
    def get_index_rm_by_id(self, id):
        list_user = self.get_all_users()
        temp_index = None
        for i in range(len(list_user)):
            if id == list_user[i].userid:
                temp_index = i
        return temp_index
    def assign_room_manager_to_customer(self, id, room_id):
        filepath = self.get_filepath("../data/user.json")
        needed_rm = self.get_rm_by_id(id)
        for ri in room_id:
            needed_rm.room_id.append(ri)
        index_rm_update = self.get_index_rm_by_id(needed_rm.userid)
        self.list_user[index_rm_update] = needed_rm
        list_update = self.to_dictionary(self.list_user)
        self.json_factory.update_file(filepath, list_update)
    def assign_customer_service_staff_to_customer(self, emp_id, cust_id):
        filepath = self.get_filepath("../data/user.json")
        css = self.get_customer_service_staff_by_id(emp_id)
        css.customer_id.append(cust_id)
        css_index = self.get_index_customer_service_staff_by_id(emp_id)
        self.list_user[css_index] = css
        list_update = self.to_dictionary(self.list_user)
        self.json_factory.update_file(filepath, list_update)
    def to_dictionary(self, arrData):
        list_dict = []
        for element in arrData:
            list_dict.append(element.__dict__)
        return list_dict
    def assign_psy_to_customer(self, psy_name, room_id):
        filepath = self.get_filepath("../data/user.json")
        needed_psy = self.get_psy_by_name(psy_name)
        for ri in room_id:
            needed_psy.room_id.append(ri)
        index_psy_update = self.get_index_psy_by_id(needed_psy.userid)
        self.list_user[index_psy_update] = needed_psy
        list_update = self.to_dictionary(self.list_user)
        self.json_factory.update_file(filepath, list_update)
    def get_customer_service_staff(self):
        list_user=self.get_all_users()
        self.list_user = list_user
        list_customer_service_staff = []
        for user in list_user:
            if user.role == "Employee" and user.position == "Customer service staff":
                list_customer_service_staff.append(user)
        return list_customer_service_staff
