import json
import os 

def read_file_db(filename):
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            try:
                data = json.load(file)
            except json.JSONDecodeError:
                data = []
    else:
        data = []
    
    return data 

def write_file_db(filename, data):
    if os.path.exists(filename):
        with open(filename, 'w') as file:
            json.dump(data, file, indent=4)

def get_role(filename, email):
    data = read_file_db(filename)
    for user in data:
        if user["email"] == email:
            return user["role"]
    return None  


def checkAccount(filename, email, password):
    data = read_file_db(filename)
    for user in data:
        if user["email"].lower() == email.lower():
            if user["password"] == password:
                return 2;   # success
            else:
                return 1;   # failure password
    return -1; #invalid email address
    

    
