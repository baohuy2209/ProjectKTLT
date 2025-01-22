from data_access_layer.UserDAL import UserDAL

user_dal = UserDAL()
list_user = user_dal.get_all_users()
for user in list_user:
    print(user)