print("------------------------------------------------------------------------------------------------------------------------------------\n")
print("\t\t\t\t\t\t\t" + "    Techno Zone" + "\n")
print("\t\t\t\t\t\t\t" + "Apple | Dell | Acer" + "\n")
print("\t\t\t\t\t\t\t" + "      Kamaladi"+"\n")
print("-------------------------------------------------------------------------------------------------------------------------------------\n")
print("\t\t\t\t\t\t\t" + "Welcome to our shop !"+"\n")
print("\t\t\t\t\t\t" + "Buy the best laptops at the best price."+"\n")
print("--------------------------------------------------------------------------------------------------------------------------------------\n")

laptops_2d_lst = []
with open("availableLaptops.txt","r") as laptop_file:
    for line in laptop_file:
        inner_lst = line.split(",") #split the line on runs of commas
        laptops_2d_lst.append(inner_lst)

def display_laptops():
    """reads text file containing laptops and displays it"""
    with open("availableLaptops.txt","r") as laptop_file:
        print("LAPTOP ID\t"+"NAME\t\t\t"+"BRAND\t\t\t"+"PRICE\t\t"+"QUANTITY\t"+"PROCESSOR\t\t"+"GRAPHIC CARD"+"\n")
        print("--------------------------------------------------------------------------------------------------------------------------------------\n")
        laptop_id = 1
        for line in laptop_file:
            print(laptop_id,"\t\t" + line.replace(",","\t\t"))
            laptop_id += 1
        print("\n"+"--------------------------------------------------------------------------------------------------------------------------------------\n")
display_laptops()

def display_operation_num():
    print("\n"+"enter 1. To sell Laptop")
    print("enter 2. To buy Laptop")
    print("enter 3. To exit"+"\n")
display_operation_num()

user_input = True
while user_input:
    input_number = input("Enter the number of your choice for operation: ")
    if input_number == "1":
        #ask for personal info
        print("\n")
        customer_name = input("Enter your name/company's name: ")
        print("\n")
        print("Hi "+customer_name+"! Welcome to Techno Zone."+"\n"+"Take a look at our laptops and decide which one you want."+"\n"+
              "Before proceeding further we will be asking for your personal details for the bill.")
        print("\n")
        customer_contact = input("Enter your contact no.: ")
        print("\n")
        customer_address = input("Enter your address: ")
        print("\n")
    
        cart = []
        def select_laptop():
            #ask for laptop id
            customer_laptop_id = int(input("Enter laptop id of the laptop you would like to purchase: "))
            print("\n")
            while customer_laptop_id <= 0 or customer_laptop_id > len(laptops_2d_lst):
                print("INVALID INPUT"+"\n")
                display_laptops()
                customer_laptop_id = int(input("Enter laptop id of the laptop you would like to purchase: "))
                print("\n")

            #update laptop quantity in 2d list
            customer_qty = int(input("Enter the number of laptops you would you like to purchase: "))
            print("\n")
            current_qty = int(laptops_2d_lst[customer_laptop_id-1][3])
            while customer_qty <= 0 or customer_qty > current_qty:
                print("INVALID QUANTITY"+"\n")
                customer_qty = int(input("Enter the number of laptops you would you like to purchase: "))
                print("\n")
            laptops_2d_lst[customer_laptop_id-1][3] = str(current_qty - customer_qty)

            #update laptop quantity in txt file
            with open("availableLaptops.txt","w") as laptop_file:
                for list in laptops_2d_lst:
                    list_to_string = ','.join(list)
                    laptop_file.write(list_to_string)
            
            #cart
            customer_product = laptops_2d_lst[customer_laptop_id-1][0]
            cost_price_dollar = laptops_2d_lst[customer_laptop_id-1][2]
            cost_price = laptops_2d_lst[customer_laptop_id-1][2].replace("$","")
            total_price = int(cost_price)*customer_qty

            cart.append([customer_product,customer_qty,cost_price_dollar,total_price])
            print(cart)
            return customer_laptop_id,customer_qty
        select_laptop()

        #ask if more laptop needed
        buy_more = True
        while buy_more: 
            user_answer = input("Do you want to buy more?(y/n): ")
            print("\n")
            if user_answer == "y":
                display_laptops()
                select_laptop()
            elif user_answer == "n":
                ship = True
                while ship:
                    ship_or_not = input("Do you want to ship?(y/n): ")
                    print("\n")
                    if ship_or_not == "y":
                        ship = False
                    elif ship_or_not == "n":
                        print("not shipped")
                        ship = False
                buy_more = False     
        #break main loop
        user_input = False
    elif input_number == "3":
        exit()