from function import *
import os 

choice = 0
os.system("clear")
mainMenu()
while True:
    choice = int(input("Enter your choice: "))
    if choice == 1:
        os.system("clear")
        signUp()
    elif choice == 2:
        os.system("clear")
        username = signIn()
        choice1 = int(input("Enter your choice: "))
        if choice1 == 1:
            os.system("clear")
            get_information_account(username)
        else:
            pass
        
    elif choice == 3:
        break
    else:
        print("Invalid choice")