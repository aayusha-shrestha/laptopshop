def get_laptops():
    laptops_2d_lst = []
    with open("read.txt","r") as laptop_file:
        for line in laptop_file:
            inner_lst = line.split(",") #split the line on runs of commas
            laptops_2d_lst.append(inner_lst)
    return laptops_2d_lst

def select_laptop(operation_num,cart):
    inventory = get_laptops()
    #ask for laptop id
    id_success = False
    while id_success == False:
        try:
            customer_laptop_id = int(input("Enter laptop id of the laptop you would like to purchase: "))
            print("\n")
            current_qty = int(inventory[customer_laptop_id-1][3])
            if customer_laptop_id <= 0 or customer_laptop_id > len(inventory):
                    print("ID DOES NOT EXIST\n")
                    # display_laptops()
            elif operation_num == "1":
                if current_qty == 0:
                    print("The product is currently out of stock. We apologize for the inconvenience.\n"+
                      "Please feel free to explore some of our other products that may meet your needs. \n")
                else :
                    id_success = True
            else:
                id_success = True
        except:
            print("INVALID input for ID\n")

    #ask for laptop quantity
    qty_success = False
    while qty_success == False:
        try:
            customer_qty = int(input("Enter the number of laptops you would you like to purchase: "))
            print("\n")
            if customer_qty <= 0:
                print("INVALID QUANTITY\n")
            elif operation_num == "1":
                if customer_qty > current_qty:
                    print("Unfortunately, at the moment we only have",current_qty,"available.\n")
                else:
                    qty_success = True
            elif operation_num == "2":
                if customer_qty > 100:
                    print("Please note that we are currently limiting orders to 100 per resellers.\n")
                else:
                    qty_success = True
        except:
            print("INVALID input for quantity\n")
    
    #update laptop quantity in 2d list
    if operation_num == "1":
        inventory[customer_laptop_id-1][3] = str(current_qty - customer_qty)
    else:
        inventory[customer_laptop_id-1][3] = str(current_qty + customer_qty)

    #update laptop quantity in txt file
    with open("read.txt","w") as laptop_file:
        for list in inventory:
            laptop_file.write(','.join(list))
            
    #cart
    customer_product = inventory[customer_laptop_id-1][0]
    brand = inventory[customer_laptop_id-1][1]
    rate = inventory[customer_laptop_id-1][2].replace("$","")
    net_amount = int(rate)*customer_qty

    cart.append([customer_product,brand,str(customer_qty),rate,str(net_amount)])
    return cart