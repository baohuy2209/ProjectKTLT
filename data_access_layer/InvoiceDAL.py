import os

from IO.JSONFileFactory import JSONFileFactory
from model.Invoice import Invoice


class InvoiceDAL:
    def __init__(self):
        self.list_invoices = []
        self.json_factory = JSONFileFactory()
    def get_filepath(self, filepath):
        current_dir = os.path.dirname(__file__)
        filepath = os.path.join(current_dir, filepath)
        return str(filepath)
    def get_all_invoices(self):
        filepath = self.get_filepath("../data/invoices.json")
        self.list_invoices = self.json_factory.read_file(filepath, "r")
        list_invoices = []
        for invoice in self.list_invoices:
            temp_invoice = Invoice(invoice_id=invoice["invoice_id"], booking_id=invoice["booking_id"], invoice_date=invoice["invoice_date"], tax_amount=invoice["tax_amount"], discount_amount=invoice["discount_amount"], total_payable=invoice["total_payable"])
            list_invoices.append(temp_invoice)
        self.list_invoices = list_invoices
        return self.list_invoices
    def store_invoices(self, cur_invoice):
        filepath = self.get_filepath("../data/invoices.json")
        self.json_factory.write_file(filepath, "w", cur_invoice.__dict__)