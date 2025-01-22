from IO.JSONFileFactory import JSONFileFactory

jsonfile = JSONFileFactory()
datas = jsonfile.read_file("../data/user.json", "r")
for data in datas:
    print(dict(data))
new_data = {
    "userid": "user3",
    "name": "Dang Ngoc Hoai Phuong",
    "password": "123456",
    "email": "dangngochoaiphuong@gmail.com",
    "phone": "0343545635",
    "address": "Phu Yen",
    "role": "Employee",
    "position": "Customer service staff",
    "salary": 20000,
    "work_shift": "Thursday, Saturday, Sunday",
    "hired_date": "2025/02/10",
    "customer_id": "cust1"
}
jsonfile.write_file("../data/user.json", "w", new_data)
current_data = jsonfile.read_file("../data/user.json", "r")
