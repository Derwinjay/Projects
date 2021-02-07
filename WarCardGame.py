from random import shuffle  #use to shuffe deck
from time import sleep #use to slow the game
from itertools import islice #used to cut the deck into 2 parts
from sys import exit

def creatDeck():
    deck = []

    faceValues = ["A","K","Q","J"]

    for i in range(4):
        for card in range(2,11):
            deck.append(str(card))
        
        for card in faceValues:
            deck.append(card)
    shuffle(deck)
    return deck

class Player:

     #The cards that are up for bounty, and do not change among players
    warPile = [] 

    #pile is the mini deck each player has
    def __init__(self,name, Pile = []):
        self.name = name
        self.pile = Pile
        self.warCards = []    #the card that each player flips off the top of their pile for comparison
        self.warPoint = 0
        
        

    def __str__(self):
        #shows how many cards a player has
        
        yourCardCount = "You have " + str(len(self.pile)) + " cards in your pile " + str(self.name) + ".\n"
        return yourCardCount 

    #This is used to keep the ranks of the card values
    def cardRanks(self):

        faceCardsDict = {"A": 13, "J":11, "Q": 12, "K":13,
                            "2":2,"3":3,"4":4,"5":5,"6":6,"7":7,
                            "8":8,"9":9,"10":10}
        
        for card in self.warCards:
            for i in faceCardsDict:
                self.warPoint = faceCardsDict[card]

    #winner gets the cards in the warPile
    def winWar(self):
        
        for cards in Player.warPile:
            self.pile.append(cards)
        
        Player.warPile = [] #emptys the card pile
        shuffle(self.pile)

    #Event that happens if players tie in rank
    def WAR(self):

        for cards in self.warCards:
            Player.warPile.append(cards)
        self.warCards = []

        for card in range(4):
            self.warCards.append(self.pile[card])

        for card in self.warCards:
            self.pile.remove(card)
        shuffle(self.pile)
    
    #Funtion that is used to place card for battle
    def Battle(self,cardNumber):
        #takes a number entered by the user and sets that number a a index for the users deck
        #adds that index value to self.warCars list to battle with
        (self.warCards).append(self.pile[cardNumber])
        
        del self.pile[cardNumber]   #takes that index value out of the users deck
    
    def afterBattle(self):
        #Puts the cards used to battle with in a list that does not change
        #And sets the users warCard list to empty
        for cards in self.warCards:
            Player.warPile.append(cards)
        self.warCards = []

def rules():    #gives the object of the game and how to win
    print(
    '''The object of the game is to take a card from your \n
    deck and and do battle with your oponent. The player with the\n
    bigest card value wins. If its a tie, then both players take 4 cards\n
    off the top of the deck and compare the 4th card, whoevers card is bigger gets all the cards.\n
    Player who has 0 cards or gets to WAR with less the 4 card losses.")
    print("A = 13, K = 13, Q = 12, J = 11
    ''')
    try:
        gameStart = input("Do you want to resume the game?: \n (y/n): ")
    except(ValueError):
        print("You entered a non valid answer. Resuming game\n")
        gameStart = "y"

    if gameStart == "y":
        print("Continuing game...")
        sleep(3)
    elif gameStart == "n":
        exit()





Deck = iter(creatDeck())
#Takes the deck cuts it in half
split_length = [26,26]
#Gives us 2 halves of a deck and puts them into a list
Deck_player = [list(islice(Deck,elem)) for elem in split_length]


P1 = input("Enter Your name Player 1:\n")
P2 = input("Enter your name Player 2:\n")

Player1 = Player(P1, Deck_player[0])
Player2 = Player(P2, Deck_player[1])
print(Player1)
print(Player2)

while len(Player1.pile) > 0 and len(Player2.pile) > 0:
#Store the value of card that each player wants to use
    #print(Player1.pile)
    #print(Player2.pile)
    print("Type help for rules.")
    War1 = input(f"What card do you want to use from your deck {Player1.name}? Enter a number from 1 to {len(Player1.pile)}\n")
    War2 = input(f"What card do you want to use from your deck {Player2.name}? Enter a number from 1 to {len(Player2.pile)}\n")
    
    if War1 == "help" or War2 == "help":
        rules()
        War1 = int(input(f"What card do you want to use from your deck {Player1.name}? Enter a number from 1 to {len(Player1.pile)}\n")) - 1
        War2 = int(input(f"What card do you want to use from your deck {Player2.name}? Enter a number from 1 to {len(Player2.pile)}\n")) - 1
    
    War1 = int(War1) - 1
    War2 = int(War2) - 1

    Player1.Battle(War1)
    #print(Player1.warCards)
    Player2.Battle(War2)
    #print(Player2.warCards)
    Player1.cardRanks()
    Player2.cardRanks()

    print(Player1.warCards, "This is your card P1")
    print(Player2.warCards, "This is your card P2")

    #checks if Player 1 has won
    if Player1.warPoint > Player2.warPoint:
        print(Player1.name, "won the battle")
        Player1.afterBattle()
        Player2.afterBattle()
        print(Player.warPile, "These are the cards that were won.\n")
        sleep(2)
        Player1.winWar()
        
    #checks if Player 2 has won
    elif Player1.warPoint < Player2.warPoint:
        print(Player2.name, "won the battle")
        Player1.afterBattle()
        Player2.afterBattle()
        print(Player.warPile, "These are the cards that were won.\n")
        sleep(2)
        Player2.winWar()
        

    #if there is a tie
    else:

        while Player1.warPoint == Player2.warPoint:
            if len(Player1.pile) > 3 and len(Player2.pile) > 3:
                print("WAR has started...Fliping 4 cards from each players deck. (pause for suspense)")
                Player1.WAR()
                Player2.WAR()
                sleep(4)
                Player1.cardRanks()
                Player2.cardRanks()
                if Player1.warPoint > Player2.warPoint:
                    print(Player1.name, "won the War!!")
                    Player1.afterBattle()
                    Player2.afterBattle()
                    print(Player.warPile, "\n These are the cards that were won in the war\n")
                    sleep(2)
                    Player1.winWar()
                    
                elif Player1.warPoint < Player2.warPoint:
                    print(Player2.name, "won the War!!")
                    Player1.afterBattle()
                    Player2.afterBattle()
                    print(Player.warPile, "\n These are the cards that were won in the war\n")
                    sleep(2)
                    Player2.winWar()
                    
            else:
                if Player1.pile <= 3:
                    print(Player1.name + ", you are out of card. You lose the game.")
                    exit()
                elif Player2.pile <= 3:
                    print(Player1.name + ", you are out of card. You lose the game.")
                    exit()

    if len(Player1.pile) == 0:
        print(Player1.name + ", you are out of card. You lose the game.")
        exit()
    elif len(Player2.pile) == 0:
        print(Player1.name + ", you are out of card. You lose the game.")
        exit()