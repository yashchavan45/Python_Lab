import sqlite3
conn=sqlite3.connect("bank.db")
cursor=conn.cursor()
cursor.execute("SELECT * FROM accounts")
data=cursor.fetchall()
#print(data)
for row in data:
    print("Id:",row[0])
    print("Name:",row[1])
    print("Balance:",row[2])
conn.close()