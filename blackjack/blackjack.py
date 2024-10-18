import random
import os
import time

# currently the value of the "score" and "dealer_score" variables aren't calculated

def get_value(card, score):
    try:
        return int(card) # if the card is just a number it will return that to be added to the player's current score
    except:
        if card != "A": # if the card is a J Q or K it will return 10
            return 10
        if score + 11 <= 21: # returns 11 for an ace if it won't make player go bust
            return 11
        else:
            return 1 # returns 1 for an ace if 1 would make dealer go bust

def round(hand, score, dealer_hand, dealer_score, deck):
    while True and len(deck) != 0: # manages player turn
        print(f"Your current hand is {hand} with a score of {score}")
        player_choice = input("Hit (H) or Stand (S): ").lower() # takes player choice
        
        if player_choice == "h":
            card = deck.pop() # takes the card off the top of the deck
            hand.append(card) # adds the card to the player's hand
            score += get_value(card, score) #adds new card to player's score
            
            print(f"You picked up: {card}")
            time.sleep(1)
            os.system("cls")
        else:
            break
    
    while dealer_score < 17 and len(deck) != 0: # manages dealers turn
        card = deck.pop() # takes the card off the top of the deck
        dealer_hand.append(card) # adds the card to the dealers's hand
        dealer_score += get_value(card, dealer_score) #adds new card to dealer's score
    
    return hand, score, dealer_hand, dealer_score, deck

# MAIN PROGRAM

print("""Automatic Jackblack Player
--------------------------""")

games = 0
blackjack = 0
game_end = 0
bust = 0

deck = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]*4 # creates the cards that will be in the deck
random.shuffle(deck) # shuffles the deck

while True:
    hand = []
    score = 0
    dealer_hand = []
    dealer_score = 0

    while True and len(deck) != 0: # this controls if a round is active or not
        hand, score, dealer_hand, dealer_score, deck = round(hand, score, dealer_hand, dealer_score, deck)
        break
    
    if score == 21:
        print("You've got blackjack")
        games += 1
        blackjack += 1
    elif score < 21:
        print(f"You've scored {score}")
        games += 1
        game_end += 1
    else:
        print(f"You've gone bust with a deck of {score} :(")
        games += 1
        bust += 1

    print(f"Your cards were {hand}")

    if len(deck) < 1:
        print("The deck has run out of cards")
        break

print(f"""You played {games} games.
You got {blackjack} blackjacks.
You got {game_end} games that weren't blackjack or bust.
You bust {bust} times.""")
input("Press enter to exit")