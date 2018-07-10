import smtplib
server=smtplib.SMTP('smtp.gmail.com',587)
server.starttls()  #starts listening
server.login("your email","your password")
msg="hello buddy!!!!!!!!!"
server.sendmail("Your email id","the email address to be send",msg)
server.quit()
