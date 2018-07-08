import pymysql
db=pymysql.connect("127.0.0.1","root","1234","newdatabase",3306)
cursor=db.cursor()
try:
  cursor.execute("insert into records values(1,'Keshav','IT','Engineer')")
  db.commit()
except:
    db.rollback()
    db.close()
print("records inserted")    
    
    
