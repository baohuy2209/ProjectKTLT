class User:
    def __init__(self, userid, name=None, password, email, phone=None, address=None, role=None):
        self.userid = userid
        self.name = name
        self.password = password
        self.email = email
        self.phone = phone
        self.address = address
        self.role = role
    def __str__(self):
        info = f"Information of user: \n +Id: {self.userid} \n +Name: {self.name} \n +Password:{self.password} \n +:Email: {self.email} \n +Phone: {self.phone} \n +Address: {self.address} \n +Role: {self.role}"
        return info
