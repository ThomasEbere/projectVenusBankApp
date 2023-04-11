# from random import randint, randrange
#
# newNum= randint(10000, 99999)
# print(newNum)

# import base64
# print(base64.b64encode("mike".encode("utf-8")))
#
# https://stackoverflow.com/questions/157938/hiding-a-password-in-a-python-script-insecure-obfuscation-only

from email.message import EmailMessage
import smtplib
import os


# def send_email(message, destination):
#     # important, you need to send it to a server that knows how to send e-mails for you
#     server = smtplib.SMTP('smtp.gmail.com', 587)
#     server.starttls()
#     # don't know how to do it without cleartexting the password and not relying on some json file that you dont git
#     # control...
#     server.login('waterloobanking@gmail.com', 'gamvqmzsferrqjzv')
#     msg = EmailMessage()
#     message = """How is it going this wonderful day"""
#     msg.set_content(message)
#
#     msg['Subject'] = 'Account Opening'
#     msg['From'] = 'waterloobanking@gmail.com'
#     msg['To'] = destination
#     server.send_message(msg)
#     print("successful")
#
#
# if __name__ == '__main__':
#     send_email('msg', 'tebere.chukwuka@gmail.com')

