import sqlite3
conn=sqlite3.connect("bank.db")
cursor=conn.cursor()
cursor.execute("""UPDATE accounts
               SET Balance=2000
               WHERE Id=1""")
conn.commit()
cursor.execute("SELECT * FROM accounts")
data=cursor.fetchall()
for row in data:
    print("Id:",row[0])
    print("Name:",row[1])
    print("Balance:",row[2])
conn.close()