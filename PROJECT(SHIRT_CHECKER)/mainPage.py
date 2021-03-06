import sys
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QMessageBox
import BLL
import signUpPage
import customerPage

class mainPage(QtWidgets.QMainWindow):
    def __init__(self):
        super(mainPage, self).__init__()
        loadUi("mainPage.ui", self)
        self.show()

        self.pushButton_viewAll.clicked.connect(self.viewAllButton_clicked)
        self.pushButton_addCustomer.clicked.connect(self.addCustomerButton_clicked)
        self.pushButton_delete.clicked.connect(self.deleteCustomerButton_clicked)
        self.pushButton_addAccount.clicked.connect(self.addAccountButton_clicked)


    def viewAllButton_clicked(self):
        self.tableWidget_main.setRowCount(0)
        self.tableWidget_main.setColumnCount(9)
        allCustomer = BLL.customer.viewCustomer()
        for row_number, user in enumerate(allCustomer):
            self.tableWidget_main.insertRow(row_number)
            for column_number, data in enumerate(user):
                cell = QtWidgets.QTableWidgetItem(str(data))
                self.tableWidget_main.setItem(row_number,column_number,cell)

    def addCustomerButton_clicked(self):
        self.newWindow = customerPage.customerPage()
        self.close()
        self.newWindow.show()

    def addAccountButton_clicked(self):
        self.newWindow = signUpPage.signUp()
        self.close()
        self.newWindow.show()

    def deleteCustomerButton_clicked(self):
        print(BLL.customer.deleteCustomer(self.tableWidget_main.currentRow()))


#########################################################################################################################################
