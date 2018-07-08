import pymysql
db=pymysql.connect("127.0.0.1","root","1234","newdatabase",3306)
cursor=db.cursor()
def insert():
    ids=int(input("enter your id:"))
    name=str(input("enter your name"))
    dept=str(input("enter your department"))
    desig=str(input("enter your designation"))
    db=pymysql.connect("127.0.0.1","root","1234","newdatabase",3306)
    cursor=db.cursor()
    try:
      sql="insert into records values(%d,'%s','%s','%s')"%(ids,name,dept,desig)
      cursor.execute(sql)
      db.commit()
      print("records added")
    except:
      db.rollback()
      db.close()
def delete():
    id=int(input("enter the id you want to delete"))
    db=pymysql.connect("127.0.0.1","root","1234","newdatabase",3306)
    cursor=db.cursor()
    try:
        sql="delete from records where id=%d"%(id)
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()
        db.close()
        print("record deleted")    
def update():
        ids=int(input("enter the id you want to update"))
        name=str(input("enter the name"))
        dept=str(input("enter the department to be updated"))
        desig=str(input("enter the designation to be updated"))
        db=pymysql.connect("127.0.0.1","root","1234","newdatabase",3306)
        cursor=db.cursor()
        sql="UPDATE records SET name='%s',dept='%s',designation='%s' where id='%d'"%(name,dept,desig,ids)
        cursor.execute(sql)
        db.commit()
        db.close()
def view():
    ids=int(input("enter the id for which you want to view the records"))
    db=pymysql.connect("127.0.0.1","root","1234","newdatabase",3306)
    cursor=db.cursor()
    sql="select * from records"
    try:
       cursor.execute(sql)
       result=cursor.fetchall()
       print(result)
       for row in result:
          ids=row[0]
          name=row[1]
          dept=row[2]
          desg=row[3]
    except:
       print("error")
       db.close()
def search():
    
    ids=int(input("enter the id you want to search"))
    sql="select * from records where id='%d'"%(ids)
    cursor=db.cursor()
    cursor.execute(sql)
    result=cursor.fetchall()
    print(result)





opt="Y"    
    
print("WELCOME TO THE DATABASE MANAGEMENT SYSTEM")
print("1.insert employees")
print("2.delete employees")
print("3.update employees")
print("4.view employees details")
print("5.search employees")

while opt=="Y":
    ch=int(input("enter your choice"))
    if(ch==1):
        insert()
    elif(ch==2):
        delete()
    elif(ch==3):
        update()
    elif(ch==4):
        view()
    elif(ch==5):
        search()
    else:
        print("enter the correct choice")
    opt=str(input("Do you want to continue !!"))    

    
