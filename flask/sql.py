# coding=utf-8

import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="dsong"

)
print(mydb)


