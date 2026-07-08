import sqlite3
conn = sqlite3.connect("bank.db")
cursor=conn.cursor()
conn.close()