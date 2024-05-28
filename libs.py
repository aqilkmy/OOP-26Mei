import socket
# import main
from time import sleep

PC_NAME = socket.gethostname()
welcome_msg = 'WELCOME'
style1 = '#' * (len(PC_NAME) + len(welcome_msg) + 7 )

def welcome_message():
    print(style1)
    print(f'## {welcome_msg} {PC_NAME} ##')
    print(style1)

def exit_program():
    print('Program will stoped in')
    sleep(1)
    print('3...')
    sleep(1)
    print('2...')
    sleep(1)
    print('1...')
    sleep(1)
    print('*** Program stoped ***')
# menu()
        
if __name__ == '__main__':
    welcome_message()
    exit_program()