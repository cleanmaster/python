import pymysql
db=pymysql.connect("127.0.0.1","root","1234","newdatabase",3306)
cursor=db.cursor()
try:
     cursor.execute("delete from records where id=1")
     db.commit()
except:
    db.rollback()
    db.close()
print("record deleted")    
