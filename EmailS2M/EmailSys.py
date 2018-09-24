import smtplib
from email import encoders
from email.message import Message
from email.mime.audio import MIMEAudio
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import pandas as pd
df = pd.read_csv('C:/Users/Yash/PycharmProjects/EmailS2M/input/Email.csv',delimiter=',')
fromaddr = "yash@stones2milestones.com"
# toaddr = "EMAIL ADDRESS YOU SEND TO"
for xemail in df['Email'].tolist():
    # name= xname
    toaddr =xemail
    print(toaddr)
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "SUBJECT OF THE EMAIL"
    body = "Hi\nDemo "
    # html = """\
    # <html>
    #   <head></head>
    #   <body>
    #     <p>Hi!<br>
    #        How are you?<br>
    #        Here is the <a href="http://www.python.org">link</a> you wanted.
    #     </p>
    #   </body>
    # </html>
    # """
    #
    # # Record the MIME types of both parts - text/plain and text/html.
    # part2 = MIMEText(html, 'html')
    msg.attach(MIMEText(body, 'plain'))
    filename = "ReadVantage_fast2_Columbia Convt.pdf"
    attachment = open("C:/FastReports/ReadVantage_fast2_Columbia Convt.pdf", "rb")
    part = MIMEBase('application', 'octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
    msg.attach(part)
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(fromaddr, "9016720124")
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    print('Success')
    server.quit()