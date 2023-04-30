from datetime import datetime
from operations import welcome_msg,display_laptops,display_operation_num,personal_info,select_laptop,bill

welcome_msg()

display_laptops()

display_operation_num()

user_input = True
while user_input:
    input_number = input("Enter the number of your choice for operation: ")
    if input_number == "1":
        personal_info()
        cart = []
        cart = select_laptop(cart)

        #ask if more laptop needed
        buy_more = True
        while buy_more: 
            user_answer = input("Do you want to buy more?(y/n): ")
            print("\n")
            if user_answer == "y":
                display_laptops()
                select_laptop(cart)
            elif user_answer == "n":
                ship = True
                while ship:
                    ship_or_not = input("Do you want to ship?(y/n): ")
                    print("\n")
                    obj_datetime = datetime.now()
                    if ship_or_not == "y":
                        bill(cart,obj_datetime,ship_or_not)
                        ship = False
                    elif ship_or_not == "n":
                        bill(cart,obj_datetime,ship_or_not)
                        ship = False
                buy_more = False     
        user_input = False
    elif input_number == "3":
        exit()