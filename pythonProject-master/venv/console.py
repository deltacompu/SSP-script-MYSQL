import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class notifications2():

    def sendEmail(self,message1):

        sender = 'davsuar@amazon.com'
        receivers = ['deltacompu2@gmail.com']

        message = """ From: IT support BFL1 Subject: SSP printers need your attention


        """ + message1
        try:
            smtpObj = smtplib.SMTP('smtp.amazon.com')
            smtpObj.sendmail(sender, receivers, message)
            print("Successfully sent email")
        except smtplib.SMTPException:
            print("Error: unable to send email")

