from model.User.Customer.Customer import Customer


class CustomerStandard(Customer):
    def __init__(self, userid, name, password, email, phone, address, role, loyalty_points, customer_type, reward_points, discount_rate):
        super().__init__(userid, name, password, email, phone, address, role, loyalty_points, customer_type)
        self.reward_points =  reward_points
        self.discount_rate = discount_rate
    def __str__(self):
        info = f"Information of user: \n +Id: {self.userid} \n +Name: {self.name} \n +Password:{self.password} \n +:Email: {self.email} +Phone: {self.phone} +Address: {self.address} +Role: {self.role} +Loyal Points: {self.loyalty_points} +Customer Type: {self.customer_type} \n +Reward Points: {self.reward_points} + \n +Discount rate: {self.discount_rate}"
        return info
