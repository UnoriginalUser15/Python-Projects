import os
import time
from colorama import Fore, Back, Style # colorama allows me to colour the outputed text with the format {Fore.COLOUR}

while True:
    try:
        column_num = int(input("Columns: "))
        row_num = int(input("Rows: "))
        break
    except:
        print("You can't create a grid without whole numbers")
        time.sleep(2)
        os.system("cls")

while True:
    if column_num <= 0 or row_num <= 0:
        print ("You have to have at least 1 column and 1 row")
        time.sleep(2)
        os.system("cls")
    else:
        break

column_list = [f"{Fore.RESET}O"]*column_num # creates a list with how many columns a row has
grid = []
for i in range(row_num):
    grid.append(column_list[:]) # the : (slice) creates a copy of the c_list and adds it to the grid list

# this draws the grid
def draw():
    for i in range(row_num):
        if i == 0:
            print(*list(range(1, column_num + 1)))
        print(*grid[i]) # the * unpacks the list and prints it without the [] and ,

def add_piece():
    if player == 1:
        piece = f"{Fore.BLUE}B"
    else:
        piece = f"{Fore.RED}R"
# this makes the piece fall to the lowest point in the column
    for i in reversed(range(row_num)):
        if grid[i][c_choice] == f"{Fore.RESET}O":
            grid[i][c_choice] = piece
            break
        if grid[0][c_choice] != f"{Fore.RESET}O":
            print("You tried to put a piece in a full column, forfieting your turn")
            time.sleep(2)
            break
    return grid

def horizontal_check(): # checks if there is a winning horizontal line
    for i in range(row_num):
        if f"{Fore.BLUE}B{Fore.BLUE}B{Fore.BLUE}B{Fore.BLUE}B" in "".join(grid[i]) or f"{Fore.RED}R{Fore.RED}R{Fore.RED}R{Fore.RED}R" in "".join(grid[i]):
            return True, "h" # the boolian is to break the main program's while loop, the string is for the win message
    return False, ""

def vertical_check(): # checks if there is a winning vertical line
    for c in range(column_num): # c represents column
        temp_column = ""
        for r in range(row_num): # r represents column
            temp_column += grid[r][c]
            if f"{Fore.BLUE}B{Fore.BLUE}B{Fore.BLUE}B{Fore.BLUE}B" in temp_column or f"{Fore.RED}R{Fore.RED}R{Fore.RED}R{Fore.RED}R" in temp_column:
                return True, "v" # the boolian is to break the main program's while loop, the string is for the win message
    return False, ""

def downright_check():
    line_value = 0
    used_lines = []

    for r in range(row_num):
        temp_downright = ""
        for c in range(column_num):
            if c - r not in used_lines:
                line_value = c - r
                used_lines.append(line_value)
                for a in range(row_num):
                    for b in range(column_num):
                        if b - a == line_value:
                            temp_downright += grid[a][b]
                if f"{Fore.BLUE}B{Fore.BLUE}B{Fore.BLUE}B{Fore.BLUE}B" in temp_downright or f"{Fore.RED}R{Fore.RED}R{Fore.RED}R{Fore.RED}R" in temp_downright:
                    return True, ""
    return False, ""

def downleft_check():
    line_value = 0
    used_lines = []

    for r in range(row_num):
        temp_downleft = ""
        for c in range(column_num):
            if c + r not in used_lines: # this creates the value of line that is checked
                line_value = c + r
                used_lines.append(line_value)
                for a in range(row_num): # this creates a string of everything in that line
                    for b in range(column_num):
                        if b + a == line_value:
                            temp_downleft += grid[a][b]
                if f"{Fore.BLUE}B{Fore.BLUE}B{Fore.BLUE}B{Fore.BLUE}B" in temp_downleft or f"{Fore.RED}R{Fore.RED}R{Fore.RED}R{Fore.RED}R" in temp_downleft:
                    return True, ""
    return False, ""

# main program
draw()

player = 1

while True:
    print(f"{Fore.RESET}It is player {player}'s go.")
    c_choice = int(input("Enter the column number: ")) - 1
    
    add_piece() # calls the add_piece function
    
    horizontal_check() # checks if there's a winning horizontal or not
    won = horizontal_check()[0]
    win_type = horizontal_check()[1]
    if won == True:
        break
    
    vertical_check() # checks if there's a winning vertical or not
    won = vertical_check()[0]
    win_type = vertical_check()[1]
    if won == True:
        break

    downright_check()
    won = downright_check()[0]
    win_type = downright_check()[1]
    if won == True:
        break
    
    downleft_check()
    won = downleft_check()[0]
    win_type = downleft_check()[1]
    if won == True:
        break

    os.system("cls")
    draw()
    
    if won == False:
        if player == 1:
            player = 2
        else:
            player = 1

os.system("cls")
draw()
{Fore.RESET}

if win_type == "h":
    print(f"{Fore.RESET}Player {player} has won with a horizontal line!")
elif win_type == "v":
    print(f"{Fore.RESET}Player {player} has won with a vertical line!")
else:
    print(f"{Fore.RESET}Player {player} has won with a diagonal line!")
input("Press enter to quit")