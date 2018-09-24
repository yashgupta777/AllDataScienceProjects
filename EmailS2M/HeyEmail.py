import smtplib
from email import encoders
from email.message import Message
from email.mime.audio import MIMEAudio
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import pandas as pd

df = pd.read_csv('C:/Users/Yash/PycharmProjects/EmailS2M/input/Email.csv', delimiter=',')
fromaddr = "nikhil@stones2milestones.com"
# toaddr = "EMAIL ADDRESS YOU SEND TO"
# cc = "yash@stones2milestones.com"
for index, row in df.iterrows():
    print(row["Name"], row["Email"], row["Gender"])
    xgender = row["Gender"]
    xname = row["Name"]
    # name= xname
    toaddr = row["Email"]

    # print(fromaddr)
    print(toaddr)
    # print(cc)
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    # msg['Cc'] = cc
    msg['Subject'] = "Congratulations & Introducing Stones2Milestones // 6th School Leadership Summit"
    body = """\
            <html>
              <head></head>
              <body>
                <p>Happy Evening {name} {gender},<br><br>                                                      
                </p>
                <p>I missed an opportunity to interact with you at the 6th School Leadership Summit held in Delhi last Saturday. Congratulations on the achievement, I am sure you enjoyed the summit as much as we did. <br>               
                </p>
                <p>
                It was personally an engaging experience interacting with your school and the educators as a part of the <strong> Importance of Inducive Policies to Build Effective School Education Ecosystem </strong> panel along with Ryan Pinto, Roshan Gandhi, Dr Manjula Shroff, Shreevats Jaipuria, Raghav Podar & Abha Meghe. <br>
                </p>
                <p>I would like to take this moment to personally introduce our mission of  <strong>'Creating a Nation of Readers'. </strong>In case you find our pursuit worthwhile, would love to schedule a conversation on how you can play your part in it. <br></p>                                
                <p>Looking forward to interacting with you.<br></p>
                 <p>Yours in Reading,<br></p>    
                 <p>Nikhil<br><br></p>                                                                           
                <p style="font-size: x-small;color: rgb(153, 153, 153);font-style: italic;">Recent accomplishments:<br>
                    + S2M launches World's first adaptive reading ecosystem designed for schools. Watch the product video <a href="https://www.youtube.com/watch?v=iJI_L1w9tzM&feature=youtu.be">here</a><br>
                    + S2M hosted Asia's largest children's literature festival <a href="http://www.bookaroo.in/"> Bookaroo</a> on Nov'17 with 101 sessions / 60 Authors / 13 Countries over two days at India Gate<br>
                    + S2M was handpicked to be part of <a href="https://www.projectliteracy.com/lab/">Project Literacy Lab</a> in the US (run by Pearson & Unreasonable Group) and was the only organisation from Asia to be selected. Coverage  <a href="http://www.prnewswire.co.in/news-releases/edtech-startup-stones2milestones-handpicked-to-attend-the-worlds-first-accelerator-dedicated-to-closing-the-global-literacy-gap-657377653.html">here</a><br>
                    + Our free reading assessment for schools <a href="https://f-ast.in/">'FAST'</a> has been taken by over 50,000 children across the country. You can register your school <a href="https://f-ast.in/"> here.</a> <br> </p>

                <html xmlns="http://www.w3.org/1999/xhtml">
                    <head>
                        <title></title>
                    </head>
                    <body style="word-wrap: break-word; -webkit-nbsp-mode: space; -webkit-line-break: after-white-space;">
                        <div dir="ltr" style="color: rgb(34, 34, 34); font-family: arial, sans-serif; font-size: 12.8px; font-variant-ligatures: normal; orphans: 2; widows: 2;">
                            <table width="402" cellpadding="0" style="font-size: 12.8px; font-family: roboto, sans-serif;">
                <tbody>
                                    <tr>
                                        <td style="font-family: arial, sans-serif; margin: 0px;">
                                            <span style="color: rgb(66, 172, 78);">
                                                <span style="font-size: small;">
                                                    <b>Nikhil </b>
                                                     Saraf</span>
                                            </span>
                                             <span style="font-family: roboto, sans-serif;">
                                                <span style="font-size: xx-small;">/ </span>
                                                <span style="color: rgb(102, 102, 102);">
                                                    <font size="1">Gurgaon</font>
                                                </span>
                                                 <span style="font-size: xx-small;"> </span>
                                            </span>

                </td>

                </tr>
                                    <tr>
                                        <td style="font-family: arial, sans-serif; margin: 0px;">
                                            <span style="font-family: roboto, sans-serif; color: rgb(102, 102, 102);">
                                                <font size="1">
                                                    <strong>+91</strong>
                                                     <strong> 8511117267 </strong>
                                                     / 9077077777</font>
                                            </span>
                                            <br />
                                        </td>

                </tr>
                                    <tr>
                                        <td style="font-family: arial, sans-serif; margin: 0px;">
                                            <span style="font-family: roboto, sans-serif;">
                                                <span style="color: rgb(102, 102, 153);">
                                                    <a href="http://www.stones2milestones.com/" rel="noopener" target="_blank" style="color: rgb(102, 102, 102);">
                                                        <font size="1">www.stones2milestones.com</font>
                                                    </a>
                                                    <br />
                                                    <br />
                                                </span>
                                            </span>
                                        </td>

                </tr>
                                </tbody>
                            </table>
                        </div>
                        <div dir="ltr" style="color: rgb(34, 34, 34); font-family: arial, sans-serif; font-size: 12.8px; font-variant-ligatures: normal; orphans: 2; widows: 2;">
                            <a href="http://www.stones2milestones.com/" target="_blank" rel="noopener" data-saferedirecturl="https://www.google.com/url?hl=en&amp;q=http://www.stones2milestones.com&amp;source=gmail&amp;ust=1503670571498000&amp;usg=AFQjCNGEOjcpAOsHBZ8wh6MjH4pv2B9teg">
                                <img src="https://drive.google.com/a/stones2milestones.com/uc?id=0BxWUUNugOdzGYTFPN0xveTZWX0E&amp;export=download" width="510" height="172" />
                            </a>
                        </div>
                        <div dir="ltr" style="color: rgb(34, 34, 34); font-family: arial, sans-serif; font-size: 12.8px; font-variant-ligatures: normal; orphans: 2; widows: 2;">
                            <div dir="ltr" style="font-size: 12.8px; font-variant-ligatures: normal;"></div>
                            <div dir="ltr" style="font-size: 12.8px; font-variant-ligatures: normal;"></div>
                        </div>
                    </body>
                </html>
              </body>
            </html>
            """.format(name=xname,gender =xgender)
    #
    # # Record the MIME types of both parts - text/plain and text/html.
    # part2 = MIMEText(html, 'html')
    msg.attach(MIMEText(body, 'html'))
    # filename = "Stones2Milestones Intro Note.pdf"
    # attachment = open("C:/Users/Yash/Downloads/Stones2Milestones Intro Note.pdf", "rb")
    part = MIMEBase('application', 'octet-stream')
    # part.set_payload((attachment).read())
    # encoders.encode_base64(part)
    # part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
    # msg.attach(part)
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(fromaddr, "S2M@98765")
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    print('Success')
    server.quit()