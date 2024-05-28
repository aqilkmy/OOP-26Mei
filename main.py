from libs import welcome_message, exit_program
from games import game1
from tools import shop
import os

# print("Test")
def menu():
    user_option = int(input(f"Main menu : \n1.Games \n2.Shop\nYour choice :"))
    os.system("clear")
    if user_option == 1:
        print("**Games**")
        game1.start()
    elif user_option == 2:
        shop.start()
    while user_option !=1 and user_option !=2:
        os.system('clear')
        user_option = int(input(f"Main menu : \n1.Games \n2.Shop\nPlease choice available menu :"))

def main():
    welcome_message()
    menu()

if __name__ == '__main__':
    main()
    