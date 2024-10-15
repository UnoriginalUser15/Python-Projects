import random

def get_value(card, score):
    try:
        return int(card) # if the card is just a number it will return that to be added to the player's current score
    except:
        if card != "A": # if the card is a J Q or K it will return 10
            return 10
        elif score + 11 <= 21: # returns 11 for an ace if it won't make player go bust
            return 11
        else:
            return 1 # returns 1 for an ace if 1 would make player go bust

print("""Automatic Jackblack Player
--------------------------""")

games = 0
blackjack = 0
deck = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]*4 # creates the cards that will be in the deck
random.shuffle(deck) # shuffles the deck

while True:
    hand = []
    score = 0

    while score < 17 and len(deck) != 0:
        card = deck.pop() # takes the card off the top of the deck
        hand.append(card) # adds the card to the player's hand
        score += get_value(card, score) #adds new card to player's score
    
    if score == 21:
        print("You've got blackjack")
        games += 1
        blackjack += 1
    elif score < 21:
        print(f"You've scored {score}")
        games += 1
    else:
        print(f"You've gone bust with a deck of {score} :(")
        games += 1

    print(f"Your cards were {hand}")

    if len(deck) < 1:
        break

print(f"You played {games} games")
input("Press enter to exit")