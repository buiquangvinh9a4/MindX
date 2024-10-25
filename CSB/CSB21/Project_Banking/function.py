import os 
def checkValidUsername(username, path):
    lst_usernames = []
    with open(path, "r") as fr:
        for line in fr:
            user = line.split(";")[0]
            lst_usernames.append(user)
    
    if username in lst_usernames:
        return True
    return False

def mainMenu():
    
    print("=== MINDX BANKING ===")
    print("1. Create new account")
    print("2. Login")
    print("3. Exit")
    print("=====================")

def menuAccount(username):
    
    print(f"=== WELCOME, {username} ===")
    print("1. Xem thông tin")
    print("2. Nạp tiền")
    print("3. Rút tiền")
    print("4. Chuyển tiền")
    print("5. Thoát")
    print("=====================")

def signUp():
    path = "Project_Banking/list_accounts.txt"
    print("=== SIGN UP ===")
    
    # -> username
    while True:
        username = input("- Username: ")
        if not(checkValidUsername(username, path)):
            if len(username) >= 4:
                break
            else:
                print("Username must be at least 4 characters")
        else:
            print("Username invalid. Please rechoice!")

    # -> password
    while True:
        password = input("- Password: ")
        if len(password) >= 6 and " " not in password:
            break
        else:
            if len(password) < 6:
                print("Password must be at least 6 characters")
            if " " in password:
                print("Password cannot contain space")

    # -> repeat password:
    while True:
        repeat_password = input("- Repeat password: ")
        if repeat_password == password:
            break
        else:
            print("Password does not match!")
    
    # -> STK: ID
    import random
    id = random.randint(100000, 999999)

    # -> Full name
    while True:
        full_name = input("- Full name: ")
        if len(full_name) >= 4:
            break
        else:
            print("Full name must be at least 4 characters")
    
        
    # Correct Account
    with open(path, "a") as fw:
        fw.write(f"{username};{password};{id};{full_name};0\n")
        print(f"Finish. Welcome to MindX Banking, {full_name}")

def get_list_accounts():
    path = "Project_Banking/list_accounts.txt"
    lst_accounts = {}
    with open(path, "r") as fr:
        for line in fr:
            line = line.split(";")
            # username -> line[0]
            # password -> line[1]
            lst_accounts[line[0]] = line[1]
    return lst_accounts

def get_full_list_accounts():
    path = "Project_Banking/list_accounts.txt"
    lst_accounts = []
    with open(path, "r") as fr:
        for line in fr:
            if "\n" in line:
                line = line[:-1]
            line = line.split(";")
            username = line[0]
            password = line[1]
            id = line[2]
            full_name = line[3]
            balance = int(line[4])
            lst_accounts.append([username, password, id, full_name, balance])
    return lst_accounts


def signIn():
    lst_accounts = get_list_accounts()

    print("=== SIGN IN ===")

    # username  -> tồn tại username trong lst_accounts (key)
    count_trial_user = 0
    while True:
        username = input("- Username: ")
        # nếu username đã có trong hệ thống
        if username in lst_accounts.keys():
            break
        else:
            print("Username does not exist!")
            count_trial_user += 1
            if count_trial_user >= 3:
                print("You have exceeded the maximum number of attempts. Please try again later!")
                mainMenu()
                break

    # password -> trùng khớp với value của key
    if count_trial_user < 3:
        count_trial_pass = 0
        while True:
            password = input("- Password: ")
            # nếu password = value của key tương ứng
            if password == lst_accounts[username]:
                break
            else:
                print("Password is incorrect!")
                count_trial_pass += 1
                if count_trial_pass >= 3:
                    print("You have exceeded the maximum number of attempts. Please try again later!")
                    break

        print("Login Successfully. Welcome!!!")
        menuAccount(username)
        return username



def get_information_account(username):
    lst_full_acc = get_full_list_accounts()

    index = 0  # vị trí tài khoản trong lst_full_acc
    for i in range(len(lst_full_acc)):
        if lst_full_acc[i][0] == username:
            index = i
            break
    
    # lựa chọn thêm cho password
    l = len(lst_full_acc[index][1])
    pass_hidden = "*" * l
    print("===== THÔNG TIN TÀI KHOẢN ======")
    print(f"- Username: {lst_full_acc[index][0]}")
    print(f"- Password: {pass_hidden}")
    print(f"- ID: {lst_full_acc[index][2]}")
    print(f"- Full name: {lst_full_acc[index][3]}")
    print(f"- Balance: {lst_full_acc[index][4]}")



    

