def display_laptops():
    """reads text file containing laptops and displays it"""
    with open("read.txt","r") as laptop_file:
        print("="*132 + "\n")
        print("LAPTOP ID\t"+"NAME\t\t\t"+"BRAND\t\t\t"+"PRICE\t\t"+"QUANTITY\t"+"PROCESSOR\t\t"+"GRAPHIC CARD"+"\n")
        print("="*132 + "\n")
        laptop_id = 1
        for line in laptop_file:
            print(laptop_id,"\t\t" + line.replace(",","\t\t"))
            laptop_id += 1
        print("\n" + "="*132 + "\n")