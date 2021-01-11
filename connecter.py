import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode

try:
    connection = mysql.connector.connect(host='192.168.0.16',
                                         database='python',
                                         user='root',
                                         password='')
    mySql_insert_query = """INSERT INTO users (u_name, f_name, l_name, password) values ('goofy', 'george', 'hewitt', 'buddy456')"""

    cursor = connection.cursor()
    cursor.execute(mySql_insert_query)
    connection.commit()
    print("nice one")
    cursor.close()
except mysql.connector.Error as error:
    print("failed")