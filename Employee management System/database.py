import sqlite3

#To create database and to connect with it
conn = sqlite3.connect('employeedb.db', check_same_thread=False)
print("Database created and connected succesfully!")

cursor = conn.cursor()

#To create table
cursor.execute('''CREATE TABLE IF NOT EXISTS employees(empid INTEGER PRIMARY KEY,name TEXT,designation TEXT)''')
print("Employee Table created successfully!!")
