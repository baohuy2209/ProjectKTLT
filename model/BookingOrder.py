class BookingOrder:
    def __init__(self, booking_id, check_in_date, check_out_date, customer_id, employee_id, promotion_id):
        self.booking_id = booking_id
        self.check_in_date = check_in_date
        self.check_out_date = check_out_date
        self.customer_id = customer_id
        self.employee_id = employee_id
        self.promotion_id = promotion_id
    def __str__(self):
        info = f"Information: \n +Id: {self.booking_id} \n +Check in date: {self.check_in_date} \n +Check out date: {self.check_out_date} +\n Customer ID: {self.employee_id} \n +Employee ID: {self.customer_id} \n +Promotion ID: {self.promotion_id}"
        return info