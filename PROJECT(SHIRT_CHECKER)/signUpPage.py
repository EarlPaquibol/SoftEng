import sys
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QMessageBox
from loginPage import *
import BLL

class signUp(QtWidgets.QMainWindow):
    def __init__(self):
        super(signUp, self).__init__()
        loadUi("signUpPage.ui", self)
        self.show()

        self.pushButton_create.clicked.connect(self.createButton_clicked)
        self.pushButton_cancel.clicked.connect(self.backToLogin)

    def createButton_clicked(self):
        if(self.checkInputs()):
            newAccountObj = BLL.account(self.lineEdit_firstNameSU.text(), self.lineEdit_lastNameSU.text(), self.lineEdit_studNum.text(), self.lineEdit_usernameSU.text(), self.lineEdit_passwordSU.text())
            if(newAccountObj.createAccount() == int(self.lineEdit_studNum.text())):
                self.backToLogin()

    def checkInputs(self):
        if(self.lineEdit_firstNameSU.text() == "" or self.lineEdit_lastNameSU.text() == "" or self.lineEdit_studNum.text() == "" or self.lineEdit_usernameSU.text() == "" or self.lineEdit_passwordSU.text() == ""):
            self.warningBox("DO NOT LEAVE THE INPUT FIELDS EMPTY!")
            return False
        elif(self.lineEdit_firstNameSU.text().isalpha() == False):
            self.warningBox("INVALID FIRST NAME!\nNAME MUST ONLY CONTAIN LETTERS")
            return False
        elif(self.lineEdit_lastNameSU.text().isalpha() == False):
            self.warningBox("INVALID LAST NAME!\nNAME MUST ONLY CONTAIN LETTERS")
            return False
        elif(self.lineEdit_studNum.text().isdecimal() == False):
            self.warningBox("INVALID STUDENT NUMBER!\nSTUDENT NUMBER MUST ONLY CONTAIN NUMBERS")
            return False
        elif(self.lineEdit_usernameSU.text().isalnum() == False):
            self.warningBox("INVALID USERNAME!\nINVALID CHARACTERS USED IN USERNAME!")
            return False
        else:
            return True

    def backToLogin(self):
        self.ui = LoginPage()
        self.ui.show()
        self.close()

    def warningBox(self,tMsg):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setText(tMsg)
        msg.setWindowTitle("SIGN UP FAILED")
        msg.setStandardButtons(QMessageBox.Ok)
        x = msg.exec_()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = signUp()
    window.show()
    sys.exit(app.exec_())
