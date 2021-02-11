import sqlite3

connection = sqlite3.connect('db.sqlite3')
cur = connection.cursor()
cur.execute('DROP TABLE IF EXISTS Counts')
cur.execute ('CREATE TABLE Counts(email TEXT, count INTEGER)')

file_name = 'mbox.txt'
file_handle = open(file_name)
for line in file_handle:
    if not line.startswith('From') :
        continue 
    line_list = line.split()
    email_address = line_list[1]
    cur.execute('SELECT count FROM Counts WHERE email = ?',
                (email_address,))
    row = cur.fetchone()
    
    if row is None :
        cur.execute('INSERT INTO Counts (email,count)VALUES (?,1)', 
                    (email_address,))
    else :
        cur.execute('''UPDATE Counts SET count = count + 1
         WHERE email = ?''', (email_address,))
    connection.commit()
