from connector import *

f_name = "tom"
l_name = "tit"
password = "took"
username = "shit"
 
    

def send_data():
    global cursor
    add_user = """INSERT INTO users (f_name, l_name, password, username) VALUES (%s, %s, %s, %s).format(record)"""
    cursor.execute(add_user)
    connection.commit
    
def connect():
    global connection
    global cursor
    if connection_success:
        connection = mysql.connector.connect(host='192.168.0.16',
                                         database='python',
                                         user='python',
                                         password='Buddy456')
        cursor = connection.cursor()


while connection_success:
    connect()
    record = (f_name, l_name, password, username)
    #input_user()
    send_data()

