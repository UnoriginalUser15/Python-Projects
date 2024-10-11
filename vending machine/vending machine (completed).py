import time
import os
import random # used for random numebers
from colorama import Fore, Back, Style # colorama allows me to colour the outputed text with the format {Fore.COLOUR}
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
    "a1":["Potion", "of Healing", 1.45, "Common", "Heals 2d4 + 2"],
    "a2":["Potion", "of Greater Healing", 2.59, "Uncommon", "Heals 4d4 + 4"],
    "b1":["Bag", "of Beans", 4.99, "Rare", "If you dump the bag's contents they explode in a 10ft radius and deal 5d4 fire damage"],
    "b2":["Bag", "of Holding", 3.45, "Uncommon", "64 cubic feet of space within the bag"],
    "c1":["Cloak", "of Billowing", 1.25, "Common", "Use a bonus action to make it billow dramatically"],
    "c2":["Cloak", "of Arachnida", 7.65, "Very Rare", "Resistance to poison damage"]
}
# dictionary that contains the stock of each item and generates them randomly
stock_dict = {"a1": random.randint(5,20), "a2": random.randint(2,8), "b1": random.randint(1,4), "b2": random.randint(3,12), "c1": random.randint(1,6), "c2": 1}

credit = 0.00
# lists that are used to check if an input is valid
valid_coin = ["1p", "2p", "5p", "10p", "20p", "50p", "£1", "£2"]
payment_command = ["a", "b"]

# this controls the input of coins and tracking credit
def payment():
    # makes credit variable accessable outside of funciton
    global credit
    global payment_active

    payment_input = input("Please put in your input (coin/command): ").lower() #forces input to be lower case to avoid error
    
    if payment_input in valid_coin: # checks if input is valid a coin
        coin = coin_dict.get(payment_input)
        
        credit += coin
        credit = round(credit, 2)
        print("Processing...")
        time.sleep(0.5)
    elif payment_input in payment_command: # checks if the input is a command if it isn't a coin
        match payment_input:
            case "a":
                print(f"{Fore.YELLOW}---------------------------------------{Fore.RESET}")
                print("Proceeding to item selection...")
                time.sleep(2)
                payment_active = False
            case "b":
                print("Canceling payment, your coins will dispense shortly!")
                time.sleep(2)
                print(f"£ {credit} dispensed")
                time.sleep(2)
                credit = 0.00
    else: # if it's neither a coin or command it will tell the user to put a valid input in
        print("Invalid input, please put in a valid coin or command")
        time.sleep(2)

valid_code = ["a1", "a2", "b1", "b2", "c1", "c2"]
item_command = ["a", "b", "c", "d"]

def item_select():
    global credit
    global payment_active
    global item_active
    global exit_vending

    item_code = input("Please put in the code of your desired item: ").lower()
    command_input = input("Please put in a command listed above: ").lower()
    print(f"{Fore.YELLOW}---------------------------------------{Fore.RESET}")
    item = item_dict.get(item_code)
    item_stock = stock_dict.get(item_code)

    if item_code in valid_code and command_input in item_command:
        if command_input == "a":
            if (credit - item[2]) > 0.0 and item_stock > 0:
                credit -= item[2] # takes item cost off credit
                credit = round(credit, 2)
                print("Thank you for your purchase, your", item[0], item[1], "will now dispense...")
                stock_dict.update({item_code: stock_dict.get(item_code) - 1}) # this removes 1 from the stock of the item
                time.sleep(2)
                print(item [0], item[1], "dispensed :]")
                time.sleep(2)
            elif (credit - item[2]) <= 0.0:
                print("You do not have enough credit for this item, please select another item or return to payment.")
                time.sleep(2)
            else:
                print("This item is currently out of stock, please select another item or return to payment and cancel payment.")
                time.sleep(2)
        elif command_input == "b":
            print("Returning to payment...")
            payment_active = True
            item_active = False
            time.sleep(1.5)
        elif command_input == "c":
            if stock_dict.get(item_code) != 1: # this is to request the stock of an item and adds an 's' on the end of the noun of the item if the stock is not 1
                item_noun = item[0] + "s"
            else:
                item_noun = item[0]
            print(f"""Price: £{item[2]}
Stats: {item[4]}
Rarity: {item[3]}
Stock: {stock_dict.get(item_code)} {item_noun} {item[1]} currently in stock""")
            
            print(f"{Fore.YELLOW}---------------------------------------{Fore.RESET}")
            input("Press anything to return to item selection")
        elif command_input == "d":
            item_active = False
            exit_vending = True
            print("Exiting...")
            time.sleep(2)
    else:
        print("You have not input a valid code or command, please put in a valid input")
        time.sleep(2)

