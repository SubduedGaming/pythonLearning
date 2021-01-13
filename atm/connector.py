import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode

global connection_success

try:
    connection = mysql.connector.connect(host='192.168.0.16',
                                         database='python',
                                         user='python',
                                         password='Buddy456')
    cursor = connection.cursor()
    connection.commit()
    print("nice one")
    connection_success = True
    cursor.close()
except mysql.connector.Error as error:
    print("failed")