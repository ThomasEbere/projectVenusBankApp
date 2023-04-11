from email.message import EmailMessage
import smtplib
from random import randint

import os


class SendEmail:

    def send_email(self, destination, firstname):
        # important, you need to send it to a server that knows how to send e-mails for you
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        # don't know how to do it without cleartexting the password and not relying on some json file that you dont git
        # control...
        server.login('waterloobanking@gmail.com', 'gamvqmzsferrqjzv')
        msg = EmailMessage()
        message = f"""Hello {firstname},
            Thanks for opening an account with us. We hope you enjoy your banking experience. 
            Your once time password is. Please use this passcode \033[1m{SendEmail.generate_account_number()}\033[0m
            to confirm your email in the console. Thanks WaterlooBank"""
        msg.set_content(message)

        msg['Subject'] = 'Account Opening'
        msg['From'] = 'waterloobanking@gmail.com'
        msg['To'] = destination
        server.send_message(msg)
        print("successful")

    @staticmethod
    def generate_account_number():
        new_num = randint(10000, 99999)
        return new_num
