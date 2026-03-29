import sqlite3
import random
con = sqlite3.connect("broslibDB.db")
cur = con.cursor()
cur1 = con.cursor()
rvar1 = random.randint(1, 5)
rvar2 = (rvar1, )
cur.execute("SELECT booknum, room, bcase, shelf, position, title, author FROM books WHERE booknum =?",  (rvar2))
records = cur.fetchall()
print("Total current books are:  ", len(records))
print("Printing each row")
for row in records:
    var1 = row[0]
    print(var1)
    var2 = row[1]
    print(var2)
    var3 = row[2]
    print(var3)
    var4 = row[3]   
    print(var4)
    var5 = row[4]   
    print(var5)
    var6 = row[5]   
    print(var6)
    var7 = row[6]   
    print(var7)
bookdata = [
    ("MON","20260329", var1, var2, var3, var4, var5, var6, var7, "good read")
]
cur.executemany("INSERT INTO readings VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", bookdata)
con.commit()
cur.execute("SELECT day, date, booknum, room, bcase, shelf, position, title, author, notes FROM readings")
records = cur.fetchall()
print("Total current books are:  ", len(records))
print("Printing each row")
for row in records:
    print(row[0])
    print(row[1])
    print(row[2])
    print(row[3])
    print(row[4])
    print(row[5])
    print(row[6])
    print(row[7])
    print(row[8])
    print(row[9])
cur.close()