import sqlite3

connection = sqlite3.connect('emaildb.sqlite')
cur = connection.cursor()

cur.execute('DROP TABLE IF EXISTS Counts')
cur.execute ('CREATE TABLE Counts(email TEXT, count INTEGER)')

file_name = input ('Input your file name: ')
f_handle = open(file_name)
for line in f_handle:
    if not line.startswith('From') :
        continue 
    line = line.strip()
    line_list = line.split()
    email = line_list[1]
    cur.execute('SELECT count FROM Counts WHERE email = ?', (email,))
    row = cur.fetchone()
    if row is None :
        cur.execute('INSERT INTO Counts (email,count)VALUES (?,1)', (email,))
    else :
        cur.execute('''UPDATE Counts SET count = count + 1
         WHERE email = ?''', (email,))
    connection.commit()

