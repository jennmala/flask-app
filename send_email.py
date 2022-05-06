from email.mime.text import MIMEText
import smtplib

def send_email(email, height, average_height, count):
    from_email='qwe@gmail.com'
    from_password=''
    to_email=email

    subject='Height data'
    message='hey <strong>%s</ strong>.Average <strong>%s</ strong> of <strong>%s</ strong> people.' % (height, average_height, count)
    print(message)

    msg = MIMEText(message, 'html')
    msg['Subject'] = subject
    msg['To'] = to_email
    msg['From'] = from_email

    gmail=smtplib.SMTP('smtp.gmail.com', 465)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(from_password, from_password)
    gmail.send_message(msg)
