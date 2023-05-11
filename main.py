from operations import get_name,select_id, select_qty, add_to_cart
from read import get_laptops, display_laptops, display_bill
from write import welcome_msg, display_operation_num, update_qty, bill

welcome_msg()
display_laptops()
inventory = get_laptops()
cart = []

while True:
    display_operation_num()
    operation_num = input("Enter the number of your choice for operation: ")
    print("\n")
    if operation_num == "1":
        name = get_name()
        display_laptops()
        id = select_id(inventory,operation_num)
        current_qty = int(inventory[id-1][3])
        qty = select_qty(current_qty,operation_num)
        inventory[id-1][3] = str(current_qty - qty)
        update_qty(inventory)
        cart = add_to_cart(inventory,id,qty,cart)

        #ask if more laptop needed
        buy_more = True
        while buy_more: 
            user_answer = input("Would you like another laptop?(y/n): ")
            print("\n")
            if user_answer == "y":
                display_laptops()
                id = select_id(inventory,operation_num)
                current_qty = int(inventory[id-1][3])
                qty = select_qty(current_qty,operation_num)
                inventory[id-1][3] = str(current_qty - qty)
                update_qty(inventory)
                cart = add_to_cart(inventory,id,qty,cart)
            elif user_answer == "n":
                ship = True
                while ship:
                    ship_choice = input("Do you want to ship?(y/n): ")
                    print("\n")
                    if ship_choice == "y":
                        filename = bill(name,cart,ship_choice,operation_num)
                        display_bill(filename)
                        display_laptops()
                        cart = []
                        ship = False
                    elif ship_choice == "n":
                        filename = bill(name,cart,ship_choice,operation_num)
                        display_bill(filename)
                        display_laptops()
                        cart = []
                        ship = False
                buy_more = False     

    elif operation_num == "2":
        name = get_name()
        display_laptops()
        id = select_id(inventory,operation_num)
        current_qty = int(inventory[id-1][3])
        qty = select_qty(current_qty,operation_num)
        inventory[id-1][3] = str(current_qty + qty)
        update_qty(inventory)
        cart = add_to_cart(inventory,id,qty,cart)

        #ask if more laptop needed
        buy_more = True
        while buy_more: 
            user_answer = input("Do you want to buy more?(y/n): ")
            print("\n")
            if user_answer == "y":
                display_laptops()
                id = select_id(inventory,operation_num)
                current_qty = int(inventory[id-1][3])
                qty = select_qty(current_qty,operation_num)
                inventory[id-1][3] = str(current_qty + qty)
                update_qty(inventory)
                cart = add_to_cart(inventory,id,qty,cart)
            elif user_answer == "n":
                ship_choice = "n"
                filename = bill(name,cart,ship_choice,operation_num)
                display_bill(filename)
                display_laptops()
                cart = []
                buy_more = False    

    elif operation_num == "3":
        print("Thank you for visiting our shop.\n")
        exit()