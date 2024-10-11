valid_input = False

def year_check():
    valid_input = False

    while valid_input == False:
        try:
            year = int(input("Please input the year here: "))

            valid_input = True
        except:
            print("Invalid input, please put in a number")
    #do not touch the line, you have been warned
    print("-------------------------------------")

    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        print(year ,"is a leap year")
    else:
        print(year ,"is not a leap year")

run_program = True
while run_program == True:
    year_check()
    print("-------------------------------------")
    run_check = input("Type 'exit' if you want to close the program. Type anything else if you ant to continue: ")[:1].lower()
    print("-------------------------------------")

    if run_check == "e":
        run_program = False