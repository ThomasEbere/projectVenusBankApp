from random import randint
import maskpass
from database import Database
from emails import Email
import dependency

send = Email.SendEmail()

newData = Database.Database()
newData.createconnection()
newData.createcollection()


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
            newuser = Users.converdatatostring(firstname, lastname, address, email, mobile_number, password,
                                               accountnumber,
                                               Users.deposit)
            if not newData.checkuser(email):
                if newData.insertData(newuser):
                    Users.sendconfirmaccount(email, firstname)
                    return "Success"
                else:
                    print("An Error occurred")
                    return cls.create_account()
            else:
                choice = int(input("""User with this email already exist. 
                        Press 1 to log in  or press two to use an email that does not exist to sign up"""))
                if choice == 1:
                    cls.login()
                return cls.create_account()
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
            send.accountcreation(destination, firstname)

    @staticmethod
    def login():
        print("""Welcome to Waterloo Bank. Kindly provide us with the following details to access your account""")
        email = input("Enter your email ")
        password = input("Enter your password ")
        if newData.checkuser(email):
            founddata = newData.checkuser(email)
            keys = ['first_Name', 'password']
            values = list(map(founddata.get, keys))
            firstname, newpass = values
            if password == newpass:
                Users.menu(email, firstname)
            else:
                print("Invalid password. Please check password and enter it again")
                Users.login()
        else:
            print("User does not exit. Please follow the prompt to sign up instead")
            Users.create_account()

    @staticmethod
    def menu(email, firstname):
        menu = """
        
        Press 1 to perform Deposit
        Press 2 to perform Withdrawal
        press 3 to check balance
        Press 4 for transfer
        """
        userchoice = int(input(menu))
        if userchoice == 1:
            Users.accountdeposit(email, firstname)
        elif userchoice == 2:
            Users.withdraw(email, firstname)
        elif userchoice == 3:
            Users.balance(email)
        elif userchoice == 4:
            Users.transfer(email, firstname)

    @staticmethod
    def accountdeposit(email, firstname):
        amount = int(input("Enter amount you want to deposit"))
        currentamount = newData.checkuser(email)['deposit']
        updatedbalance = amount + currentamount
        if newData.updatebalance(email, updatedbalance):
            if send.updatedbalance(email, amount, firstname, updatedbalance):
                Users.usertransactionprompt()

        else:
            print("Deposit failed. Please try again")
            Users.accountdeposit(email, firstname)

    @staticmethod
    def withdraw(email, firstname):
        amount = int(input("Enter amount you want to withdraw"))
        currentamount = newData.checkuser(email)['deposit']
        if currentamount > amount:
            updatedbalance = currentamount - amount
            if newData.updatebalance(email, updatedbalance):
                if send.withdraw(email, amount, firstname, updatedbalance):
                    Users.usertransactionprompt()
            else:
                print("Withdrawal failed. Please try again")
                Users.withdraw(email, firstname)
        else:
            print("Insufficient Balance. Please check balance to know your limit")
            Users.usertransactionprompt()

    @staticmethod
    def balance(email):
        currentamount = newData.checkuser(email)['deposit']
        print("Your current balance is {}".format(currentamount))
        Users.usertransactionprompt()

    @staticmethod
    def usertransactionprompt():
        transaction = int(input("Press 1 to perform another transaction or press 2 to exit "))
        if transaction == 1:
            Users.login()
        else:
            print("Thanks for banking with us ")

    @staticmethod
    def transfer(email, firstname):
        accountnumber = int(
            input("Enter the account number you want to transfer to "))  # Getting the account no to transfer to
        if newData.checkuseraccount(accountnumber):  # Checking that the account no exit
            accountinfo = newData.checkuseraccount(accountnumber)  # Getting account details
            keys = ['first_Name', 'deposit', 'email']
            values = list(map(accountinfo.get, keys))
            receptfirstname, receideposit, receiemail = values
            print(receiemail)
            amountdepo = int(input("Enter the amount you want to send to {} ".format(
                receptfirstname)))  # Getting amount you want to transfer
            currentamount = newData.checkuser(email)['deposit']  # getting your current balance
            if currentamount > amountdepo:  # Checking your current balance
                updatedbalance = currentamount - amountdepo  # perform subtraction
                currentamount = newData.checkuser(receiemail)['deposit']  # get balance of receiver
                updatdbalance = amountdepo + currentamount  # Credit the receiver
                if newData.updatebalance(email, updatedbalance) and newData.updatebalance(receiemail,
                                                                                          updatdbalance):  # update
                    # balance of sender
                    send.transwith(email, amountdepo, firstname, updatedbalance, receptfirstname)
                    send.transdepo(receiemail, amountdepo, firstname, updatdbalance, receptfirstname)
                    print("Successful Transaction")
                else:
                    print("Error performing transaction. Please try again later")
            else:
                print("Insufficient Balance. check balance and try again")
                Users.usertransactionprompt()
        else:
            print("Account does not exit. Check account and try again ")
            Users.transfer(email, firstname)


Users.login()
