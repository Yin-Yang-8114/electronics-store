from display import print_main_menu
from functions import user_choice
from product_mengment import product_management

def main():
    while True:
        print_main_menu()
        choice = user_choice("Enter your choice (1-5):")
        match choice:
            case 1:
                product_management()
            case 2:
                pass # TODO Inventory Management
            case 3:
                pass # TODO Sales Management
            case 4:
                pass # TODO Reports
            case 5:
                print(" Goodbye")
                break
            case _ :
                print("please choose btween 1-5")

if __name__ == "__main__":
    main()
