import pymysql
db=pymysql.connect("127.0.0.1","root","1234","newdatabase",3306)
cursor=db.cursor()
sql="UPDATE records SET name='manuj' where id=1"
cursor.execute(sql)
db.commit()
db.close()
