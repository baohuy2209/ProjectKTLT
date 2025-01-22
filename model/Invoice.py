class Invoice:
    def __init__(self, invoice_id, booking_id, invoice_date, tax_amount, discount_amount, total_payable):
        self.invoice_id = invoice_id
        self.booking_id = booking_id
        self.invoice_date = invoice_date
        self.tax_amount = tax_amount
        self.discount_amount = discount_amount
        self.total_payable = total_payable
    def __str__(self):
        info = f"Information: \n +ID: {self.invoice_id} \n +Booking ID: {self.booking_id} \n +Invoice date: {self.invoice_date} \n +Tax amount: {self.tax_amount} \n +Discount amount: {self.discount_amount} \n +Total payable: {self.total_payable}"
        return info
