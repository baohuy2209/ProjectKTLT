from IO.JSONFileFactory import JSONFileFactory


class InvoiceDAL:
    def __init__(self):
        self.list_invoices = []
        self.json_factory = JSONFileFactory()
    def store_invoices(self, cur_invoice):
        pass