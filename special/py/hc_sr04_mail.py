import smtplib
from email.mime.text import MIMEText


smtp = smtplib.SMTP('smtp.gmail.com',587)
smtp.ehlo()
smtp.starttls()
        
smtp.login('ssarmango@gmail.com','la609160!')        
msg = MIMEText('hc_sr04_Detected')
msg['Subject'] = 'Hey, you must notify this situation'
msg['To'] = 'codingspecialist@naver.com'
smtp.sendmail('ssarmango@gmail.com', 'codingspecialist@naver.com',msg.as_string())
smtp.quit()
print('send email')
