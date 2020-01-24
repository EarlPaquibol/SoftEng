import sys
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QMessageBox
import BLL
import mainPage

class customerPage(QtWidgets.QMainWindow):
    def __init__(self):
        super(customerPage, self).__init__()
        loadUi("customerPage.ui", self)
        self.show()


        self.pushButton_add.clicked.connect(self.addButton_clicked)
        self.pushButton_cancelAdd.clicked.connect(self.backToMainPage)

    def addButton_clicked(self):
        if(self.checkInfo()):
            newCustomerObj = BLL.customer(self.lineEdit_firstNameM.text(), self.lineEdit_lastNameM.text(), self.lineEdit_studNumM.text(),
                                          self.lineEdit_conNumM.text(), self.lineEdit_typeM.text(), self.comboBox_size.currentText(),
                                          self.lineEdit_priceM.text(), self.lineEdit_paymentM.text(), self.comboBox_status.currentText())
            if(newCustomerObj.createCustomer() == int(self.lineEdit_studNumM.text())):
                self.backToMainPage()

    def backToMainPage(self):
        self.newWindow = mainPage.mainPage()
        self.close()
        self.newWindow.show()

    def errorBox(self, tMsg):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setText(tMsg)
        msg.setWindowTitle("LOGIN FAILED")
        msg.setStandardButtons(QMessageBox.Ok)
        x = msg.exec_()

    def checkInfo(self):
        if(self.lineEdit_studNumM.text() == "" or self.lineEdit_firstNameM.text() == "" or self.lineEdit_lastNameM.text() == ""
         or self.lineEdit_conNumM.text() == "" or self.lineEdit_typeM.text() == "" or self.lineEdit_priceM.text() == ""
         or self.lineEdit_paymentM.text() == ""):
            self.errorBox("DO NOT LEAVE INPUT FIELDS EMPTY!")
            return False
        elif(self.lineEdit_studNumM.text().isdecimal() == False):
            self.errorBox("INVALID STUDENT NUMBER!\nSTUDENT NUMBER MUST ONLY CONTAIN NUMBERS")
            return False
        elif(self.lineEdit_firstNameM.text().isalpha() == False or self.lineEdit_lastNameM.text().isalpha() == False):
            self.errorBox("INVALID FIRST NAME!\nNAME MUST ONLY CONTAIN LETTERS")
            return False
        elif(self.lineEdit_conNumM.text().isdecimal() == False):
            self.errorBox("INVALID CONTACT NUMBER!\CONTACT NUMBER MUST ONLY CONTAIN NUMBERS")
            return False
        elif(self.lineEdit_priceM.text().isdecimal() == False):
            self.errorBox("INVALID PRICE!")
            return False
        elif(self.lineEdit_paymentM.text().isdecimal() == False):
            self.errorBox("INVALID PAYMENT!")
            return False
        else:
            return True
