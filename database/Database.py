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
    def getalldata():
        for doc in connect.createcollection().find():
            print(doc)


connect = Database()

connect.getalldata()
