import pymysql
db=pymysql.connect("127.0.0.1","root","1234","newdatabase",3306)
cursor=db.cursor()
sql="select * from records"
try:
    cursor.execute(sql)
    result=cursor.fetchall()
    print(result)
    for row in result:
        id=row[0]
        name=row[1]
        dept=row[2]
        desg=row[3]
        print("id=",id,"name+",name,"dept=",dept,"designation=",desg)
except:
    print("error")
    db.close()
