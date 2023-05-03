from operations import select_laptop
from read import display_laptops
from write import welcome_msg,display_operation_num,bill

welcome_msg()
display_laptops()
display_operation_num()
cart = []
while True:
    operation_num = input("Enter the number of your choice for operation: ")
    print("\n")
    if operation_num == "1":
        name = input("Enter name/company's name: ")
        print("\n")
        cart = select_laptop(operation_num,cart)
        #ask if more laptop needed
        buy_more = True
        while buy_more: 
            user_answer = input("Do you want to buy more?(y/n): ")
            print("\n")
            if user_answer == "y":
                display_laptops()
                select_laptop(operation_num,cart)
            elif user_answer == "n":
                ship = True
                while ship:
                    ship_choice = input("Do you want to ship?(y/n): ")
                    print("\n")
                    if ship_choice == "y":
                        bill(name,cart,ship_choice,operation_num)
                        display_laptops()
                        display_operation_num()
                        cart = []
                        ship = False
                    elif ship_choice == "n":
                        bill(name,cart,ship_choice,operation_num)
                        display_laptops()
                        display_operation_num()
                        cart = []
                        ship = False
                buy_more = False     
    elif operation_num == "2":
        name = input("Enter name/company's name: ")
        print("\n")
        cart = select_laptop(operation_num,cart)
        #ask if more laptop needed
        buy_more = True
        while buy_more: 
            user_answer = input("Do you want to buy more?(y/n): ")
            print("\n")
            if user_answer == "y":
                display_laptops()
                select_laptop(operation_num,cart)
            elif user_answer == "n":
                ship_choice = "n"
                bill(name,cart,ship_choice,operation_num)
                display_laptops()
                display_operation_num()
                cart = []
                buy_more = False     
    elif operation_num == "3":
        exit()
