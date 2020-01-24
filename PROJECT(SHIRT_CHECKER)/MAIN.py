import sys
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QMessageBox
import BLL
import mainPage

class LoginPage(QtWidgets.QMainWindow):
    def __init__(self):
        super(LoginPage, self).__init__()
        loadUi("loginPage.ui", self)
        self.show()

        self.lineEdit_password.setEchoMode(QtWidgets.QLineEdit.Password) #HIDE PASSWORD
        self.pushButton_login.clicked.connect(self.loginButton_clicked)
        # self.pushButton_signUp.clicked.connect(self.signUpButton_clicked)

    def loginButton_clicked(self):
        if(self.checkInputs()):
            checkAccount = BLL.login(self.lineEdit_username.text(), self.lineEdit_password.text())
            verify = checkAccount.verifyAccount()
            if(verify != ""):
                self.showMainWindow()
            else:
                self.popUpbox("ERROR!")

    def checkInputs(self):
        if(self.lineEdit_username.text() == "" and self.lineEdit_password.text() == ""):
            self.popUpbox("DO NOT LEAVE INPUT FIELDS EMPTY!")
            return False
        elif(self.lineEdit_username.text() == ""):
            self.popUpbox("USERNAME EMPTY!")
            return False
        elif(self.lineEdit_password.text() == ""):
            self.popUpbox("PASSWORD EMPTY!")
            return False
        else:
            return True

    def popUpbox(self, tMsg):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setText(tMsg)
        msg.setWindowTitle("LOGIN FAILED")
        msg.setStandardButtons(QMessageBox.Ok)
        x = msg.exec_()

    def showMainWindow(self):
        self.newWindow = mainPage.mainPage()
        self.close()
        self.newWindow.show()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = LoginPage()
    window.show()
    sys.exit(app.exec_())
