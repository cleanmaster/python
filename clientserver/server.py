host="localhost"
port=int(input("enter port number:")) #reserve a port number for your service
import socket  #import socket module
s=socket.socket() #create a socket object
s.bind((host,port))
s.listen(1)
conn,addr=s.accept() # establish connection withh client
data=conn.recv(2000)
print(data.decode())
