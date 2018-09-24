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
fromaddr = "swati@stones2milestones.com"
# toaddr = "EMAIL ADDRESS YOU SEND TO"
# cc = "yash@stones2milestones.com"
for index, row in df.iterrows():
    print(row["Name"], row["Email"])

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
    msg['Subject'] = "Request for meeting to introduce our mission '''Creating a Nation of Readers'''"
    body = """\
            <html>
              <head></head>
              <body>
              <table class="m_-7483528846982294712m_2706618194857576682nl-container" style="border-collapse:collapse;table-layout:fixed;border-spacing:0;vertical-align:top;min-width:320px;Margin:0 auto;background-color:#ffffff;width:100%" cellpadding="0" cellspacing="0">
	<tbody>
	<tr style="vertical-align:top">
		<td style="word-break:break-word;border-collapse:collapse!important;vertical-align:top">
    

    <div style="background-color:transparent">
      <div style="Margin:0 auto;min-width:320px;max-width:620px;word-wrap:break-word;word-break:break-word;background-color:transparent" class="m_-7483528846982294712m_2706618194857576682block-grid m_-7483528846982294712m_2706618194857576682two-up">
        <div style="border-collapse:collapse;display:table;width:100%;background-color:transparent">
          

              
            <div class="m_-7483528846982294712m_2706618194857576682col m_-7483528846982294712m_2706618194857576682num6" style="max-width:320px;min-width:310px;display:table-cell;vertical-align:top">
              <div style="background-color:transparent;width:100%!important">
              <div style="border-top:0px solid transparent;border-left:0px solid transparent;border-bottom:0px solid transparent;border-right:0px solid transparent;padding-top:5px;padding-bottom:5px;padding-right:0px;padding-left:0px">

                  
                    <div align="left" class="m_-7483528846982294712m_2706618194857576682img-container m_-7483528846982294712m_2706618194857576682left m_-7483528846982294712m_2706618194857576682fixedwidth" style="padding-right:0px;padding-left:0px">

  <a href="http://api.sx8.email/api/v1/track/campaign/click/8AJ0HoQN9mJgHucmwly1VK/5Lv9bBRZLZ5qwNbMjkJ2Ms" target="_blank" data-saferedirecturl="https://www.google.com/url?hl=en&amp;q=http://api.sx8.email/api/v1/track/campaign/click/8AJ0HoQN9mJgHucmwly1VK/5Lv9bBRZLZ5qwNbMjkJ2Ms&amp;source=gmail&amp;ust=1522311455304000&amp;usg=AFQjCNFVSkcVyASYXBfjsI1RftNCkzi2OQ">
    <img class="m_-7483528846982294712m_2706618194857576682left m_-7483528846982294712m_2706618194857576682fixedwidth CToWUd" align="left" border="0" src="https://ci5.googleusercontent.com/proxy/9JYo4H-KvWxZGngMxxi8KQNQZN0GTq_2QZNxnQejirMSFpVRJtHimWyHMYr_DdYaEk8bqQlTaJHsgR7dKEvhzwzoQhgJg4lhxGKWCr91FzF1G132uYh-9mcufE4EiOKTENcge7QpEPgxPZGWy4mW3BJa10Tcl0-bhLXcLqkH43yr1D6MmyV3U6frLO9PoPz6CZwDwke5F5O8fI92niZ-7sFUC1MrtRJY-dKALLg9LoEN1Le7-1I0QVtYWfIWxjRSYcNKrd1twWHL4hS5HpTs8YyO1Yc4ewNYRVg=s0-d-e1-ft#https://pro-bee-user-content-eu-west-1.s3.amazonaws.com/public/users/Integrators/840f4477-2071-4b5b-a7c9-79cd553fea12/9IJZLz6h3PYbcMOwkQEghU/editor_images/59dcea26-54b5-45cc-801b-9a170ac87978.png" alt="Image" title="Image" style="outline:none;text-decoration:none;clear:both;display:block!important;border:none;height:auto;float:none;width:100%;max-width:232.5px" width="232.5">
  </a>

</div>

                  
              </div>
              </div>
            </div>
              
            <div class="m_-7483528846982294712m_2706618194857576682col m_-7483528846982294712m_2706618194857576682num6" style="max-width:320px;min-width:310px;display:table-cell;vertical-align:top">
              <div style="background-color:transparent;width:100%!important">
              <div style="border-top:0px solid transparent;border-left:0px solid transparent;border-bottom:0px solid transparent;border-right:0px solid transparent;padding-top:5px;padding-bottom:5px;padding-right:0px;padding-left:0px">

                  
                    <div>
	
	<div style="color:#555555;line-height:120%;font-family:'Montserrat','Trebuchet MS','Lucida Grande','Lucida Sans Unicode','Lucida Sans',Tahoma,sans-serif;padding-right:10px;padding-left:10px;padding-top:10px;padding-bottom:10px">	
		<div style="font-size:12px;line-height:14px;font-family:Montserrat,'Trebuchet MS','Lucida Grande','Lucida Sans Unicode','Lucida Sans',Tahoma,sans-serif;color:#555555;text-align:left"><p style="margin:0;font-size:12px;line-height:14px;text-align:right"><span style="color:rgb(66,172,78);font-size:12px;line-height:14px"><strong><span style="font-size:28px;line-height:33px">Creating a Nation of Readers</span></strong></span></p></div>	
	</div>
	
</div>
                  
              </div>
              </div>
            </div>
          
        </div>
      </div>
    </div>    <div style="background-color:transparent">
      <div style="Margin:0 auto;min-width:320px;max-width:620px;word-wrap:break-word;word-break:break-word;background-color:transparent" class="m_-7483528846982294712m_2706618194857576682block-grid">
        <div style="border-collapse:collapse;display:table;width:100%;background-color:transparent">
          

              
            <div class="m_-7483528846982294712m_2706618194857576682col m_-7483528846982294712m_2706618194857576682num12" style="min-width:320px;max-width:620px;display:table-cell;vertical-align:top">
              <div style="background-color:transparent;width:100%!important">
              <div style="border-top:0px solid transparent;border-left:0px solid transparent;border-bottom:0px solid transparent;border-right:0px solid transparent;padding-top:5px;padding-bottom:5px;padding-right:0px;padding-left:0px">

                  
                    
<table border="0" cellpadding="0" cellspacing="0" width="100%" class="m_-7483528846982294712m_2706618194857576682divider" style="border-collapse:collapse;table-layout:fixed;border-spacing:0;vertical-align:top;min-width:100%">
    <tbody>
        <tr style="vertical-align:top">
            <td class="m_-7483528846982294712m_2706618194857576682divider_inner" style="word-break:break-word;border-collapse:collapse!important;vertical-align:top;padding-right:10px;padding-left:10px;padding-top:10px;padding-bottom:10px;min-width:100%">
                <table class="m_-7483528846982294712m_2706618194857576682divider_content" align="center" border="0" cellpadding="0" cellspacing="0" width="100%" style="border-collapse:collapse;table-layout:fixed;border-spacing:0;vertical-align:top;border-top:1px dashed #dddddd">
                    <tbody>
                        <tr style="vertical-align:top">
                            <td style="word-break:break-word;border-collapse:collapse!important;vertical-align:top">
                                <span></span>
                            </td>
                        </tr>
                    </tbody>
                </table>
            </td>
        </tr>
    </tbody>
</table>
                  
              </div>
              </div>
            </div>
          
        </div>
      </div>
    </div>    <div style="background-color:transparent">
      <div style="Margin:0 auto;min-width:320px;max-width:620px;word-wrap:break-word;word-break:break-word;background-color:transparent" class="m_-7483528846982294712m_2706618194857576682block-grid">
        <div style="border-collapse:collapse;display:table;width:100%;background-color:transparent">
          

              
            <div class="m_-7483528846982294712m_2706618194857576682col m_-7483528846982294712m_2706618194857576682num12" style="min-width:320px;max-width:620px;display:table-cell;vertical-align:top">
              <div style="background-color:transparent;width:100%!important">
              <div style="border-top:0px solid transparent;border-left:0px solid transparent;border-bottom:0px solid transparent;border-right:0px solid transparent;padding-top:5px;padding-bottom:5px;padding-right:0px;padding-left:0px">

                  
                    <div align="center" class="m_-7483528846982294712m_2706618194857576682img-container m_-7483528846982294712m_2706618194857576682center m_-7483528846982294712m_2706618194857576682autowidth m_-7483528846982294712m_2706618194857576682fullwidth" style="padding-right:0px;padding-left:0px">

  <img class="m_-7483528846982294712m_2706618194857576682center m_-7483528846982294712m_2706618194857576682autowidth m_-7483528846982294712m_2706618194857576682fullwidth CToWUd a6T" align="center" border="0" src="https://ci4.googleusercontent.com/proxy/AsTZ-3N-Bslqo6sEkIDi26OqznO75wMZca0xXBnLP9g_FeR-xmOTygB4LDHXFLUfjBURrjf70JSSPxcp4uejuQkKgmjIPeGlonK7jRD2FESIEI_oA8Hychd6IMTanHUhi4R3jII3MdaV47kIUeNdmPb6MdHnL_nD_eW9bshGSsFY-oh4FMaiOAdaJafgzoNZcSPJdOG_2yTIh_ZzDI9HVCf8T1bExibn3kENkZ1x8N-_LDD-lDIexbdR=s0-d-e1-ft#https://pro-bee-user-content-eu-west-1.s3.amazonaws.com/public/users/Integrators/840f4477-2071-4b5b-a7c9-79cd553fea12/9IJZLz6h3PYbcMOwkQEghU/Webminar-MMPANT-63.jpg" alt="Image" title="Image" style="outline:none;text-decoration:none;clear:both;display:block!important;border:0;height:auto;float:none;width:100%;max-width:620px" width="620" tabindex="0"><div class="a6S" dir="ltr" style="opacity: 0.01; left: 801px; top: 534px;"><div id=":5m" class="T-I J-J5-Ji aQv T-I-ax7 L3 a5q" role="button" tabindex="0" aria-label="Download attachment " data-tooltip-class="a1V" data-tooltip="Download"><div class="aSK J-J5-Ji aYr"></div></div></div>

</div>

                  
              </div>
              </div>
            </div>
          
        </div>
      </div>
    </div>    <div style="background-color:transparent">
      <div style="Margin:0 auto;min-width:320px;max-width:620px;word-wrap:break-word;word-break:break-word;background-color:transparent" class="m_-7483528846982294712m_2706618194857576682block-grid">
        <div style="border-collapse:collapse;display:table;width:100%;background-color:transparent">
          

              
            <div class="m_-7483528846982294712m_2706618194857576682col m_-7483528846982294712m_2706618194857576682num12" style="min-width:320px;max-width:620px;display:table-cell;vertical-align:top">
              <div style="background-color:transparent;width:100%!important">
              <div style="border-top:0px solid transparent;border-left:0px solid transparent;border-bottom:0px solid transparent;border-right:0px solid transparent;padding-top:5px;padding-bottom:5px;padding-right:0px;padding-left:0px">

                  
                    
<div align="center" class="m_-7483528846982294712m_2706618194857576682button-container m_-7483528846982294712m_2706618194857576682center" style="padding-right:10px;padding-left:10px;padding-top:10px;padding-bottom:10px">
  
    <a href="http://api.sx8.email/api/v1/track/campaign/click/c9mj20bWRHltqDtlkBfmxO/5Lv9bBRZLZ5qwNbMjkJ2Ms" style="display:block;text-decoration:none;text-align:center;color:#ffffff;background-color:#42ac4e;border-radius:4px;max-width:232px;width:122px;width:auto;border-top:0px solid transparent;border-right:0px solid transparent;border-bottom:0px solid transparent;border-left:0px solid transparent;padding-top:5px;padding-right:55px;padding-bottom:5px;padding-left:55px;font-family:'Lato',Tahoma,Verdana,Segoe,sans-serif" target="_blank" data-saferedirecturl="https://www.google.com/url?hl=en&amp;q=http://api.sx8.email/api/v1/track/campaign/click/c9mj20bWRHltqDtlkBfmxO/5Lv9bBRZLZ5qwNbMjkJ2Ms&amp;source=gmail&amp;ust=1522311455304000&amp;usg=AFQjCNHu45X9s-t-yRULAXdowxUP_zrf3g">
      <span style="font-size:16px;line-height:32px"><span style="font-size:20px;line-height:40px">Register Now</span></span>
    </a>
  
</div>

                  
                  
                    <div>
	
	<div style="font-family:'Roboto',Tahoma,Verdana,Segoe,sans-serif;line-height:150%;color:#71777d;padding-right:10px;padding-left:10px;padding-top:10px;padding-bottom:0px">	
		<div style="line-height:18px;font-size:12px;color:#71777d;font-family:'Roboto',Tahoma,Verdana,Segoe,sans-serif;text-align:left"><p style="margin:0;font-size:12px;line-height:18px;text-align:center">&nbsp;<br></p><p style="margin:0;font-size:12px;line-height:18px"><span style="font-size:14px;line-height:21px;color:rgb(0,0,0)">Dear Educator,</span></p><p style="margin:0;font-size:12px;line-height:18px">&nbsp;<br></p><p style="margin:0;font-size:12px;line-height:18px"><span style="font-size:14px;line-height:21px;color:rgb(0,0,0)"><em>We invite you to the second edition of our Reading First Webinar Series. Thank you so much for the overwhelming response to the first session with Jagruti Gala on the 17th of March. It was a thoroughly engaging session. We have shared the details of the recording and extra resources below the invite.</em>&nbsp;</span></p><p style="margin:0;font-size:12px;line-height:18px">&nbsp;<br></p><p style="margin:0;font-size:12px;line-height:18px"><span style="font-size:14px;line-height:21px;color:rgb(0,0,0)">Technology powered by Artificial Intelligence has started driving the way people live, the way companies hire and the way new products are developed.</span></p><p style="margin:0;font-size:12px;line-height:18px">&nbsp;<br></p><p style="margin:0;font-size:12px;line-height:18px"><span style="font-size:14px;line-height:21px;color:rgb(0,0,0)">Headlines like “Robots can now read better than humans, putting millions of jobs at risk,” and “Computers are getting better than humans at reading.” are to be seen more and more often. As we know, reading is crucial in developing rational and logical thinking. With an education system that has not undergone significant changes over the past few decades, how do we ensure that our children are reading enough to be lifelong learners and stay ahead of the curve?</span></p><p style="margin:0;line-height:18px;text-align:left;font-size:12px">&nbsp;<br></p><p style="margin:0;font-size:12px;line-height:18px;text-align:left"><span style="font-size:14px;line-height:21px;color:rgb(0,0,0)"><strong><span style="line-height:21px;font-size:14px">Join us to learn more about:</span></strong></span></p><ol><li style="font-size:12px;line-height:21px;text-align:left"><span style="font-size:14px;line-height:21px;color:rgb(0,0,0)"><strong><span style="line-height:21px;font-size:14px">Skills needed to succeed in an AI-powered world</span></strong></span></li><li style="font-size:12px;line-height:21px;text-align:left"><span style="font-size:14px;line-height:21px;color:rgb(0,0,0)"><strong><span style="line-height:21px;font-size:14px">&nbsp;Relationship between reading, academic and professional success, and a happy life</span></strong></span></li><li style="font-size:12px;line-height:21px;text-align:left"><span style="font-size:14px;line-height:21px;color:rgb(0,0,0)"><strong><span style="line-height:21px;font-size:14px">&nbsp;Role of educators and parents in helping children balance the traditional academic system with the needs of <span class="aBn" data-term="goog_45708834" tabindex="0"><span class="aQJ">tomorrow</span></span></span></strong></span></li></ol><p style="margin:0;font-size:12px;line-height:18px;text-align:center"><span style="color:rgb(0,0,0);font-size:12px;line-height:18px"><strong><span style="font-size:12px;line-height:18px"><span style="font-size:14px;line-height:21px">DATE</span><span style="font-size:14px;line-height:21px"></span><span style="font-size:14px;line-height:21px"> -&nbsp;</span><span style="font-size:14px;line-height:21px"><span class="aBn" data-term="goog_45708835" tabindex="0"><span class="aQJ">Saturday, 7th April 2018</span></span></span></span></strong></span></p><p style="margin:0;font-size:12px;line-height:18px;text-align:center"><span style="color:rgb(0,0,0);font-size:12px;line-height:18px"><strong><span style="font-size:12px;line-height:18px"><span style="font-size:14px;line-height:21px">TIME-&nbsp;</span><span style="font-size:14px;line-height:21px"><span class="aBn" data-term="goog_45708836" tabindex="0"><span class="aQJ">11:00 AM</span></span> - 12:15 Noon IST</span></span></strong></span></p><p style="margin:0;font-size:12px;line-height:18px;text-align:center"><span style="color:rgb(0,0,0);font-size:12px;line-height:18px"><strong>&nbsp;</strong></span><br></p><p style="margin:0;font-size:14px;line-height:21px;text-align:center"><strong><span style="color:rgb(0,0,0);font-size:12px;line-height:18px"><span style="font-size:14px;line-height:21px">Featured Speaker -<a style="color:#42ac4e;color:#42ac4e;color:#42ac4e;color:#42ac4e;color:#42ac4e;color:#42ac4e;color:#42ac4e;color:#42ac4e;color:#42ac4e;color:#42ac4e;color:#42ac4e;color:#42ac4e;color:#42ac4e;color:#42ac4e;color:#42ac4e;text-decoration:underline" href="http://api.sx8.email/api/v1/track/campaign/click/nho8EHE1GT9CSVWvJWYQvt/5Lv9bBRZLZ5qwNbMjkJ2Ms" rel="noopener" target="_blank" data-saferedirecturl="https://www.google.com/url?hl=en&amp;q=http://api.sx8.email/api/v1/track/campaign/click/nho8EHE1GT9CSVWvJWYQvt/5Lv9bBRZLZ5qwNbMjkJ2Ms&amp;source=gmail&amp;ust=1522311455304000&amp;usg=AFQjCNEvp0jIkdpo9bRmcjxhXrP_N2RPFA">Prof. (Dr.) M.M. Pant﻿</a><br>Ph.D. from IIT, Roorkee, an ex-faculty member at IIT, Kanpur and a member of the Board of Governors at IIT, Delhi</span></span></strong></p><p style="margin:0;font-size:12px;line-height:18px">&nbsp;<br></p><p style="margin:0;font-size:12px;line-height:18px"><span style="font-size:16px;line-height:24px;color:rgb(0,0,0)">I</span><span style="font-size:16px;line-height:24px;color:rgb(0,0,0)">deal for school leaders &amp; decision makers including, principals, academic coordinators and management.</span></p><p style="margin:0;font-size:12px;line-height:18px">&nbsp;<br></p><p style="margin:0;font-size:12px;line-height:18px"><span style="font-size:11px;line-height:16px"><strong><span style="line-height:16px;color:rgb(0,0,0);font-size:11px">*<em>Limited slots available on first come first&nbsp; serve basis. Request you to register as soon as possible.</em></span></strong></span></p><p style="margin:0;font-size:12px;line-height:18px"><br></p></div>	
	</div>
	
</div>
                  
                  
                    
<div align="center" class="m_-7483528846982294712m_2706618194857576682button-container m_-7483528846982294712m_2706618194857576682center" style="padding-right:10px;padding-left:10px;padding-top:10px;padding-bottom:10px">
  
    <a href="http://api.sx8.email/api/v1/track/campaign/click/c9mj20bWRHltqDtlkBfmxO/5Lv9bBRZLZ5qwNbMjkJ2Ms" style="display:block;text-decoration:none;text-align:center;color:#ffffff;background-color:#42ac4e;border-radius:4px;max-width:232px;width:122px;width:auto;border-top:0px solid transparent;border-right:0px solid transparent;border-bottom:0px solid transparent;border-left:0px solid transparent;padding-top:5px;padding-right:55px;padding-bottom:5px;padding-left:55px;font-family:'Lato',Tahoma,Verdana,Segoe,sans-serif" target="_blank" data-saferedirecturl="https://www.google.com/url?hl=en&amp;q=http://api.sx8.email/api/v1/track/campaign/click/c9mj20bWRHltqDtlkBfmxO/5Lv9bBRZLZ5qwNbMjkJ2Ms&amp;source=gmail&amp;ust=1522311455304000&amp;usg=AFQjCNHu45X9s-t-yRULAXdowxUP_zrf3g">
      <span style="font-size:16px;line-height:32px"><span style="font-size:20px;line-height:40px">Register Now</span></span>
    </a>
  
</div>

                  
                  
                    
<table border="0" cellpadding="0" cellspacing="0" width="100%" class="m_-7483528846982294712m_2706618194857576682divider" style="border-collapse:collapse;table-layout:fixed;border-spacing:0;vertical-align:top;min-width:100%">
    <tbody>
        <tr style="vertical-align:top">
            <td class="m_-7483528846982294712m_2706618194857576682divider_inner" style="word-break:break-word;border-collapse:collapse!important;vertical-align:top;padding-right:10px;padding-left:10px;padding-top:10px;padding-bottom:10px;min-width:100%">
                <table class="m_-7483528846982294712m_2706618194857576682divider_content" align="center" border="0" cellpadding="0" cellspacing="0" width="100%" style="border-collapse:collapse;table-layout:fixed;border-spacing:0;vertical-align:top;border-top:1px solid #bbbbbb">
                    <tbody>
                        <tr style="vertical-align:top">
                            <td style="word-break:break-word;border-collapse:collapse!important;vertical-align:top">
                                <span></span>
                            </td>
                        </tr>
                    </tbody>
                </table>
            </td>
        </tr>
    </tbody>
</table>
                  
                  
                    <div>
	
	<div style="color:#555555;line-height:150%;font-family:'Roboto',Tahoma,Verdana,Segoe,sans-serif;padding-right:10px;padding-left:10px;padding-top:10px;padding-bottom:10px">	
		<div style="font-size:12px;line-height:18px;font-family:Roboto,Tahoma,Verdana,Segoe,sans-serif;color:#555555;text-align:left"><p style="margin:0;font-size:14px;line-height:21px"><span style="color:rgb(0,0,0);font-size:16px;line-height:24px"><span style="color:rgb(0,128,0);font-size:16px;line-height:24px">Reading First Webinar #1:</span> </span></p><p style="margin:0;font-size:14px;line-height:21px"><span style="color:rgb(0,0,0);font-size:14px;line-height:21px"><strong><span style="font-size:14px;line-height:21px">Connecting the Dots Between Reading &amp; Academic Achievement&nbsp;</span></strong></span></p><p style="margin:0;font-size:14px;line-height:21px"><span style="color:rgb(0,0,0);font-size:14px;line-height:21px"><strong><span style="font-size:14px;line-height:21px">With Jagruti Gala on 17th March, 2017</span></strong></span></p></div>	
	</div>
	
</div>
                  
                  
                    
<div align="center" class="m_-7483528846982294712m_2706618194857576682button-container m_-7483528846982294712m_2706618194857576682center" style="padding-right:10px;padding-left:10px;padding-top:10px;padding-bottom:10px">
  
    <a href="http://api.sx8.email/api/v1/track/campaign/click/O8Gg6d2hq1KaD8tK2iDIAx/5Lv9bBRZLZ5qwNbMjkJ2Ms" style="display:block;text-decoration:none;text-align:center;color:#ffffff;background-color:#42ac4e;border-radius:4px;max-width:312px;width:272px;width:auto;border-top:0px solid transparent;border-right:0px solid transparent;border-bottom:0px solid transparent;border-left:0px solid transparent;padding-top:5px;padding-right:20px;padding-bottom:5px;padding-left:20px;font-family:'Lato',Tahoma,Verdana,Segoe,sans-serif" target="_blank" data-saferedirecturl="https://www.google.com/url?hl=en&amp;q=http://api.sx8.email/api/v1/track/campaign/click/O8Gg6d2hq1KaD8tK2iDIAx/5Lv9bBRZLZ5qwNbMjkJ2Ms&amp;source=gmail&amp;ust=1522311455305000&amp;usg=AFQjCNEX-IMnu5qlFSLooRPCUbrYVFlWsg">
      <span style="font-size:16px;line-height:32px"><span style="font-size:16px;line-height:32px">Webinar Recording &amp; Extra Resources</span></span>
    </a>
  
</div>

                  
              </div>
              </div>
            </div>
          
        </div>
      </div>
    </div>    <div style="background-color:transparent">
      <div style="Margin:0 auto;min-width:320px;max-width:620px;word-wrap:break-word;word-break:break-word;background-color:transparent" class="m_-7483528846982294712m_2706618194857576682block-grid">
        <div style="border-collapse:collapse;display:table;width:100%;background-color:transparent">
          

              
            <div class="m_-7483528846982294712m_2706618194857576682col m_-7483528846982294712m_2706618194857576682num12" style="min-width:320px;max-width:620px;display:table-cell;vertical-align:top">
              <div style="background-color:transparent;width:100%!important">
              <div style="border-top:0px solid transparent;border-left:0px solid transparent;border-bottom:0px solid transparent;border-right:0px solid transparent;padding-top:5px;padding-bottom:5px;padding-right:0px;padding-left:0px">

                  
                    
<table border="0" cellpadding="0" cellspacing="0" width="100%" class="m_-7483528846982294712m_2706618194857576682divider" style="border-collapse:collapse;table-layout:fixed;border-spacing:0;vertical-align:top;min-width:100%">
    <tbody>
        <tr style="vertical-align:top">
            <td class="m_-7483528846982294712m_2706618194857576682divider_inner" style="word-break:break-word;border-collapse:collapse!important;vertical-align:top;padding-right:10px;padding-left:10px;padding-top:10px;padding-bottom:10px;min-width:100%">
                <table class="m_-7483528846982294712m_2706618194857576682divider_content" height="0px" align="center" border="0" cellpadding="0" cellspacing="0" width="100%" style="border-collapse:collapse;table-layout:fixed;border-spacing:0;vertical-align:top;border-top:1px solid #bbbbbb">
                    <tbody>
                        <tr style="vertical-align:top">
                            <td style="word-break:break-word;border-collapse:collapse!important;vertical-align:top;font-size:0px;line-height:0px">
                                <span>&nbsp;</span>
                            </td>
                        </tr>
                    </tbody>
                </table>
            </td>
        </tr>
    </tbody>
</table>
                  
                  
                    
<div align="center" style="padding-right:10px;padding-left:10px;padding-bottom:5px">
  <div style="line-height:5px;font-size:1px">&nbsp;</div>
  <div style="display:table;max-width:151px">
  
    <table align="left" border="0" cellspacing="0" cellpadding="0" width="32" height="32" style="border-collapse:collapse;table-layout:fixed;border-spacing:0;vertical-align:top;Margin-right:5px">
      <tbody><tr style="vertical-align:top"><td align="left" valign="middle" style="word-break:break-word;border-collapse:collapse!important;vertical-align:top">
        <a href="http://api.sx8.email/api/v1/track/campaign/click/yq2JQriiv2P8HSsC5fM7nb/5Lv9bBRZLZ5qwNbMjkJ2Ms" title="Facebook" target="_blank" data-saferedirecturl="https://www.google.com/url?hl=en&amp;q=http://api.sx8.email/api/v1/track/campaign/click/yq2JQriiv2P8HSsC5fM7nb/5Lv9bBRZLZ5qwNbMjkJ2Ms&amp;source=gmail&amp;ust=1522311455305000&amp;usg=AFQjCNG1alGHp5bNuO0Cjo25lWh354rsug">
          <img src="https://ci6.googleusercontent.com/proxy/u-0pR7H_IVV0SwqjC-xZy6subarDmQtFnXn9xDkK-zSj2otaH24x9aCsofbktF56PuODMqsNqqDPqWn5dOYPUj49Aj8XrsmHrindvBukwnoUtg6ZTW3cZGIPnvJXuWU4kc4jbtWlr6P5tsYMpRpWkNmfQZMO7-_tAIcSnX4gofYn-hik2xkJgrW2sSV51o4=s0-d-e1-ft#https://d2fi4ri5dhpqd1.cloudfront.net/public/resources/social-networks-icon-sets/t-only-logo-default-gray/facebook@2x.png" alt="Facebook" title="Facebook" width="32" style="outline:none;text-decoration:none;clear:both;display:block!important;border:none;height:auto;float:none;max-width:32px!important" class="CToWUd">
        </a>
      <div style="line-height:5px;font-size:1px">&nbsp;</div>
      </td></tr>
    </tbody></table>
      
    <table align="left" border="0" cellspacing="0" cellpadding="0" width="32" height="32" style="border-collapse:collapse;table-layout:fixed;border-spacing:0;vertical-align:top;Margin-right:5px">
      <tbody><tr style="vertical-align:top"><td align="left" valign="middle" style="word-break:break-word;border-collapse:collapse!important;vertical-align:top">
        <a href="http://api.sx8.email/api/v1/track/campaign/click/RLxvo002nq36NRh3q7z5k7/5Lv9bBRZLZ5qwNbMjkJ2Ms" title="Twitter" target="_blank" data-saferedirecturl="https://www.google.com/url?hl=en&amp;q=http://api.sx8.email/api/v1/track/campaign/click/RLxvo002nq36NRh3q7z5k7/5Lv9bBRZLZ5qwNbMjkJ2Ms&amp;source=gmail&amp;ust=1522311455305000&amp;usg=AFQjCNFQ2uVUKPihgw4u9Sslafjzu_yLUQ">
          <img src="https://ci6.googleusercontent.com/proxy/cvJJ9MiaS4SSYHREKm1inf1qi_Gua_lmSmBxtDAova2Cs2--eHjnXshZDg2290AtHKxpJrOiXd-sHtNtgCOQdlmHw7WRrsFqWjoBPx-Ertaf6cDNSMt3cv3_pN-mRVwoYw-wU2Z_puFz7oZxlFmf5TO0AdP_ULsu_UQZTWF-GItfBooEUikrHi2vVP-KGw=s0-d-e1-ft#https://d2fi4ri5dhpqd1.cloudfront.net/public/resources/social-networks-icon-sets/t-only-logo-default-gray/twitter@2x.png" alt="Twitter" title="Twitter" width="32" style="outline:none;text-decoration:none;clear:both;display:block!important;border:none;height:auto;float:none;max-width:32px!important" class="CToWUd">
        </a>
      <div style="line-height:5px;font-size:1px">&nbsp;</div>
      </td></tr>
    </tbody></table>
      
    <table align="left" border="0" cellspacing="0" cellpadding="0" width="32" height="32" style="border-collapse:collapse;table-layout:fixed;border-spacing:0;vertical-align:top;Margin-right:0">
      <tbody><tr style="vertical-align:top"><td align="left" valign="middle" style="word-break:break-word;border-collapse:collapse!important;vertical-align:top">
        <a href="http://api.sx8.email/api/v1/track/campaign/click/qJ96qMLTjlTiY29RSW0LEF/5Lv9bBRZLZ5qwNbMjkJ2Ms" title="Web Site" target="_blank" data-saferedirecturl="https://www.google.com/url?hl=en&amp;q=http://api.sx8.email/api/v1/track/campaign/click/qJ96qMLTjlTiY29RSW0LEF/5Lv9bBRZLZ5qwNbMjkJ2Ms&amp;source=gmail&amp;ust=1522311455305000&amp;usg=AFQjCNHqVOGcANZ7c9Join-OuS-FT-x6Zg">
          <img src="https://ci6.googleusercontent.com/proxy/EkZcx_3fwnqo8R1I65JlZuSDvwoJlAtg1aeGCueW0XGLicZbvSCn4j3je5tDLL48z-Az6W3cIRSmKnsJbpp6En-Xuzv0V7y0Q-ZI6ALP1J9VzGBPWaxPN5d37aMJkzXeEJa1bxu0kjK8Z7ML5tvAXwcCSql8My_WO7dH3yGFDq_WvacxyycBZduD9uJfsA=s0-d-e1-ft#https://d2fi4ri5dhpqd1.cloudfront.net/public/resources/social-networks-icon-sets/t-only-logo-default-gray/website@2x.png" alt="Web Site" title="Web Site" width="32" style="outline:none;text-decoration:none;clear:both;display:block!important;border:none;height:auto;float:none;max-width:32px!important" class="CToWUd">
        </a>
      <div style="line-height:5px;font-size:1px">&nbsp;</div>
      </td></tr>
    </tbody></table>
    
  </div>
</div>
                  
              </div>
              </div>
            </div>
          
        </div>
      </div>
    </div>    <div style="background-color:transparent">
      <div style="Margin:0 auto;min-width:320px;max-width:620px;word-wrap:break-word;word-break:break-word;background-color:transparent" class="m_-7483528846982294712m_2706618194857576682block-grid">
        <div style="border-collapse:collapse;display:table;width:100%;background-color:transparent">
          

              
            <div class="m_-7483528846982294712m_2706618194857576682col m_-7483528846982294712m_2706618194857576682num12" style="min-width:320px;max-width:620px;display:table-cell;vertical-align:top">
              <div style="background-color:transparent;width:100%!important">
              <div style="border-top:0px solid transparent;border-left:0px solid transparent;border-bottom:0px solid transparent;border-right:0px solid transparent;padding-top:0px;padding-bottom:0px;padding-right:0px;padding-left:0px">

                  
                    <div align="center" class="m_-7483528846982294712m_2706618194857576682img-container m_-7483528846982294712m_2706618194857576682center m_-7483528846982294712m_2706618194857576682fixedwidth" style="padding-right:0px;padding-left:0px">

  <a href="http://api.sx8.email/api/v1/track/campaign/click/Fzy8ZvlZtpJBHrcyfCiM0S/5Lv9bBRZLZ5qwNbMjkJ2Ms" target="_blank" data-saferedirecturl="https://www.google.com/url?hl=en&amp;q=http://api.sx8.email/api/v1/track/campaign/click/Fzy8ZvlZtpJBHrcyfCiM0S/5Lv9bBRZLZ5qwNbMjkJ2Ms&amp;source=gmail&amp;ust=1522311455305000&amp;usg=AFQjCNEgKpTFvMrO1kqhuKZA67lequGbtQ">
    <img class="m_-7483528846982294712m_2706618194857576682center m_-7483528846982294712m_2706618194857576682fixedwidth CToWUd" align="center" border="0" src="https://ci5.googleusercontent.com/proxy/MaxZTv3qujpDZ-YbhUX8yPr81Gaxa9bnKV0WZCw3WY33JUvN5_Y__Xh5knkNqF84nLOiLUYCg1MCXVDZ5rf1zpXSMsML0LNih7kfx9jFkGaJX5LAkndJPO34DigWNi7MuvdhAa9uW6MKZ2hwMglSitiRXu6K6nNw3FfqWTS6GuYauqHQ5QKjzY-yn3b9lkCWBKY7h8ro7JFVSRMb6sGMK2bTmafX0lcjsIShKxddOI4Ik2Wbj7lKPSyylKH-uBWwO5LCThkLeHqt-7f4GzyuGsWLu40WZkeWnjI=s0-d-e1-ft#https://pro-bee-user-content-eu-west-1.s3.amazonaws.com/public/users/Integrators/840f4477-2071-4b5b-a7c9-79cd553fea12/9IJZLz6h3PYbcMOwkQEghU/editor_images/252deeb7-bc7a-4422-9330-521f87e1bbea.png" alt="Image" title="Image" style="outline:none;text-decoration:none;clear:both;display:block!important;border:none;height:auto;float:none;width:100%;max-width:403px" width="403">
  </a>

</div>

                  
              </div>
              </div>
            </div>
          
        </div>
      </div>
    </div>   
		</td>
  </tr>
  </tbody>
  </table>
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
    server.sendmail(fromaddr, toaddr, text)
    print('Success')
    server.quit()