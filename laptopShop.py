print("------------------------------------------------------------------------------------------------------------------------------------------\n")
print("\t\t\t\t\t\t\t" + "    Techno Zone" + "\n")
print("\t\t\t\t\t\t\t" + "Apple | Dell | Acer" + "\n")
print("\t\t\t\t\t\t\t" + "      Kamaladi"+"\n")
print("-------------------------------------------------------------------------------------------------------------------------------------------\n")
print("\t\t\t\t\t\t\t" + "Welcome to our shop !"+"\n")
print("\t\t\t\t\t\t" + "Buy the best laptops at the best price."+"\n")
print("--------------------------------------------------------------------------------------------------------------------------------------------\n")

def display_laptops():
    """reads text file containing laptops and displays it"""
    file = open("availableLaptops.txt","r")
    print("LAPTOP ID\t"+"NAME\t\t\t"+"BRAND\t\t\t"+"PRICE\t\t"+"QUANTITY\t\t"+"PROCESSOR\t\t"+"GRAPHIC CARD"+"\n")
    laptop_id = 1
    for line in file:
        print(laptop_id,"\t\t" + line.replace(",","\t\t"))
        laptop_id += 1
    file.close()
display_laptops()

laptops_2d_lst = [["Razer Blade","Razer","$2000",20,"i7 7th Gen","GTX 3060"],
            ["XPS","Dell","$1976",15,"i5 9th Gen,GTX 3070"],
            ["Alienware","Alienware","$1978",24,"i5 9th Gen","GTX 3070"],
            ["Swift 7","Acer","$900" ,12,"i5 9th Gen","GTX 3070"],
            ["Macbook Pro 16","Apple","$3500",10,"i5 9th Gen","GTX 3070"]]

def display_operation_num():
    print("\n"+"enter 1. To sell Laptop")
    print("enter 2. To buy Laptop")
    print("enter 3. To exit"+"\n")
display_operation_num()

input_number = int(input("Enter the number of your choice for operation: "))

if input_number == 1:
    customer_name = input("Enter your name: ")
    customer_contact = int(input("Enter your phone number: "))
    customer_location = input("Enter your location: ")
    customer_laptop_id = int(input("Enter laptop id of the laptop you would like to purchase: "))
    while customer_laptop_id <= 0 or customer_laptop_id > len(laptops_2d_lst):
        print("\n"+"INVALID INPUT"+"\n")
        display_laptops()
        customer_laptop_id = int(input("Enter laptop id of the laptop you would like to purchase: "))
elif input_number == 3:
    exit()