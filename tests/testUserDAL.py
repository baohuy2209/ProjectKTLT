from data_access_layer.UserDAL import UserDAL

user_dal = UserDAL()
# user_dal.assign_psy_to_customer("Lam Thuy Dung", ["catharsis4"])
# user_dal.assign_customer_service_staff_to_customer("user3", "user5")
user_dal.update_loyalty_point_user("user5", 1)