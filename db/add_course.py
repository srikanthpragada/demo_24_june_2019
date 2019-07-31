
import sqlite3

con = sqlite3.connect(r"e:\classroom\python\june24\training.db")
cur = con.cursor()
title = input("Enter title : ")
duration = input ("Enter duration : ")
fee = input("Enter fee : ")
cur.execute("insert into courses (title,duration,fee) values(?,?,?)",
              (title,duration,fee))
con.commit()
cur.close()
con.close()