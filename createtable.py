import pymysql
db=pymysql.connect("127.0.0.1","root","1234","newdatabase",3306)
cursor=db.cursor()
try:
   cursor.execute("""create table records(id int primary key,name varchar(30),dept varchar(30),designation varchar(40))""")
except:
    db.rollback()
    db.close()
print("record deleted")
