import os
import sqlite3
import datetime

# create a default path to connect to and create (if necessary) a database
# called 'database.sqlite3' in the same directory as this script
DEFAULT_PATH = os.path.join(os.path.dirname(__file__), 'database.db')

accountTable = """ CREATE TABLE IF NOT EXISTS Accounts (
                                    Student_Number integer PRIMARY KEY,
                                    Name text,
                                    Username text,
                                    Password text
                                ); """

customerTable = """CREATE TABLE IF NOT EXISTS Customers (
                                Student_Number integer PRIMARY KEY,
                                Name text,
                                Phone_Number text,
                                Type text,
                                Size text,
                                Price integer,
                                Payment integer,
                                Status text,
                                Date text
                            );"""

def connectToDB():
    connection = sqlite3.connect(DEFAULT_PATH)
    cur = connection.cursor()
    cur.execute(accountTable)
    cur.execute(customerTable)
    return connection


def newAccount(stdNum, fullName, username, password):
    con = connectToDB()
    cur = con.cursor()
    cur.execute("INSERT INTO Accounts VALUES (?, ?, ?, ?)", (stdNum, fullName, username, password))
    con.commit()
    return cur.lastrowid

def checkLogin(userN, passW):
    con = connectToDB()
    cur = con.cursor()
    cur.execute("SELECT Name,Username,Password FROM Accounts WHERE username = ?  AND password = ?", (userN, passW))
    result = cur.fetchall()
    if(result == []):
        return ""
    else:
        return result[0][0]



def newCustomer(studNum, fullName, phoneNum, shType, shSize, price, payment, status):
    con = connectToDB()
    cur = con.cursor()
    cur.execute("INSERT INTO Customers VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", (studNum, fullName, phoneNum, shType, shSize, price, payment, status, datetime.date.today()))
    con.commit()
    con.close()
    return cur.lastrowid

def delete_Customer(deleteRow):
    con = connectToDB()
    cur = con.cursor()
    res = viewAll_Customer()
    for row in enumerate(res):
        if(row[0] == deleteRow):
            data = row[1]
            studNum = int(data[0])
            fullname = data[1]
            pnum = data[2]
            shType = data[3]
            shSize = data[4]
            shPrice = int(data[5])
            shPayment = int(data[6])
            shStatus = data[7]
            shDate = data[8]
            cur.execute("DELETE FROM Customers WHERE Student_Number = ? AND Name = ? AND Phone_Number = ? AND Type = ? AND Size = ? AND Price = ? AND Payment = ? AND Status = ? AND Date = ?",  (studNum, fullname , pnum, shType, shSize, shPrice, shPayment, shStatus, shDate))
            con.commit()
    return cur.lastrowid

def viewAll_Customer():
    con = connectToDB()
    cur = con.cursor()
    cur.execute("SELECT * FROM Customers")
    return cur.fetchall()
