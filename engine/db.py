import sqlite3

conn = sqlite3.connect("myai.db")  # to make a database
cursor = conn.cursor()

#query ="CREATE TABLE IF NOT EXISTS sys_command( id integer primary key, name VARCHAR(100), path VARCHAR(1000))"       # creating a table sys_command
#cursor.execute(query)

# insert into table

# query ="INSERT INTO sys_command VALUES (null, 'one note', 'C:\\Program Files\\Microsoft Office\\root\\Office16\\ONENOTE.exe')"
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