def get_name():
    """asks user's name and validates it"""
    name_is_string = False
    while name_is_string == False:
        name = input("Enter name/company's name: ")
        print("\n")
        if name.isalpha():
            print("Hi "+name+"! Welcome to our shop."+"\n"+"Take a look at our laptops and decide which one you want."+"\n")
            name_is_string = True
            return name
        else:
            print("Error: Please input a valid name.\n")

def select_id(inventory,operation_num):
    """asks for laptop id and validates it"""
    id_success = False
    while id_success == False:
        try:
            laptop_id = int(input("Enter the desired laptop id: "))
            print("\n")      
            if operation_num == "1":
                if laptop_id <= 0 or laptop_id > len(inventory):
                    print("Error: ID does not exist\n")
                    # display_laptops()
                elif int(inventory[laptop_id-1][3]) == 0: 
                    print("The product is currently out of stock. We apologize for the inconvenience.\n"+
                      "Please feel free to explore some of our other products that may meet your needs. \n")
                else :
                    id_success = True
                    return laptop_id
            elif operation_num == "2":
                if laptop_id <= 0 or laptop_id > len(inventory):
                    print("Error: ID does not exist\n")
                else:
                    id_success = True
                    return laptop_id
        except:
            print("Error: Invalid input for ID\n")

def select_qty(current_qty,operation_num):
    """asks for laptop quantity and validates it"""
    qty_success = False
    while qty_success == False:
        try:
            laptop_qty = int(input("Enter the desired quantity of laptop: "))
            print("\n")
            if operation_num == "1":
                if laptop_qty <= 0:
                    print("Error: Quantity cannot be negative or zero\n")
                elif laptop_qty > current_qty:
                    print("Unfortunately, at the moment we only have",current_qty,"available.\n")
                else:
                    qty_success = True
                    return laptop_qty
            elif operation_num == "2":
                if laptop_qty <= 0:
                    print("Error: Invalid quantity\n")
                elif laptop_qty > 100:
                    print("Please note that we are currently limiting orders to 100 per resellers.\n")
                else:
                    qty_success = True
                    return laptop_qty
        except:
            print("Error: Invalid input for quantity\n")

def add_to_cart(inventory,id,qty,cart):
    """adds the product, qty, rate, net amount to the list cart"""
    product = inventory[id-1][0]
    brand = inventory[id-1][1]
    rate = inventory[id-1][2].replace("$","")
    net_amount = int(rate)*qty

    cart.append([product,brand,str(qty),rate,str(net_amount)])
    return cart