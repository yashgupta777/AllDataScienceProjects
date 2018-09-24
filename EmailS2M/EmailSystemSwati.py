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
fromaddr = "swati@stones2milestones.com"
# toaddr = "EMAIL ADDRESS YOU SEND TO"
# cc = "yash@stones2milestones.com"
for index, row in df.iterrows():
    print (row["Name"], row["Email"])


    xname = row["Name"]
    # name= xname
    toaddr =row["Email"]

    # print(fromaddr)
    print(toaddr)
    # print(cc)
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    # msg['Cc'] = cc
    msg['Subject'] = "Request for meeting to introduce our mission '''Creating a Nation of Readers'''"
    body = """\
            <html>
              <head></head>
              <body>
                <p>Dear School Leader,<br><br>                                                      
                </p>
                <p><a href="http://www.stones2milestones.com/">Stones2Milestones</a> is on a mission to 'Create a Nation of Readers'<br></p>
                <p> Young Indian children going to English medium schools fall behind academically because they are expected to learn, read and speak in a language that is alien to them and their surroundings - English. <br>                   
                </p>
                <p>
                We solve that problem by giving them the <strong> skill and will to read in English <strong> through scientifically designed and intuitive reading programs which give them a lifelong edge in learning.<br>
                </p>
                <p>We are unique because we are pioneering this effort in a systematic way that is contextual and age-appropriate where English is a second language yet aspirational. In India itself,  <strong>an estimated 89% of 250 million children read below grade level. </strong><br></p>
                <p>Currently, we have an affordable offering for schools, directly impacting more than 100,000 children. The team believes that by helping children to 'Learn to Read' in elementary years, they enable them to 'Read to Learn' during formal education and eventually 'Read to Lead' in their chosen path, aiding them in finding their place in the world.<br></p>
                <p>PFA an introductory note to know more about us.<br></p>
                <p>In case you find our pursuit worthwhile, we look forward to having a conversation with you.<br></p>                
                <p>Please let us know a convenient date to visit you to give a small presentation on our work.<br></p>
                <p>Request for meeting on coming week of April 2018.<br></p>
                 <p>Yours in Reading,<br></p>    
                 <p>Swati Rohatgi<br><br></p>                                                                           
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
                                                    <b>Swati </b>
                                                     Rohatgi</span>
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
                                                     <strong> 9077110077 </strong>
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
            """
    #
    # # Record the MIME types of both parts - text/plain and text/html.
    # part2 = MIMEText(html, 'html')
    msg.attach(MIMEText(body, 'html'))
    filename = "Stones2Milestones Intro Note.pdf"
    attachment = open("C:/Users/Yash/Downloads/Stones2Milestones Intro Note.pdf", "rb")
    part = MIMEBase('application', 'octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
    msg.attach(part)
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(fromaddr, "swati417")
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr , text)
    print('Success')
    server.quit()