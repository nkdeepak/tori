"""
    The main class used to send mail to the required user.
"""
import smtplib

class Mail():
    
    def __init__(self):
        pass

    def get_user_email(self):
        pass

    def send_mail(self, to_mail):
        self.to_mail = to_mail
        email_from_addr = "myfromemail@gmail.com"
        email_to_addr = "mytoemail@gmail.com"
        email_smtp_server = "smtp.gmail.com"
        email_smtp_port = "587"
        email_user = "myfromemail"
        email_password = "mypassword"

#Email Subject
email_subject = "Welcome to Python Email Test"

    def format_mail(self):
        pass