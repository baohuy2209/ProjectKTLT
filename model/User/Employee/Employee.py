from model.User.User import User


class Employee(User):
    def __init__(self, userid, name=None, password=None, email=None, phone=None, address=None, role=None, position=None, salary=None, work_shift=None, hired_date=None):
        super().__init__(userid, name, password, email, phone, address, role)
        self.position = position
        self.salary = salary
        self.work_shift = work_shift
        self.hired_date = hired_date

    def __str__(self):
        info = f"Information of user: \n +Id: {self.userid} \n +Name: {self.name} \n +Password:{self.password} \n +:Email: {self.email} \n +Phone: {self.phone} \n +Address: {self.address} \n +Role: {self.role} \n +Position: {self.position}  \n +Salary: {self.salary} \n +WorkShift: {self.work_shift} \n +HiredDate: {self.hired_date}"
        return info
