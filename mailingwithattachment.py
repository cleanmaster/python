import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
fromaddr="your email id"
toaddr="email address to send"
sub="testing mailing with attachment"
msg=MIMEMultipart()
msg['from']=fromaddr
msg['To']=toaddr
msg['subject']=sub
body="hello world!!!!!!!!!!"
msg.attach(MIMEText(body,'plain'))
filename="filename"
attachment=open("filename with extension","rb")
part=MIMEBase('application','octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header("content_Disposition","attachment;filename=%s"%filename)
msg.attach(part)
server=smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(fromaddr,"your password")
text=msg.as_string()
server.sendmail(fromaddr,toaddr,text)
server.quit()
