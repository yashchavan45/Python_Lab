import sqlite3
conn = sqlite3.connect("bank.db")
cursor=conn.cursor()
cursor.execute("""
CREATE TABLE accounts(
               id INTEGER PRIMARY KEY,
               name TXT,
               balance REAL)""")
conn.commit()
conn.close()