#Point of Sale

print("|==========================================================================================================================|")
print("|Hello!Welcome to our store.                                                                                               |")
print("|> Please READ the guidelines and CORRECTLY FILL the question asking that you want to buy and the QUANTITY of it,Thank you.|")
print("|==========================================================================================================================|")
print("List of the product and their respective price(s):")
print("========================")
print("|Product Name: |Price  |")
print("------------------------")
print("|> Coffe       |₱10.50 |")
print("|> Sandwich    |₱20.50 |")
print("|> Palaman     |₱7.50  |")
print("|> Water       |₱5.00  |")
print("========================")
print()
print("Type Y for Yes,I want that product and N for No,I don't want that product and other alphabet and numbers considerd as a No")

first_product = "Coffe"
user_coffe_product = input("You want Coffe?[Y/N] : ")
user_coffe_product = user_coffe_product.upper()
if user_coffe_product == "Y":
    user_coffe_product = 10.50
    user_coffe_qty = float(input("QTY [Put positive integer number only]:"))
    coffe_qty_total = user_coffe_product * user_coffe_qty
    print("₱",coffe_qty_total)
else:
    coffe_qty_total = 0    

second_product = "Sandwich"
user_sandwich_product = input("You wan Sandwich?[Y/N] : ")
user_sandwich_product = user_sandwich_product.upper()
if user_sandwich_product == "Y":
    user_sandwich_product = 20.50
    user_sandwich_qty = float(input("QTY [Put positive integer number only]: "))
    sandwich_qty_total = user_sandwich_product * user_sandwich_qty
    print("₱",sandwich_qty_total)
else:
    sandwich_qty_total =0

third_product = "Palaman"
user_palaman_product = input("You want Palaman?[Y/N] : ")
user_palaman_product = user_palaman_product.upper()
if user_palaman_product == "Y":
    user_palaman_product = 7.50
    user_palaman_qty = float(input("QTY [Put positive integer number only]: "))
    palaman_qty_total = user_palaman_product * user_palaman_qty
    print("₱",palaman_qty_total)
else:
    palaman_qty_total = 0 

fourth_product = "Water"
user_water_product = input("You want water?[Y/N] : ")
user_water_product = user_water_product.upper()
if user_water_product == "Y":
    user_water_product = 5.00
    user_water_qty = float(input("QTY [Put positive integer number only] : "))
    water_qty_total = user_water_product * user_water_qty
    print("₱",water_qty_total)
else:
    water_qty_total = 0    

total_all = coffe_qty_total + sandwich_qty_total + palaman_qty_total + water_qty_total
if total_all == 0:
     print("You didn't order anything") 
else:
    print("Your payment for your order is ₱",total_all )
    payment = float(input("Kindly put your money : "))
    payment = payment - total_all
    if payment < 0:
        print("Lack of funds or you type not positive integers your order automatically cancelled")
    else:
         print("Thank your for ordering our product and your change is ₱",payment)

print()
print("All information of that you order from our store")
print(">",first_product,"the total worth of ₱",coffe_qty_total)
print(">",second_product,"the total worth of ₱",sandwich_qty_total)
print(">",third_product,"the total worth of ₱",palaman_qty_total)
print(">",fourth_product,"the total worth of ₱",water_qty_total)
print("-------------------------------------------------")
print("> total amout of",total_all)
if total_all == 0:
    print("You didn't order anything")
else:    
    print("> Your Change is ₱",payment) 