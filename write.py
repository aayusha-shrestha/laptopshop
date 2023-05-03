from datetime import datetime

def welcome_msg():
    """prints shop name, address and welcome msg"""
    print("="*132 + "\n")
    print("\t\t\t\t\t\t\t" + "    Techno Zone" + "\n")
    print("\t\t\t\t\t\t\t" + "Apple | Dell | Acer" + "\n")
    print("\t\t\t\t\t\t\t" + "      Kamaladi"+"\n")
    print("="*132 + "\n")
    print("\t\t\t\t\t\t\t" + "Welcome to our shop !"+"\n")
    print("\t\t\t\t\t\t" + "Buy the best laptops at the best price."+"\n")

def display_operation_num():
    """prints numbers to be entered to buy,sell or exit from program"""
    print("\n"+"enter 1. To sell Laptop to customers")
    print("enter 2. To buy Laptop from manufacturer")
    print("enter 3. To exit"+"\n")

def bill(name,cart,ship_choice,operation_num):
    """prints bill in txt file, reads the txt file to print in terminal"""
    obj_datetime = datetime.now()
    date = obj_datetime.date()
    time = obj_datetime.strftime("%H-%M-%S")

    #generate invoice in txt file
    filename = "invoice" + time + ".txt"
    try:
        with open(filename,"w") as invoice:
            invoice.write("\t\t\t\t" + "   Sales Invoice" + "\n")
            invoice.write("\t\t\t\t" + "    TECHNO ZONE" + "\n")
            invoice.write("\t\t\t\t" + "      Kamaladi"+"\n")
            invoice.write("\t\t\t" + "9841123456,Email:technozone@gmail.com"+"\n")
            invoice.write("---------------------------------------------------------------------------------------\n")
            invoice.write("Party Details:" + "\t\t\t\t\t\t\t" + "Bill Date:" + str(date) + "\n" + "Mega Bank" + "\t\t\t\t\t\t\t" + "Bill Time:" + time + "\n")
            invoice.write("---------------------------------------------------------------------------------------\n")
            invoice.write("Customer: " + name + "\n")
            invoice.write("---------------------------------------------------------------------------------------\n")
            invoice.write("Particulars\t\t" + "Brand\t\t\t" + "Qty\t\t" + "Net Rate\t" + "NetAmt\t\n")
            invoice.write("---------------------------------------------------------------------------------------\n")
            for each in cart:
                invoice.write("\t\t".join(each))
                invoice.write("\n")
            invoice.write("---------------------------------------------------------------------------------------\n")
            total = 0
            for each in cart:
                total = total + int(each[4])
            invoice.write("Total:\t\t\t\t\t\t\t\t\t\t"+str(total)+"\n")
            if ship_choice == "y":
                shipping_charge = 10
                invoice.write("Freight & Forwarding Charges:\t\t\t\t\t\t\t"+str(shipping_charge)+"\n")
                invoice.write("---------------------------------------------------------------------------------------\n")
                grand_total = total + shipping_charge
                invoice.write("Grand Total:\t\t\t\t\t\t\t\t\t"+str(grand_total)+"\n")
            if operation_num == "2":
                vat = (13/100)*total
                invoice.write("VAT[13%]:\t\t\t\t\t\t\t\t\t"+str(vat)+"\n")
                invoice.write("---------------------------------------------------------------------------------------\n")
                gross_amount = total + vat
                invoice.write("Gross Amount:\t\t\t\t\t\t\t\t\t"+str(gross_amount)+"\n")
            invoice.write("---------------------------------------------------------------------------------------\n")
            invoice.write("Terms & Conditions\n")
            invoice.write("1.Goods once sold will not be returned.\n")
            invoice.write("2.We offer complimentary repair services for our products upto 1 year with receipt.\n")
            invoice.write("\t\t\t\tT H A N K  Y O U\n")
            invoice.write("---------------------------------------------------------------------------------------\n")
    except FileNotFoundError:
        print("File not found")
    except Exception:
        print("An error occured")
    
    #generate invoice in console
    try:
        with open(filename,"r") as invoice:
            for line in invoice:
                print(line)
    except FileNotFoundError:
        print("File not found")
    except Exception:
        print("An error occured")