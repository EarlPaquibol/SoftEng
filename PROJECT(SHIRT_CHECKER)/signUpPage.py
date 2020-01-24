import sys
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QMessageBox
import BLL
import mainPage

class signUp(QtWidgets.QMainWindow):
    def __init__(self):
        super(signUp, self).__init__()
        loadUi("signUpPage.ui", self)
        self.show()

        self.pushButton_create.clicked.connect(self.createButton_clicked)
        self.pushButton_cancel.clicked.connect(self.backToMainPage)

    def createButton_clicked(self):
        if(self.checkInputs()):
            newAccountObj = BLL.account(self.lineEdit_firstNameSU.text(), self.lineEdit_lastNameSU.text(), self.lineEdit_studNum.text(), self.lineEdit_usernameSU.text(), self.lineEdit_passwordSU.text())
            if(newAccountObj.createAccount() == int(self.lineEdit_studNum.text())):
                self.backToMainPage()

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

    def backToMainPage(self):
        self.newWindow = mainPage.mainPage()
        self.close()
        self.newWindow.show()

    def warningBox(self,tMsg):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setText(tMsg)
        msg.setWindowTitle("SIGN UP FAILED")
        msg.setStandardButtons(QMessageBox.Ok)
        x = msg.exec_()
