from DAL import newAccount, checkLogin, viewAll_Customer, newCustomer, delete_Customer

class login:

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def verifyAccount(self):
        return checkLogin(self.username, self.password)


class account:

    def __init__(self, fname, lname, stdNum, username, password):
        self.fname = fname
        self.lname = lname
        self.fullName = fname + ' ' + lname
        self.stdNum = int(stdNum)
        self.username = username
        self.password = password

    def createAccount(self):
        return newAccount(self.stdNum, self.fullName, self.username, self.password)

class customer:
    def __init__(self, firstName, lastName, studentNumber, contactNumber, shirtType, shirtSize, price, payment, status):
        self.firstName = firstName
        self.lastName = lastName
        self.fullName = firstName + ' ' + lastName
        self.studentNumber = int(studentNumber)
        self.contactNumber = contactNumber
        self.shirtType = shirtType
        self.shirtSize = shirtSize
        self.price = int(price)
        self.payment = int(payment)
        self.status = status

    def viewCustomer():
        return viewAll_Customer()

    def createCustomer(self):
        return newCustomer(self.studentNumber, self.fullName, self.contactNumber, self.shirtType, self.shirtSize, self.price, self.payment, self.status)

    def deleteCustomer(handle):
        return delete_Customer(handle)

    # def checkCustomer(self):
    #     return ""


# def main():
#     print(customer.viewCustomer())
#
# if __name__ == '__main__':
#     main()
