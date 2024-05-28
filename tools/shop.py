import main
import libs

def start():
    while True:
        print("Shop")
        back_to_main = input('Back to menu ? [y/n] : ')

        if back_to_main == 'y':
            main.menu()
        elif back_to_main == 'n':
            libs.exit_program()
exit()

if __name__ == '__main__':
    start()