from random import shuffle
#imoprts shuffle function from random library to shuffle our deck list
from time import sleep


#makes the deck
#used pop() to draw a card from list of cards and takes element away
def creatDeck():
    Deck = []
    #makes our face cards for each suit
    faceValues= ["A", "J", "Q", "K"]

    for i in range(4):
        for card in range(2,11): #each suit has  a card of 2-1
            Deck.append(str(card))

        for card in faceValues:
            Deck.append(card)
    shuffle(Deck)   #shuffle cards
    return Deck



class Player:
    def __init__(self, Hand = [], money = 100):
        self.hand = Hand
        self.score = self.setScore()    #calculates the score 
        self.money = money
        self.bet = 0

    #alows us to call print on player Ex: print(player instance)    
    def __str__(self):
        currentHand = ""    #self.hand = ["A", "10"]
                            #A 10
        for card in self.hand:
            currentHand += str(card) + " "
        
        finalStatus = currentHand  + "Score: " + str(self.score)
        #A 10 2 5 score: 18
        return finalStatus
    

    def setScore(self):
        self.score = 0  #"3 4" -> "3 4 10"
                        #7 -> 17
        #initialy sets core value to 0
        #score assigned to each card in a dictionary
        faceCardsDict = {"A": 11, "J":10, "Q": 10, "K":10,
                            "2":2,"3":3,"4":4,"5":5,"6":6,"7":7,
                            "8":8,"9":9,"10":10}

        aceCounter = 0
        
        #convert number cards into integers
        for card in self.hand:      #"10"
            self.score += faceCardsDict[card]
            if card == "A":
                aceCounter += 1
            if self.score > 21 and aceCounter !=0:
                self.score -= 10
                aceCounter -+ 1
        
        return self.score   #gives us the calculations of our score

    #recalculates our score after addind a card
    def hit(self,card):
        self.hand.append(card)
        self.score = self.setScore()

    #resets our hand
    def play(self,newHand):
        self.hand = newHand
        self.score = self.setScore()
    
    #lets us make bets
    def betMoney(self,amount):
        self.money -+ amount    #money 100; bet(20)
        self.bet += amount      #money -> 80 bet 0->20

    def win(self,result):
        if result == True:
            #checks if we have a black jack and give 2.5* money 
            if self.score == 21 and len(self.hand) == 2:
                self.money += 2.5*self.bet
            else:
                self.money += 2*self.bet
            self.bet = 0
        else:
            self.money -= self.bet
            self.bet = 0

    #function if player and house tie it gives the money back to player
    def draw(self):
        self.money += self.bet
        self.bet = 0

    #checks for blackjacks and gives win to appropriat player
    def hasBlackJack(self):
        if self.score == 21 and len(self.hand) == 2:
            return True
        else:
            return False

#shows all cards except the first card in the house hand
def printHouse(House):
    for card in range(len(House.hand)): #len(house.hand) = 5
                                        #0,1,2,3,4
        if card == 0:
            print("X", end=" ")
        elif card == len(House.hand) - 1:
            print(House.hand[card])
        else:
            print(House.hand[card], end=" ")










cardDeck = creatDeck()  #
#gives the player and house 2 random cards from the deck
firstHand = [cardDeck.pop(),cardDeck.pop()]
secondHand = [cardDeck.pop(), cardDeck.pop()]

Player1 = Player(firstHand)
House = Player(secondHand)
cardDeck = creatDeck()
while(Player1.money > 0):
    if len(cardDeck) < 20:  #checks our cards and reshuffles them if there is 20
        cardDeck = creatDeck()
    #Gives each player 2 cards
    firstHand = [cardDeck.pop(), cardDeck.pop()]
    secondHand = [cardDeck.pop(), cardDeck.pop()]
    Player1.play(firstHand)
    House.play(secondHand)

    Bet = int(input("Please enter your bet: "))
    Player1.betMoney(Bet)
    #print(cardDeck)
    print(Player1)
    printHouse(House)

    if Player1.hasBlackJack():
        if House.hasBlackJack():
            Player1.draw()
        else:
            Player1.win(True)
    else:
        while(Player1.score < 21):
            action = input("Do you want to take a card? (y/n): ")
            if action == "y":
                #pop() removes element from bottom of cardDeck list
                Player1.hit(cardDeck.pop())
                print(Player1)
                printHouse(House)
            else:
                break
        
        while(House.score < 16):
            House.hit(cardDeck.pop())
            print(House)
            sleep(1)
        #checks the condition state of game and decides if game is loss or win ofr house and player
        if Player1.score > 21:
            if House.score > 21:
                Player1.draw()
            else:
                Player1.win(False)

        elif Player1.score > House.score:
            Player1.win(True)
        
        elif Player1.score == House.score:
            Player1.draw()
        else:
            if House.score > 21:
                Player1.win(True)
            else:
                Player1.win(False)

    print(Player1.money)
    print(House)

if Player1.money <= 0:
    print("You have no money left. You lose. Find another hobby...  ")
