import sqlite3

dbh=sqlite3.connect("ericsson.db")
c=dbh.cursor()

def create_table():
    c.execute("CREATE TABLE employee(empname TEXT, exp REAL, tech TEXT)")

def load_records():
    e_name=input("Enter your name:")
    e_exp=int(input("Enter your experience:"))
    e_tech=input("Enter your technology:")
    c.execute("INSERT INTO employee VALUES(?,?,?)",(e_name, e_exp, e_tech))

def update_records():
    c.execute("UPDATE employee SET tech='Python' WHERE empname='Ganesh'")

def delete_records():
    c.execute("DELETE FROM employee WHERE tech='Oracle'")

def fetch_records():
    c.execute("SELECT * FROM employee")
    #print(c.fetchone())
    #print(c.fetchmany(3))
    for row in c.fetchall():
        if row[1] > 20:
            print(f"{row[0]} has {row[1]} years of experience in {row[2]}")
#create_table()
# for x in range(5):
#     load_records()
#update_records()
#delete_records()
fetch_records()
dbh.commit()
c.close()
dbh.close()
