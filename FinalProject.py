def chooseUnit():
    print("There are three types of unit convertions available: \n 1.Distance, 2.Volume, 3.Weight.")
    unit = input("Select the number corresponding to the unit you would like to convert: ")
    unit = int(unit)
    if unit == 1:
        distanceConv()
    elif unit == 2:
        volumeConv()
    elif unit == 3:
        weightConv()
    else:
        print("Selected number is not available, please try again.")

def distanceConv():
    print("Type 1 if you want to covert feet to meters or 2 for meters to feet.")
    select = input("Select whether you want to convert feet to meters or meters to feet: ")
    select = int(select)
    if select == 1:
        print("You have selected feet to meters.")
        quantity = input("Enter the amount to be converted: ")
        quantity = float(quantity)
        result = quantity / 3.28
        print("Your total is: ", result)
    elif select == 2:
        print("You have seleceted meters to feet.")
        quantity = input("Enter the amount to be converted: ")
        quantity = float(quantity)
        result = quantity * 3.28
        print("Your total is: ", result)
    else: 
        print("The number you have selected is not available, please try again")

def volumeConv():
    print("Type 1 if you want to covert gallons to liters or 2 for liters to gallons.")
    select = input("Select whether you want to convert gallons to litres or liters to gallons: ")
    select = int(select)
    if select == 1:
        print("You have selected gallons to liters.")
        quantity = input("Enter the amount to be converted: ")
        quantity = float(quantity)
        result = quantity * 3.78
        print("Your total is: ", result)
    elif select == 2:
        print("You have seleceted liters to gallons.")
        quantity = input("Enter the amount to be converted: ")
        quantity = float(quantity)
        result = quantity * 0.264172
        print("Your total is: ", result)
    else: 
        print("The number you have selected is not available, please try again")

def weightConv():
    print("Type 1 if you want to covert pounds to grams or 2 for grams to pounds.")
    select = input("Select whether you want to convert pounds to grams or grams to pounds: ")
    select = int(select)
    if select == 1:
        print("You have selected pounds to grams.")
        quantity = input("Enter the amount to be converted: ")
        quantity = float(quantity)
        result = quantity * 453.592
        print("Your total is: ", result)
    elif select == 2:
        print("You have seleceted grams to pounds.")
        quantity = input("Enter the amount to be converted: ")
        quantity = float(quantity)
        result = quantity * 0.0022
        print("Your total is: ", result)
    else: 
        print("The number you have selected is not available, please try again")

chooseUnit()