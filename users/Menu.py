from users import Users


class Menu:
    def prompt(self):
        menu = """Welcome to Waterloo Bank
                Press 1 to sign up ans create account
                Press 2 to log into your account\n"""
        choice = int(input(menu))
        return choice

    def selection(self):
        choice = dataprompt.prompt()
        if choice == 1:
            Users.Users.create_account()
        elif choice == 2:
            Users.Users.login()
        else:
            print("Invalid input")
            return dataprompt.prompt()


dataprompt = Menu()
dataprompt.selection()
