import smtplib

server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()
server.ehlo()
server.login("yash@stones2milestones.com", "9016720124")

msg = "YOUR MESSAGE!"
server.sendmail("yash@stones2milestones.com", "nikhil@stones2milestones.com", msg)
server.quit()

# import smtplib
# from email.MIMEMultipart import MIMEMultipart
# from email.MIMEText import MIMEText
#
# fromaddr = "YOUR ADDRESS"
# toaddr = "ADDRESS YOU WANT TO SEND TO"
# msg = MIMEMultipart()
# msg['From'] = fromaddr
# msg['To'] = toaddr
# msg['Subject'] = "SUBJECT OF THE MAIL"
#
# body = "YOUR MESSAGE HERE"
# msg.attach(MIMEText(body, 'plain'))
#
# server = smtplib.SMTP('smtp.gmail.com', 587)
# server.starttls()
# server.login(fromaddr, "YOUR PASSWORD")
# text = msg.as_string()
# server.sendmail(fromaddr, toaddr, text)
# server.quit()