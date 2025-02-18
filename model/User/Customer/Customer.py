from model.User.User import User


class Customer(User):
    def __init__(self, userid, name, username, password, email, phone, address, role, loyaltypoints, customertype):
        super().__init__(userid, name, password, username, email, phone, address, role)
        self.loyalty_points = loyaltypoints
        self.customer_type = customertype
    def __str__(self):
        info = f"Information of user: \n +Id: {self.userid} \n +Name: {self.name} \n +Password:{self.password} \n +:Email: {self.email} +Phone: {self.phone} +Address: {self.address} +Role: {self.role} +Loyal Points: {self.loyalty_points} +Customer Type: {self.customer_type}"
        return info
