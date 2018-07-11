import smtplib
fromaddr="Your email address"
toaddr="email adrress to which mail is to send"
msg=MIMEMultipart()
msg['From']=fromaddr
msg['To']=toaddr
msg['Subject']="subject"
body="hello brother"
msg.attach(MIMEText(body,'plain'))
server=smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(fromaddr,"Yourpassword")
text=msg.as_string()
server.sendmail(fromaddr,toaddr,text)
server.quit()
