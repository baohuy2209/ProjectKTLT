class User:
    def __init__(self, username, password, email, phone, address):
        self.username = username
        self.password = password
        self.email = email
        self.phone = phone
        self.address = address
    def __str__(self):
        info = f"Information of user: \n +Username: {self.username} \n +Password: {self.password} \n +Email: {self.email} +Phone: {self.phone} +Address: {self.address}"
        return info
