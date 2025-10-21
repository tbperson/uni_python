# imports
from random import shuffle
from time import sleep

# initialisation
cards = [1,1,1,1,2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10]

dealer_cards = []
player_cards = []

## Controlling variables
dealer_risk = 0.9 ## Adjust to make dealer more or less risky (
                ## 0 = dealer never risks, 1 = dealer always risks
                ## This variable only matters when dealer has between 12 and 17
                ## as a dealer will always hit on 11 or less




# pregame
shuffle(cards)

# itial deal
player_cards.append(cards.pop())
dealer_cards.append(cards.pop())
player_cards.append(cards.pop())
dealer_cards.append(cards.pop())
print("Dealer has: ? and", dealer_cards[1])
sleep(1)
print("You have:", player_cards, "for a total of", sum(player_cards))
sleep(1)


## Function to check win conditions
def check_win(player_cards, dealer_cards):
    if sum(player_cards) > 21:
        return "Dealer wins (player bust)"
    elif sum(dealer_cards) > 21:
        return "Player wins (dealer bust)"
    elif sum(player_cards) > sum(dealer_cards):
        return "Player wins"
    elif sum(player_cards) < sum(dealer_cards):
        return "Dealer wins"
    else:
        return "Push"

def player_turn():
    ##print("Dealer has:", dealer_cards ) ### Cheats
    choice = input("Would you like to hit or stay? ").lower()
    if choice == "hit":
        player_cards.append(cards.pop())
        sleep(1)
        print("You have:", player_cards, "for a total of", sum(player_cards))
        if sum(player_cards) > 21:
            sleep(1)
            print("You bust! Dealer wins.")
        else:
            player_turn()
    elif choice == "stay":
        sleep(1)
    
    ## MORE CHEATS
    elif choice == "select":
        player_cards.append(int(input("Select a card to add to your hand (1-10): ")))
    elif choice == "view":
        print("Dealer has:", dealer_cards ) 
        player_turn()
    elif choice == "steal":
        player_cards.append(dealer_cards.pop())
        print("You have:", player_cards, "for a total of", sum(player_cards))
        if sum(player_cards) > 21:
            sleep(1)
            print("You bust! Dealer wins.")
        else:
            player_turn()


def dealer_consider_player():
    ## For this function, dealer will try to guess what card the player has and take that into consideration, as well as their moves
    player_cards = len(player_cards)
    

## Dealer turn function
def dealer_turn():
    sleep(3) ## Dealer thinking time

    ## Conditions where dealer always stays
    ## Condition where dealer has blackjack
    if sum(dealer_cards) == 21:
        print("Dealer stays")
        pass

    ## Dealer will not hit on 18 or more
    if sum(dealer_cards) >= 18:
        print("Dealer stays")
        pass



    ## Conditions where dealer has to hit
    ## Dealer has 10 less than blacjack (11 or less)
    if sum(dealer_cards) <= 11:
        print("Dealer hits")
        dealer_cards.append(cards.pop())
        dealer_turn()

    ## Player shows a 10 and dealer has less than 18
    if player_cards[0] == 10 and sum(dealer_cards) < 18:
        print("Dealer hits")
        dealer_cards.append(cards.pop())
    
    
    ## Conditions where dealer makes a choice on whether to hit or stay
    if sum(dealer_cards) > 11 and sum(dealer_cards) < 18:
        dealer_stays = False ## Local to prevent dealer from staying then going
        ## Dealer calculates on chance of bust (include player in this soon)
        cards_left = cards.copy() 
        cards_left.append(player_cards[0])
        bust_cards = []
        for card in cards_left:
            if card + sum(dealer_cards) > 21:
                bust_cards.append(card)
                if len(bust_cards)/len(cards_left) >= dealer_risk:
                    print("Dealer stays")
                    dealer_stays = True
                    break
        if len(bust_cards)/len(cards_left) >= 1-dealer_risk:
            if dealer_stays == False:
                print("Dealer hits")
                dealer_cards.append(cards.pop())
                dealer_turn()
             

 
## Gameloop
while True:
    player_turn()
    dealer_turn()
    print("Dealer has:", dealer_cards, "for a total of", sum(dealer_cards))
    print("You have:", player_cards, "for a total of", sum(player_cards))
    sleep(3)
    print(check_win(player_cards, dealer_cards))
    break

