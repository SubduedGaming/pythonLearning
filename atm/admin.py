from connector import *

def input_user():
    global username
    global l_name
    global f_name
    global password
    
    print("You are about to make a new user in the database. Please input a username: ")
    username = input("")
    
    f_name = input("What is the first name? ")
    l_name = input("What is the last name? ")
    password = input("Please make a password: ")
    print([username,
           f_name,
           l_name,
           password])
    
    

def send_data():
    


while connection_success:
    input_user()
    send_data()

