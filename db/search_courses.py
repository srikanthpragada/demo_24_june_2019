
import sqlite3

con = sqlite3.connect(r"e:\classroom\python\june24\training.db")
cur = con.cursor()
title = input("Enter course title : ")
cur.execute("select * from courses where title like ?", (f'%{title}%',) )
    # print("Sorry! No courses found!")

for row in cur.fetchall():
   print(f"{row[1]:30} {row[2]:5} {row[3]:6}")


cur.close()
con.close()