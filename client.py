host="localhost"
port=int(input("enter port number"))
import socket
s=socket.socket() #create a socket object
s.connect((host,port))
st="connection done" #enter the message you want to sent
enc_msg=st.encode()
s.send(enc_msg)
