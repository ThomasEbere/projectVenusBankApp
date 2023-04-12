from random import randint
import maskpass
from database import Database
from emails import Email
import dependency
send = Email.SendEmail()

newData = Database.Database()


class Users:
    deposit = 1000

    def __init__(self, firstname, lastname, email, address, mobile_number, password):
        self.firstname = firstname
        self.lastname = lastname
        self.address = address
        self.email = email
        self.mobile_number = mobile_number
        self.password = password

    @classmethod
    def create_account(cls):
        firstname = input("Kindly enter your first Name ")
        lastname = input("Kindly enter your last Name ")
        address = input("Kindly enter your address ")
        email = input("Kindly enter your email address ")
        mobile_number = input("Kindly enter your mobile number ")
        password = input("Enter your password ")
        accountnumber = dependency.Depend.generate_account_number()
        print(f"""These are the details you entered:
            first Name: {firstname}
            last Name: {lastname}
            Address: {address}
            email:{email}
            mobile Number:{mobile_number}
            password:{password}
            Account_number:{accountnumber}
            """)
        user_credentials = input("Press Yes if you confirm that they are correct or press No to reenter")
        if user_credentials == "Yes" or "yes":
            print(user_credentials)
            newuser = Users.converdatatostring(firstname, lastname, address, email, mobile_number, password,
                                               accountnumber,
                                               Users.deposit)
            if newData.insertData(newuser):
                Users.sendconfirmaccount(email, firstname)
                return "Success"
            else:
                return "An Error occurred"
        else:
            return cls.create_account()

    @staticmethod
    def converdatatostring(first_name, last_name, address, email, mobile_number, password, account_number, deposit):
        userdata = {
            "first_Name": first_name,
            "last_Name": last_name,
            "Address": address,
            "email": email,
            "mobile_Number": mobile_number,
            "password": password,
            "Account_Number": account_number,
            "deposit": deposit
        }
        return userdata

    @staticmethod
    def sendconfirmaccount(destination, firstname):

        if __name__ == '__main__':
            print(send.confirmation_code)
            send.send_email(destination, firstname)


user = Users.create_account()
