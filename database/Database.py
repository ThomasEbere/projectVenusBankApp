import mysql.connector
from mysql.connector import Error

from pymongo import MongoClient


class Database(object):

    def createconnection(self):
        client = MongoClient()
        return client

    def createdatabase(self):
        db = connect.createconnection().BankAccount
        return db

    def createcollection(self):
        account_data = connect.createdatabase().account_data
        return account_data

    @staticmethod
    def insertData(data):
        datainserted = connect.createcollection().insert_one(data)
        return datainserted

    @staticmethod
    def checkuser(email):
        if connect.createcollection().find_one({"email": email}):
            data = connect.createcollection().find_one({"email": email})
            return data
        return False

    @staticmethod
    def getallusers():
        for data in connect.createcollection().find():
            print(data)

    @staticmethod
    def updatebalance(email, balance):
        newtopup = connect.createcollection().update_one({"email": email}, {"$set": {"deposit": balance}})
        return newtopup

    @staticmethod
    def checkuseraccount(Account_Number):
        data = connect.createcollection().find_one({"Account_Number": Account_Number})
        return data


connect = Database()
Database.getallusers()
# print(Database.checkuser("kizzito@gmail.com"))
