import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

fromaddr = "Yash@stones2milestones.com"
toaddr = "vivek@stones2milestones.com"
msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "Chutiya"

body = "Vivek Chutiya"
msg.attach(MIMEText(body, 'plain'))

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(fromaddr, "9016720124")
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()