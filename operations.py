def welcome_msg():
    print("------------------------------------------------------------------------------------------------------------------------------------\n")
    print("\t\t\t\t\t\t\t" + "    Techno Zone" + "\n")
    print("\t\t\t\t\t\t\t" + "Apple | Dell | Acer" + "\n")
    print("\t\t\t\t\t\t\t" + "      Kamaladi"+"\n")
    print("-------------------------------------------------------------------------------------------------------------------------------------\n")
    print("\t\t\t\t\t\t\t" + "Welcome to our shop !"+"\n")
    print("\t\t\t\t\t\t" + "Buy the best laptops at the best price."+"\n")
    print("--------------------------------------------------------------------------------------------------------------------------------------\n")

def get_laptops():
    laptops_2d_lst = []
    with open("availableLaptops.txt","r") as laptop_file:
        for line in laptop_file:
            inner_lst = line.split(",") #split the line on runs of commas
            laptops_2d_lst.append(inner_lst)
    return laptops_2d_lst

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

def display_operation_num():
    print("\n"+"enter 1. To sell Laptop")
    print("enter 2. To buy Laptop")
    print("enter 3. To exit"+"\n")

def personal_info():
    """ask user their name, contact, address"""
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

def select_laptop(cart):
    inventory = get_laptops()
    #ask for laptop id
    customer_laptop_id = int(input("Enter laptop id of the laptop you would like to purchase: "))
    print("\n")
    while customer_laptop_id <= 0 or customer_laptop_id > len(inventory):
        print("INVALID INPUT"+"\n")
        display_laptops()
        customer_laptop_id = int(input("Enter laptop id of the laptop you would like to purchase: "))
        print("\n")

    #update laptop quantity in 2d list
    customer_qty = int(input("Enter the number of laptops you would you like to purchase: "))
    print("\n")
    current_qty = int(inventory[customer_laptop_id-1][3])
    while customer_qty <= 0 or customer_qty > current_qty:
        print("INVALID QUANTITY"+"\n")
        customer_qty = int(input("Enter the number of laptops you would you like to purchase: "))
        print("\n")
    inventory[customer_laptop_id-1][3] = str(current_qty - customer_qty)

    #update laptop quantity in txt file
    with open("availableLaptops.txt","w") as laptop_file:
        for list in inventory:
            laptop_file.write(','.join(list))
            
    #cart
    customer_product = inventory[customer_laptop_id-1][0]
    brand = inventory[customer_laptop_id-1][1]
    rate = inventory[customer_laptop_id-1][2]
    cost_price = inventory[customer_laptop_id-1][2].replace("$","")
    net_amount = int(cost_price)*customer_qty

    cart.append([customer_product,brand,str(customer_qty),rate,str(net_amount)])
    print(cart)
    return cart

def bill(cart,obj_datetime,ship_or_not):
    date = obj_datetime.date()
    time = obj_datetime.time()
    print("\t\t\t\t" + " Sales Invoice" + "\n")
    print("\t\t\t\t" + "  TECHNO ZONE" + "\n")
    print("\t\t\t\t" + "    Kamaladi"+"\n")
    print("\t\t\t" + "9841123456,Email:technozone@gmail.com"+"\n")
    print("---------------------------------------------------------------------------------------\n")
    print("Party Details:","\t\t\t\t\t\t","Bill Date:",date,"\n"+"Mega Bank","\t\t\t\t\t\t","Bill Time:",time,"\n")
    print("---------------------------------------------------------------------------------------\n")
    print("Particulars\t\t"+"Brand\t\t\t"+"Qty\t\t"+"Net Rate\t"+"NetAmt\t")
    print("---------------------------------------------------------------------------------------\n")
    for each in cart:
        print("\t\t".join(each))
        print("\n")
    print("---------------------------------------------------------------------------------------\n")
    total = 0
    for each in cart:
        total = total + int(each[4])
    print("Total:\t\t\t\t\t\t\t\t\t\t"+str(total)+"\n")
    if ship_or_not == "y":
        shipping_charge = 100
        print("Freight & Forwarding Charges:\t\t\t\t\t\t\t"+str(shipping_charge)+"\n")
        print("---------------------------------------------------------------------------------------\n")
        grand_total = total + shipping_charge
        print("Grand Total:\t\t\t\t\t\t\t\t\t"+str(grand_total))
    print("---------------------------------------------------------------------------------------\n")
    print("Terms & Conditions\n")
    print("1.Goods once sold will not be returned.")
    print("2.We offer complimentary repair services for our products upto 1 year with receipt.\n")
    print("\t\t\t\tT H A N K  Y O U")
    print("---------------------------------------------------------------------------------------\n")