from IO.JSONFileFactory import JSONFileFactory


class Invoice_test:
    def __init__(self, invoice_id, booking_id, invoice_date, payment_amount, discount_amount, total_payable, payment_method, tax_amount=None):
        self.invoice_id = invoice_id
        self.booking_id = booking_id
        self.invoice_date = invoice_date
        self.payment_amount = payment_amount
        self.tax_amount = self.payment_amount*0.1
        self.discount_amount = discount_amount
        self.total_payable = total_payable
        self.payment_method = payment_method
    def __str__(self):
        info = f"Information: \n +ID: {self.invoice_id} \n +Booking ID: {self.booking_id} \n +Invoice date: {self.invoice_date} \n +Payment amount: {self.payment_amount} \n +Tax amount: {self.tax_amount} \n +Discount amount: {self.discount_amount} \n +Total payable: {self.total_payable} \n +Payment method: {self.payment_method}"
        return info

invoice = Invoice_test(
    invoice_id="invoice1",
    booking_id="booking1",
    invoice_date= "12/2/2025",
    payment_amount=1000,
    discount_amount=50,
    total_payable=1050,
    payment_method="Credit Card")


invoice_data = {
    "invoice_id": invoice.invoice_id,
    "booking_id": invoice.booking_id,
    "invoice_date": invoice.invoice_date,
    "payment_amount": invoice.payment_amount,
    "tax_amount": invoice.tax_amount,
    "discount_amount": invoice.discount_amount,
    "total_payable": invoice.total_payable,
    "payment_method": invoice.payment_method
}

json_factory = JSONFileFactory()
json_factory.write_file("../data/invoices.json", "w", invoice_data)