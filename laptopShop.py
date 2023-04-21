print("------------------------------------------------------------------------------------------------------------------------------------\n")
print("\t\t\t\t\t\t\t" + "    Techno Zone" + "\n")
print("\t\t\t\t\t\t\t" + "Apple | Dell | Acer" + "\n")
print("\t\t\t\t\t\t\t" + "      Kamaladi"+"\n")
print("-------------------------------------------------------------------------------------------------------------------------------------\n")
print("\t\t\t\t\t\t\t" + "Welcome to our shop !"+"\n")
print("\t\t\t\t\t\t" + "Buy the best laptops at the best price."+"\n")
print("--------------------------------------------------------------------------------------------------------------------------------------\n")

laptops_2d_lst = []
laptop_file = open("availableLaptops.txt","r")
for line in laptop_file:
    inner_lst = line.split(",") #split the line on runs of commas
    laptops_2d_lst.append(inner_lst)
laptop_file.close()

def display_laptops():
    """reads text file containing laptops and displays it"""
    laptop_file = open("availableLaptops.txt","r")
    print("LAPTOP ID\t"+"NAME\t\t\t"+"BRAND\t\t\t"+"PRICE\t\t"+"QUANTITY\t"+"PROCESSOR\t\t"+"GRAPHIC CARD"+"\n")
    laptop_id = 1
    for line in laptop_file:
        print(laptop_id,"\t\t" + line.replace(",","\t\t"))
        laptop_id += 1
    laptop_file.close()
display_laptops()

def display_operation_num():
    print("\n"+"enter 1. To sell Laptop")
    print("enter 2. To buy Laptop")
    print("enter 3. To exit"+"\n")
display_operation_num()

user_input = True
while user_input:
    input_number = (input("Enter the number of your choice for operation: "))
    if input_number == "1":
        #ask for personal info
        customer_name = input("Enter your name/company's name: ")
        customer_contact = input("Enter your contact no.: ")
        customer_address = input("Enter your address: ")
    
        def select_laptop():
            #ask for laptop id
            customer_laptop_id = int(input("Enter laptop id of the laptop you would like to purchase: "))
            while customer_laptop_id <= 0 or customer_laptop_id > len(laptops_2d_lst):
                print("\n"+"INVALID INPUT"+"\n")
                display_laptops()
                customer_laptop_id = int(input("Enter laptop id of the laptop you would like to purchase: "))

            #update laptop quantity in 2d list
            customer_qty = int(input("Enter the number of laptops you would you like to purchase: "))
            current_qty = int(laptops_2d_lst[customer_laptop_id-1][3])
            while customer_qty <= 0 or customer_qty > current_qty:
                print("\n"+"INVALID QUANTITY"+"\n")
                customer_qty = int(input("Enter the number of laptops you would you like to purchase: "))
            laptops_2d_lst[customer_laptop_id-1][3] = str(current_qty - customer_qty)

            #update laptop quantity in txt file
            laptop_file = open("availableLaptops.txt","w")
            for list in laptops_2d_lst:
                list_to_string = ','.join(list)
                laptop_file.write(list_to_string)
            laptop_file.close()
        select_laptop()

        #ask if more laptop needed
        buy_more = True
        while buy_more: 
            user_answer = input("Do you want to buy more?(y/n): ")
            if user_answer == "y":
                select_laptop()
            elif user_answer == "n":
                print("Thank you for your purchase.")
                buy_more = False     
        #break loop
        user_input = False
    elif input_number == "3":
        exit()