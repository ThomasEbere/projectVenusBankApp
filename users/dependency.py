from random import randint


class Depend:
    @staticmethod
    def generate_account_number():
        new_num = randint(10000, 99999)
        return new_num
