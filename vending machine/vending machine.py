import time
import os
# dictionary that contains all the valid coins float values
coin_dict = {
    "1p": 0.01,
    "2p": 0.02,
    "5p": 0.05,
    "10p": 0.10,
    "20p": 0.20,
    "50p": 0.50,
    "£1": 1.00,
    "£2": 2.00,
}
# dictionary that contains all the items codes names and price
item_dict = {
    "a1":["Potion", "of Healing", 1.45, "Common", "2d4 + 2"],
    "a2":["Potion", "of Greater Healing", 2.59],
    "b1":["Bag", "of Beans", 4.99, "Rare"],
    "b2":["Bag", "of Holding", 1.50],
    "c1":["item5", 1.50],
    "c2":["item6", 1.50],
}
stock_dict = {"a1": 6, "a2": 3, "b1": 2, } 

credit = 0.00
# lists that are used to check if an input is valid
valid_coin = ["1p", "2p", "5p", "10p", "20p", "50p", "£1", "£2"]
valid_command = ["a", "b"]
#this controls the input of coins and tracking credit
def payment():
    # makes credit variable accessable outside of funciton
    global credit
    global payment_active

    payment_input = input("Please put in your input (coin or command): ").lower() #forces input to be lower case to avoid error
    
    if payment_input in valid_coin: # checks if input is valid a coin
        coin = coin_dict.get(payment_input)
        
        credit += coin
        credit = round(credit, 2)
        print("Processing...")
        time.sleep(0.5)
    elif payment_input in valid_command: # checks if the input is a command if it isn't a coin
        
        if payment_input == "a":
            print("Proceeding to item selection...")
            time.sleep(2)
            payment_active = False
        elif payment_input == "b":
            print("Canceling payment, your coins will dispense shortly!")
            time.sleep(2)
            print("£", credit, "dispensed")
            time.sleep(2)
            credit = 0.00
    else: # if it's neither a coin or command it will tell the user to put a valid input in
        print("Invalid input, please put in a valid coin or command")
        time.sleep(2)

valid_code = ["a1", "a2", "b1", "b2", "c1"]

def item_select():
    global credit
    global payment_active

    item_code = input("Please put in the code of your desired item: ").lower()
    
    if item_code in valid_code:
        item = item_dict.get(item_code)
        if (credit - item[2]) > 0.0:
            credit -= item[2]
        else:
            print("You do not have enough credit for this item, please select another item or return to payment.")
    elif: item_code in valid_command:

    if stock_dict.get(item_code) != 1: #this is to request the stock of an item and adds an 's' on the end of the noun of the item if the stock is not 1
        item_noun = item[0] + "s"
    else:
        item_noun = item[0]
    print(stock_dict.get(item_code), item_noun, item[1], "currently in stock")

while True:
    payment_active = True
    while payment_active == True:
        print("""Commands:
-Proceed to item select (A)
-Cancel payment and dispense credit (B)
---------------------------------------
""")
        print("Your current credit is: £",credit)
        payment()
        os.system("cls") # clears the terminal

    item_active = True
    while item_active == True:
        print("""Commands:
-Return to payment (A)
-Check qualities of the selected item (B)
---------------------------------------
""")
        item_select()