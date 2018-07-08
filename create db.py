import pymysql
db=pymysql.connect("127.0.0.1","root","1234","",3306)
cursor=db.cursor()
cursor.execute("create database newdatabase")
cursor.execute("use newdatabase")
print("database created")
