from random import randint
import maskpass


class Users:
    deposit = 1000

    def __init__(self, firstname, lastname, email, address, mobile_number, password):
        self.firstname = firstname
        self.lastname = lastname
        self.address = address
        self.email = email
        self.mobile_number = mobile_number
        self.password = password
        self.account_no = self.generate_account_number()

    @classmethod
    def create_account(cls):
        firstname = input("Kindly enter your first Name ")
        lastname = input("Kindly enter your last Name ")
        address = input("Kindly enter your address ")
        email = input("Kindly enter your email address ")
        mobile_number = input("Kindly enter your mobile number ")
        password = input("Enter your password ")
        print(f"""These are the details you entered:
            first Name: {firstname}
            last Name: {lastname}
            Address: {address}
            email:{email}
            mobile Number:{mobile_number}
            password:{password}
            """)
        user_credentials = input("Press Yes if you confirm that they are correct or press No to reenter")
        if user_credentials == "Yes":
            return "Your account has been successfully created"
        else:
            return cls.create_account()

    @staticmethod
    def generate_account_number():
        new_num = randint(10000, 99999)
        return new_num


user = Users.create_account()