while True:
    payment_active = True
    exit_vending = False
    while payment_active == True:
        print(f"""   {Fore.RED}~|Dungeons and Vending Machines|~
{Fore.YELLOW}---------------------------------------
{Fore.MAGENTA}A1: {Fore.WHITE}Potion of Healing {Fore.GREEN}(£1.45, {stock_dict.get("a1")} in stock)
{Fore.MAGENTA}A2: {Fore.WHITE}Potion of Greater Healing {Fore.GREEN}(£2.59, {stock_dict.get("a2")} in stock)
{Fore.MAGENTA}B1: {Fore.WHITE}Bag of Beans {Fore.GREEN}(£4.99, {stock_dict.get("b1")} in stock)
{Fore.MAGENTA}B2: {Fore.WHITE}Bag of Holding {Fore.GREEN}(£3.45, {stock_dict.get("b2")} in stock)
{Fore.MAGENTA}C1: {Fore.WHITE}Cloak of Billowing {Fore.GREEN}(£1.25, {stock_dict.get("c1")} in stock)
{Fore.MAGENTA}C2: {Fore.WHITE}Cloak of Arachnida {Fore.GREEN}(£7.65, {stock_dict.get("c2")} in stock)
{Fore.YELLOW}---------------------------------------
{Fore.CYAN}Commands:
-Proceed to item select {Fore.YELLOW}(A){Fore.CYAN}
-Cancel payment and dispense credit {Fore.YELLOW}(B)
{Fore.GREEN}Coins: 1p, 2p, 5p, 10p, 20p, 50p, £1, £2
{Fore.YELLOW}---------------------------------------
Your current credit is: {Fore.GREEN}£{credit}
{Fore.YELLOW}---------------------------------------{Fore.RESET}""")
        payment()
        os.system("cls") # clears the terminal

    item_active = True
    while item_active == True:
        print(f"""   {Fore.RED}~|Dungeons and Vending Machines|~
{Fore.YELLOW}---------------------------------------
{Fore.MAGENTA}A1: {Fore.WHITE}Potion of Healing {Fore.GREEN}(£1.45, {stock_dict.get("a1")} in stock)
{Fore.MAGENTA}A2: {Fore.WHITE}Potion of Greater Healing {Fore.GREEN}(£2.59, {stock_dict.get("a2")} in stock)
{Fore.MAGENTA}B1: {Fore.WHITE}Bag of Beans {Fore.GREEN}(£4.99, {stock_dict.get("b1")} in stock)
{Fore.MAGENTA}B2: {Fore.WHITE}Bag of Holding {Fore.GREEN}(£3.45, {stock_dict.get("b2")} in stock)
{Fore.MAGENTA}C1: {Fore.WHITE}Cloak of Billowing {Fore.GREEN}(£1.25, {stock_dict.get("c1")} in stock)
{Fore.MAGENTA}C2: {Fore.WHITE}Cloak of Arachnida {Fore.GREEN}(£7.65, {stock_dict.get("c2")} in stock)
{Fore.YELLOW}---------------------------------------
{Fore.CYAN}Commands:
- Confirm purchase {Fore.YELLOW}(A){Fore.CYAN}
- Return to payment {Fore.YELLOW}(B){Fore.CYAN}
- Check qualities of the selected item {Fore.YELLOW}(C){Fore.CYAN}
- Exit the Vending Machine, this will return your remaining credit {Fore.YELLOW}(D){Fore.RED}
Make sure to ALWAYS put a valid code in even if you have no intention to purchase
{Fore.YELLOW}---------------------------------------
Your current credit is: {Fore.GREEN}£{credit}
{Fore.YELLOW}---------------------------------------{Fore.RESET}""")
        item_select()
        os.system("cls") # clears the terminal
    if exit_vending == True:
        print(f"""Dispensing change: £{credit}
Thank you for using Dungeons and Vending Machines :>""")
        credit = 0.0
        time.sleep(3)
        os.system("cls") # clears the terminal