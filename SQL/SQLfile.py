import sqlite3
# from Employee import Employee

conn = sqlite3.connect('summary.db')  #memory

c = conn.cursor()

def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS payment(first text, last text, size text, type text, pay integer, status text)')

def data_entry():
    c.execute('INSERT INTO payment VALUES("Dave", "Banguilan", "MEDIUM", "ENGBLACK", 350, "PAID")')
    conn.commit()
    c.close()
    conn.close()

create_table()
data_entry()
