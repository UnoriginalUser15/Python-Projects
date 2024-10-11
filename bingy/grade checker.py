def grade_check():
    #this prevents the program from crashing when a non-interger is inputed
    valid_input = False
    
    while valid_input ==False :
        try:
            while True:
                #checks if input is 0-100
                user_grade = int(input("Please put in your grade here [0-100]: "))

                if user_grade > 100:
                    print("Invalid grade, please put in a grade from 1-100")
                elif user_grade < 0:
                    print("Invalid grade, please put in a grade from 1-100")
                else:
                    break
            
            valid_input = True
        #if grade input does not meet checks it makes the user input again
        except:
            print("Invalid grade, please put in a grade from 1-100")


    if user_grade < 20:
        print("You got a F")
    elif user_grade > 19 and user_grade < 40:
        print("You got an E")
    elif user_grade > 39 and user_grade < 60:
        print("You got a D")
    elif user_grade > 59 and user_grade < 80:
        print("You got a C")
    elif user_grade > 79 and user_grade < 90:
        print("You got a B")
    else:
        print("Congratulations! You got an A!")

run_program = True
while run_program == True:
    grade_check()
    
    run_check = input("Type 'exit' if you want to close the program. Type anything else if you ant to continue: ")[:1].lower()
    
    if run_check == "e":
        run_program = False