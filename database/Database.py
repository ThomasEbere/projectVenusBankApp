import mysql.connector
from mysql.connector import Error


class Database:

    def __init__(self, host, database, port, user, password):
        self.host = host
        self.database = database
        self.port = port
        self.user = user
        self.password = password

    @classmethod
    def establishconnection(cls):
        try:
            connection = mysql.connector.connect(host="localhost",
                                                 database="BankApp",
                                                 port="3306",
                                                 user="root",
                                                 password="Prick123$")
            if connection.is_connected():
                db_info = connection.get_server_info()
                print("Connection to mysql server", db_info)
                cursor = connection.cursor()
                cursor.execute("Select database ();")
                record = cursor.fetchone()
                print("You are connected to the database", record)
            return connection

        except Error as e:
            print("Error while connecting to mysql database", e)
        # finally:
        #     if connection.is_connected():
        #         cursor.close()
        #         connection.close()
        #         print("my connection is closed ")
        return e

    @staticmethod
    def createtable():

        CREATE_TABLE = """CREATE TABLE bankvault(
        id int(11) NOT NULL AUTOINCREMENT,
        ACCOUNT_NO INT(11) NOT NULL, 
        FIRST_NAME VARCHAR(255) NOT NULL,
        LAST_NAME VARCHAR(255) NOT NULL,
        ADDRESS VARCHAR(255) NOT NULL,
        EMAIL VARCHAR (255) NOT NULL,
        MOBILE_NUMBER INT(20) NOT NULL,
        PASSWORD VARCHAR (255) NOT NULL, 
        PRIMARY KEY(ACCOUNT_NO))"""

        cursor = connector.cursor()
        result = cursor.execute(CREATE_TABLE)
        print("Table Created")


connector = Database.establishconnection()
Database.createtable()
