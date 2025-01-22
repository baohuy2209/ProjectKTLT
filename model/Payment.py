class Payment:
    def __init__(self, payment_id, payment_date, payment_amount, payment_method, invoice_id):
        self.payment_id = payment_id
        self.payment_date = payment_date
        self.payment_method = payment_method
        self.invoice_id = invoice_id
        self.payment_amount = payment_amount
    def __str__(self):
        info = f"Information: \n +ID: {self.payment_id} \n +Payment date: {self.payment_date} \n +Payment amount: {self.payment_amount} +Payment method: {self.payment_method} +Invoice ID: {self.invoice_id}"
        return info