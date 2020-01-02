import os
import sqlite3

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
                                Name text NOT NULL,
                                Type text NOT NULL,
                                Size text NOT NULL,
                                Payment integer,
                                Date text NOT NULL
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




# def main():
#     conn = connectToDB()
#     accountTable = """ CREATE TABLE IF NOT EXISTS Accounts (
#                                         Student_Number integer PRIMARY KEY,
#                                         Name text,
#                                         Username text,
#                                         Password text
#                                     ); """
#
#     customerTable = """CREATE TABLE IF NOT EXISTS Customers (
#                                     Student_Number integer PRIMARY KEY,
#                                     Name text NOT NULL,
#                                     Type text NOT NULL,
#                                     Size text NOT NULL,
#                                     Payment integer,
#                                     Date text NOT NULL
#                                 );"""
#     createTable(conn, accountTable)
#     createTable(conn, customerTable)
#
# if __name__ == '__main__':
#     main()
