from PyQt6.QtWidgets import QTableWidgetItem, QMessageBox

from data_access_layer.UserDAL import UserDAL
from ui.ChoosePsyConsultant import Ui_MainWindow


class ChoosePsyConsultantExt(Ui_MainWindow):
    def __init__(self):
        self.user_dal = UserDAL()
        self.list_psy = self.user_dal.get_all_psy()
        self.selected_psy = None
        self.room_register = None
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.setupSignalsAndSlot()
        self.show_list_user_gui()
    def show(self):
        self.MainWindow.show()
    def setupSignalsAndSlot(self):
        self.tableWidgetPysConsultant.itemSelectionChanged.connect(self.processSelectedItem)
        self.pushButtonExit.clicked.connect(self.processExit)
        self.pushButtonChoosePsyConsultant.clicked.connect(self.processChoosePsy)
    def show_list_user_gui(self):
        self.tableWidgetPysConsultant.setRowCount(0)
        for user in self.list_psy:
            row = self.tableWidgetPysConsultant.rowCount()
            self.tableWidgetPysConsultant.insertRow(row)
            col_psyid = QTableWidgetItem(user.userid)
            col_name = QTableWidgetItem(user.name)
            col_email = QTableWidgetItem(user.email)
            col_phone = QTableWidgetItem(user.phone)
            col_address = QTableWidgetItem(user.address)
            col_workshift = QTableWidgetItem(user.work_shift)
            col_year_of_experience = QTableWidgetItem(user.year_of_experience)
            col_customer_rate = QTableWidgetItem(str(user.billing_rate))
            self.tableWidgetPysConsultant.setItem(row, 0, col_psyid)
            self.tableWidgetPysConsultant.setItem(row, 1, col_name)
            self.tableWidgetPysConsultant.setItem(row, 2, col_email)
            self.tableWidgetPysConsultant.setItem(row, 3, col_phone)
            self.tableWidgetPysConsultant.setItem(row, 4, col_address)
            self.tableWidgetPysConsultant.setItem(row, 5, col_workshift)
            self.tableWidgetPysConsultant.setItem(row, 6, col_year_of_experience)
            self.tableWidgetPysConsultant.setItem(row, 7, col_customer_rate)
    def processSelectedItem(self):
        row = self.tableWidgetPysConsultant.currentRow()
        if row == -1 or row > len(self.list_psy):
            return
        psy = self.list_psy[row]
        self.selected_psy = psy
        id = psy.userid
        name = psy.name
        email = psy.email
        phone = psy.phone
        address = psy.address
        workshift = psy.work_shift
        year_of_experience = psy.year_of_experience
        customer_rate = str(psy.billing_rate)
        self.lineEditPsyID.setText(id)
        self.lineEditName.setText(name)
        self.lineEditEmail.setText(email)
        self.lineEditPhone.setText(phone)
        self.lineEditAddress.setText(address)
        self.lineEditWorkshift.setText(workshift)
        self.lineEditYearofExperience.setText(str(year_of_experience))
        self.lineEditCustomerRate.setText(str(customer_rate))
    def processExit(self):
        dlg = QMessageBox(self.MainWindow)
        dlg.setWindowTitle("Exit confirmation")
        dlg.setIcon(QMessageBox.Icon.Question)
        dlg.setText("Are you sure to exit?")
        dlg.setStandardButtons(QMessageBox.StandardButton.Yes|
                               QMessageBox.StandardButton.No)
        rs = dlg.exec()
        if rs == QMessageBox.StandardButton.Yes:
            self.MainWindow.close()
    def processChoosePsy(self):
        dlg = QMessageBox(self.MainWindow)
        if self.selected_psy == None:
            dlg.setWindowTitle("Choosing error")
            dlg.setIcon(QMessageBox.Icon.Warning)
            dlg.setText("Can't find this PsyConsultant!")
            dlg.exec()
            return
        dlg.setWindowTitle("Confirmation Choosing")
        dlg.setText("Are you sure to choosing this PsyConsultant?")
        dlg.setStandardButtons(QMessageBox.StandardButton.Yes |
                               QMessageBox.StandardButton.No)
        rs = dlg.exec()
        if rs == QMessageBox.StandardButton.Yes:
            print("hello")