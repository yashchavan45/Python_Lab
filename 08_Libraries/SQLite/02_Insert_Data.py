import sqlite3
conn=sqlite3.connect("bank.db")
cursor=conn.cursor()
cursor.execute("""
INSERT INTO accounts(name,balance)
VALUES ('Yash',1000)
""")
conn.commit()
print("Data Inserted Successfully!")

conn.close()