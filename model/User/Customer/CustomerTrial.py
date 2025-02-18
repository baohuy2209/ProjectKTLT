from model.User.Customer.Customer import Customer


class CustomerTrial(Customer):
    def __init__(self, userid, name, username, password, email, phone, address, role, loyalty_points, customer_type, trial_duration, service_limitations):
        super().__init__(userid, name, username, password, email, phone, address, role, loyalty_points, customer_type)
        self.trial_duration = trial_duration
        self.service_limitations = service_limitations
    def __str__(self):
        info = f"Information of user: \n +Id: {self.userid} \n +Name: {self.name} \n +Password:{self.password} \n +:Email: {self.email} +Phone: {self.phone} +Address: {self.address} +Role: {self.role} +Loyal Points: {self.loyalty_points} +Customer Type: {self.customer_type} \n +Trial duration: {self.trial_duration} + \n +Service Limitations: {self.service_limitations}"
        return info
