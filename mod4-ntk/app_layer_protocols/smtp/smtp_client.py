import smtplib


from_addr = "mconstantin@fullerton.edu"
to_addr = "user@gmail.com"
msg_body = "From: mconstantin@fullerton.edu\r\nTo: mconstantin@cox.net\r\nSubject: Testing my SMTP client!\r\nWorking!"

smtp_client = smtplib.SMTP('smtp.gmail.com', 587)
smtp_client.ehlo()
smtp_client.starttls()
smtp_client.ehlo()
smtp_client.login('user@gmail.com', 'password')
smtp_client.sendmail(from_addr, to_addr, msg_body)
smtp_client.quit()