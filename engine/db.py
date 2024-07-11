import sqlite3
import csv

conn = sqlite3.connect("myai.db")  # to make a database
cursor = conn.cursor()

# query ="CREATE TABLE IF NOT EXISTS sys_command( id integer primary key, name VARCHAR(100), path VARCHAR(1000))"       # creating a table sys_command
# cursor.execute(query)

# insert into table

# query ="INSERT INTO sys_command VALUES (null, 'powerpoint', 'C:\\Program Files\\Microsoft Office\\root\Office16\\POWERPNT.exe')"
# cursor.execute(query)
# conn.commit()

# query ="CREATE TABLE IF NOT EXISTS web_command( id integer primary key, name VARCHAR(100), url VARCHAR(1000))"       # creating a table sys_command
# cursor.execute(query)

# query ="INSERT INTO web_command VALUES (null, 'google', 'https://www.google.co.in/')"
# cursor.execute(query)
# conn.commit()

# testing module
#app_name = "microsoft word"
#cursor.execute('SELECT path FROM sys_command WHERE name IN (?)', (app_name,))
#results = cursor.fetchall()
#print(results[0][0])

#query ="CREATE TABLE IF NOT EXISTS contacts( id integer primary key, name VARCHAR(100), mobile_no VARCHAR(255), email VARCHAR(255) NULL )"       # creating a table contact
#cursor.execute(query)

""" desired_column_indices= [0,35]    # specify column indices you want to import

with open('contacts.csv','r',encoding='utf-8') as csvfile:
    csvreader=csv.reader(csvfile)
    for row in csvreader:
        selected_data = [row[i] for i in desired_column_indices]
        cursor.execute(''' INSERT INTO contacts (id,'name','mobile_no') VALUES (null, ?, ?);''', tuple(selected_data))

conn.commit()
conn.close() """

# inserting single contact
# query= "INSERT INTO contacts VALUES (null,'xyz','9999999999','null')"
# cursor.execute(query)
# conn.commit()

query="prsnI"
query=query.strip().lower()

cursor.execute(" SELECT mobile_no FROM contacts WHERE LOWER(name) LIKE ? OR LOWER(name) LIKE ?",('%'+ query + '%',query + '%'))
results = cursor.fetchall()
print(results[0][0])