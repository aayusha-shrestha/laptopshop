from datetime import datetime
from operations import welcome_msg,display_laptops,display_operation_num,personal_info,select_laptop

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
                    if ship_or_not == "y":
                        obj_datetime = datetime.now()
                        date = obj_datetime.date()
                        print("\t\t\t\t" + " Sales Invoice" + "\n")
                        print("\t\t\t\t" + "  TECHNO ZONE" + "\n")
                        print("\t\t\t\t" + "    Kamaladi"+"\n")
                        print("\t\t\t" + "9841123456,Email:technozone@gmail.com"+"\n")
                        print("-----------------------------------------------------------------------------------\n")
                        print("Party Details:"+"\t\t\t\t\t\t"+"     Bill Date:",date,"\n"+"Mega Bank"+"\n")
                        print("-----------------------------------------------------------------------------------\n")
                        print(cart)
                        ship = False
                    elif ship_or_not == "n":
                        print("not shipped")
                        ship = False
                buy_more = False     
        #break main loop
        user_input = False
    elif input_number == "3":
        exit()