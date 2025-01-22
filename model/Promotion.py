class Promotion:
    def __init__(self, promotion_id, name, discount, conditions, start_date, end_date):
        self.promotion_id = promotion_id
        self.name = name
        self.discount = discount
        self.conditions = conditions
        self.start_date = start_date
        self.end_date = end_date
    def __str__(self):
        info = f"Information: \n +ID: {self.promotion_id} \n +Name: {self.name} \n +Discount: {self.discount} \n +Conditions: {self.conditions} +Start date: {self.start_date} +End date: {self.end_date}"
        return info