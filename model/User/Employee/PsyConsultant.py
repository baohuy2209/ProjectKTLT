from model.User.Employee.Employee import Employee


class PsyConsultant(Employee):
    def __init__(self, userid, name, username, password, email, phone, address, role, position, salary, work_shift, hired_date, year_of_experience, billing_rate, room_id):
        super().__init__(userid, name, username, password, email, phone, address, role, position, salary, work_shift, hired_date)
        self.year_of_experience = year_of_experience
        self.billing_rate = billing_rate
        self.room_id = room_id

    def __str__(self):
        info = f"Information of user: \n +Id: {self.userid} \n +Name: {self.name} \n +Password:{self.password} \n +:Email: {self.email} \n +Phone: {self.phone} \n +Address: {self.address} \n +Role: {self.role} \n +Position: {self.position}  \n +Salary: {self.salary} \n +WorkShift: {self.work_shift} \n +HiredDate: {self.hired_date} \n +N.o Experience: {self.year_of_experience} +Billing rate: {self.billing_rate}"
        return info