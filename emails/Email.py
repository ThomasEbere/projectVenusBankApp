from email.message import EmailMessage
import smtplib
from random import randint
from users.dependency import Depend

import os


class SendEmail:
    confirmation_code = Depend.generate_account_number()

    def send_email(self):
        # important, you need to send it to a server that knows how to send e-mails for you
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        # don't know how to do it without cleartexting the password and not relying on some json file that you dont git
        # control...
        server.login('waterloobanking@gmail.com', 'gamvqmzsferrqjzv')
        msg = EmailMessage()
        return msg, server

    def accountcreation(self, destination, firstname):
        msg, server = email.send_email()
        message = f"""Hello {firstname},
            Thanks for opening an account with us. We hope you enjoy your banking experience. 
            Your once time password is. Please use this passcode {SendEmail.confirmation_code}
            to confirm your email in the console. 
            Thanks,
             WaterlooBank"""
        msg.set_content(message)

        msg['Subject'] = 'Congratulations on Successfully opening an account'
        msg['From'] = 'waterloobanking@gmail.com'
        msg['To'] = destination
        server.send_message(msg)
        return True

    def updatedbalance(self, destination, balance, firstname, newbalance):
        msg, server = email.send_email()
        message = f"""Hello {firstname},
                Your deposit of ${balance} was successful. Your new balance is ${newbalance}. Continue to enjoy banking 
                with us,
                Thanks,
                 WaterlooBank"""
        msg.set_content(message)

        msg['Subject'] = 'Account|-Operation|Deposit'
        msg['From'] = 'waterloobanking@gmail.com'
        msg['To'] = destination
        server.send_message(msg)
        return True

    def withdraw(self, destination, balance, firstname, newbalance):
        msg, server = email.send_email()
        message = f"""Hello {firstname},
                Your withdrawal of ${balance} was successful. Your new balance is ${newbalance}. Continue to enjoy 
                banking with us Thanks, WaterlooBank"""
        msg.set_content(message)

        msg['Subject'] = 'Account-Operation|Withdrawal'
        msg['From'] = 'waterloobanking@gmail.com'
        msg['To'] = destination
        server.send_message(msg)
        return True

    def transwith(self, destination, balance, firstname, newbalance, receiptfirstname):
        msg, server = email.send_email()
        message = f"""Hello {firstname},
                You successfully transferred  ${balance}  to {receiptfirstname}. Your new balance is ${newbalance}. Continue to enjoy 
                banking with us Thanks, WaterlooBank"""
        msg.set_content(message)

        msg['Subject'] = 'Account-Operation|Transfer'
        msg['From'] = 'waterloobanking@gmail.com'
        msg['To'] = destination
        server.send_message(msg)
        return True

    def transdepo(self, destination, balance, firstname, newbalance, receiptfirstname):
        msg, server = email.send_email()
        message = f"""Hello {receiptfirstname},
                You successfully received  ${balance}  from {firstname}. Your new balance is ${newbalance}. Continue to enjoy 
                banking with us Thanks, WaterlooBank"""
        msg.set_content(message)

        msg['Subject'] = 'Account-Operation|Deposit'
        msg['From'] = 'waterloobanking@gmail.com'
        msg['To'] = destination
        server.send_message(msg)
        return True

    # @staticmethod
    # def generate_account_number():
    #     new_num = randint(10000, 99999)
    #     return new_num


email = SendEmail()
