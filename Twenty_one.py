##------------------------------------------------------------Twenty-One------------------------------------------------------------##
##----------------------------------------------------------              ----------------------------------------------------------##
##------------------------------------------------------------          ------------------------------------------------------------##
##----------------------------------------------------------------------------------------------------------------------------------##
import random

## The Deck
deck = {
    "ace of hearts": 11,
    "two of hearts": 2,
    "three of hearts": 3,
    "four of hearts": 4,
    "five of hearts": 5,
    "six of hearts": 6,
    "seven of hearts": 7,
    "eight of hearts": 8,
    "nine of hearts": 9,
    "ten of hearts": 10,
    "jack of hearts": 10,
    "queen of hearts": 10,
    "king of hearts": 10,

    "ace of diamonds": 11,
    "two of diamonds": 2,
    "three of diamonds": 3,
    "four of diamonds": 4,
    "five of diamonds": 5,
    "six of diamonds": 6,
    "seven of diamonds": 7,
    "eight of diamonds": 8,
    "nine of diamonds": 9,
    "ten of diamonds": 10,
    "jack of diamonds": 10,
    "queen of diamonds": 10,
    "king of diamonds": 10,

    "ace of spades": 11,
    "two of spades": 2,
    "three of spades": 3,
    "four of spades": 4,
    "five of spades": 5,
    "six of spades": 6,
    "seven of spades": 7,
    "eight of spades": 8,
    "nine of spades": 9,
    "ten of spades": 10,
    "jack of spades": 10,
    "queen of spades": 10,
    "king of spades": 10,

    "ace of clubs": 11,
    "two of clubs": 2,
    "three of clubs": 3,
    "four of clubs": 4,
    "five of clubs": 5,
    "six of clubs": 6,
    "seven of clubs": 7,
    "eight of clubs": 8,
    "nine of clubs": 9,
    "ten of clubs": 10,
    "jack of clubs": 10,
    "queen of clubs": 10,
    "king of clubs": 10

}
## Simulates a pile of used cards to be returned to deck
pile = {}
## Player hit or stay, return total count
def hit_stay(player_total, continu):
    try:
        choice=int(input("\nPress '1' to hit or '2' to stay: "))
        if (choice == 1):
            draw = random.choice(list(deck.keys()))
            player_total += deck.get(draw)
            print("\nYou drew ", draw)
            print("Your new total is: ", player_total, "\n")
            pile.update(deck)
            del deck[draw]
        elif (choice == 2):
            print("You stayed.\n")
            continu = False
        else:
            print("You didn't hit '1' or '2'!")
            hit_stay(player_total,continu)
    except:
        print("Input error!")
        hit_stay(player_total,continu)
        
    
    return(player_total,continu)

## Dealer AI, hit or stay
def dealer(dealer_total):
    if (dealer_total < 17):
        print("Dealer Hits!")
        draw = random.choice(list(deck.keys()))
        dealer_total += deck.get(draw)
        #print("\nDealer's new total is: ", dealer_total, "\n")
        pile.update(deck)
        del deck[draw]
        
    elif (dealer_total > 17 and dealer_total < 22):
        print("Dealer stays.\n")

    return(dealer_total)

## Body for the main game
def game(win,loss):
    ## Initialize card hand dictionaries
    dealer_hand = {}
    player_hand = {}
    
    ## Dealer draw
    draw = random.choice(list(deck.keys()))
    #d_card_1 = draw
    dealer_hand["dealer_card_1"] = deck.get(draw)
    pile.update(deck)
    del deck[draw]
    

    draw = random.choice(list(deck.keys()))
    #d_card_2 = draw
    dealer_hand["dealer_card_2"] = deck.get(draw)
    pile.update(deck)
    del deck[draw]
    
    dealer_total = dealer_hand["dealer_card_1"] + dealer_hand["dealer_card_2"]
    #print("\nDealer hand: ", d_card_1, " and ", d_card_2, " --> Total: ", dealer_total)

    ## Player draw, display cards and total
    draw = random.choice(list(deck.keys()))
    card_1 = draw
    player_hand["p_card_1"] = deck.get(draw)
    pile.update(deck)
    del deck[draw]

    draw = random.choice(list(deck.keys()))
    card_2  = draw
    player_hand["p_card_2"] = deck.get(draw)
    pile.update(deck)
    del deck[draw]
 

    player_total = player_hand["p_card_1"] + player_hand["p_card_2"]
    print("\nYour hand: ", card_1, " and ", card_2, " --> Total: ", player_total)

    ## Hit or stay phase
    continu = True
    while (continu == True):
        if (player_total >= 21):
            continu = False
            break
        player_total, continu = hit_stay(player_total, continu)
        if (player_total >= 21):
            break
        dealer_total = dealer(dealer_total)
        if (dealer_total >= 21):
            break
    
    ## Replenish deck
    deck.update(pile)
    pile.clear()    
    ## Determine winner
    win_condition(player_total, dealer_total, win, loss)


    
## Win conditions
def win_condition(player_total, dealer_total, win, loss):
    print("Your total: ", player_total, "\nDealer total: ", dealer_total, "\n")
    if (dealer_total > 21):
        print("Dealer busts, you win!\n")
        win += 1
    elif (player_total > 21):
        print("You bust, dealer wins.\n")
        loss += 1
    elif (player_total > dealer_total):
        print("You win!\n")
        win += 1
    elif (dealer_total > player_total):
        print("Dealer wins.\n")
        loss += 1
    elif (player_total == dealer_total):
        print("Draw, dealer wins.\n")
        loss += 1
    
    print("Wins: ",win, "Losses: ",loss)
    ## Ask user if they want to keep playing
    print("\nPlay again?")
    start_menu(win,loss)


## Start menu
def start_menu(win,loss):
    try:
        choice_=int(input("Type '1' to play\nType '2' to exit: "))
        if(choice_ == 1):
            game(win,loss)
        elif(choice_ == 2):
            print("\nPlay again soon!")

        else:
            print("Input error!")
            start_menu(win,loss)
    except:
        print("Invalid input!")
        start_menu(win,loss)

## Enter user name
def name_input(win,loss):
    print("\n")
    print("##----------------------------------------------------Twenty-One----------------------------------------------------##")
    print("##--------------------------------------------------              --------------------------------------------------##")
    print("##------------------------------------------------                  ------------------------------------------------##")
    print("##------------------------------------------------------------------------------------------------------------------##")
    name=input("Enter your name: ")
    print("\nWelcome to 21 " + str(name) + ", enjoy the game!\n")
    start_menu(win,loss)

## Starts the program
win = 0
loss = 0
name_input(win,loss)