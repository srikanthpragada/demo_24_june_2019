
import sqlite3

con = sqlite3.connect(r"e:\classroom\python\june24\training.db")
cur = con.cursor()
title = input("Enter course title : ")
cur.execute("select * from courses where title like ?", (f'%{title}%',) )

rows = cur.fetchall()
if len(rows) == 0:
    print("Sorry! No courses found!")
else:
    for row in rows:
        print(f"{row[1]:30} {row[2]:5} {row[3]:6}")


cur.close()
con.close()