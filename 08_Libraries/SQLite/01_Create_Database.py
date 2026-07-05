import sqlite3
import os

#print("Current Working Directory:")
#print(os.getcwd())

conn = sqlite3.connect("bank.db")
cursor=conn.cursor()
cursor.execute("""
CREATE TABLE accounts(
               id INTEGER PRIMARY KEY,
               name TXT,
               balance REAL)""")
conn.commit()
conn.close()
print("Table Created Successfully!")

conn.close()