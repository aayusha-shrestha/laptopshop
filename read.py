def get_laptops():
    """reads txt file containing laptops and stores it in 2d list"""
    laptops_2d_lst = []
    try:
        with open("read.txt","r") as laptop_file:
            for line in laptop_file:
                inner_lst = line.split(",") #split the line on runs of commas
                laptops_2d_lst.append(inner_lst)
        return laptops_2d_lst
    except FileNotFoundError:
        print("File not found")
    except Exception:
        print("An error occured")

def display_laptops():
    """reads text file containing laptops and prints it"""
    try:
        with open("read.txt","r") as laptop_file:
            print("="*132 + "\n")
            print("LAPTOP ID\t"+"NAME\t\t\t"+"BRAND\t\t\t"+"PRICE\t\t"+"QUANTITY\t"+"PROCESSOR\t\t"+"GRAPHIC CARD"+"\n")
            print("="*132 + "\n")
            laptop_id = 1
            for line in laptop_file:
                print(laptop_id,"\t\t" + line.replace(",","\t\t"))
                laptop_id += 1
            print("\n" + "="*132 + "\n")
    except FileNotFoundError:
        print("File not found")
    except Exception:
        print("An error occured")