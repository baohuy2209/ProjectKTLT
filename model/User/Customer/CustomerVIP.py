from model.User.Customer.Customer import Customer


class CustomerVIP(Customer):
    def __init__(self, userid, name, password, email, phone, address, role, loyalty_points, customer_type, free_services):
        super().__init__(userid, name, password, email, phone, address, role, loyalty_points, customer_type)
        self.free_services = free_services
    def __str__(self):
        info = f"Information of user: \n +Id: {self.userid} \n +Name: {self.name} \n +Password:{self.password} \n +:Email: {self.email} +Phone: {self.phone} +Address: {self.address} +Role: {self.role} +Loyal Points: {self.loyalty_points} +Customer Type: {self.customer_type} \n +Free Services: {self.free_services}"
        return info
