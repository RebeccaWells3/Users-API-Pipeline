import sqlite3

connection = sqlite3.connect('user_db')
cursor = connection.cursor()

#table columns = id, name, username, email, city, company_name

#create user table
cursor.execute('''
CREATE TABLE IF NOT EXISTS users 
(id INTEGER PRIMARY KEY,
 name TEXT,
 username TEXT,
 email TEXT,
 city TEXT,
 company_name TEXT)
''')

