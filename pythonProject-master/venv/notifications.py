import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class notifications():

    def sendEmail(self,message1):
        sender = 'bfl1-it@amazon.com'
        receivers = ['deltacompu2@gmail.com']

        message = """Subject: SSP printers need your attention


        """ + message1
        try:
            smtpObj = smtplib.SMTP('smtp.amazon.com')
            smtpObj.sendmail(sender, receivers, message)
            print("Successfully sent email")
        except SMTPException:
            print("Error: unable to send email")

