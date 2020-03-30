#!/usr/bin/python3
"""Lista all states from the database hbtn_0e_0_usa"""
import MySQLdb
conn = MySQLdb.connect(host="localhost",
                       port=3306,
                       user="root",
                       passwd="root",
                       db="hbtn_0e_0_usa",
                       charset="utf8")
cur = conn.cursor()
cur.execute("SELECT * from states ORDER BY states.id ASC")
query = cur.fetchall()
for row in query:
    print(row)
cur.close()
conn.close()
