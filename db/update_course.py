import sqlite3

con = sqlite3.connect(r"e:\classroom\python\june24\training.db")
cur = con.cursor()
id = input("Enter Id : ")
newfee = input("Enter new fee : ")
cur.execute("update courses set fee = ? where id = ?", (newfee, id))
if cur.rowcount == 1:
    print("Successfully updated course!")
    con.commit()
else:
    print("Sorry! Course not found!")

cur.close()
con.close()
