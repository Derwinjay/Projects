import string
 

# print(input("enter"))
# print(chr(27) + "[2J") camand to clear the console
alphabet = set(string.ascii_uppercase)
used_letters = set() #empty []



def Hang_man():
    counter = 0
    #player enters a word for the other player to guess
    ANS_word = input("Player 1 enter a word: \n").upper()
    print(chr(27) + "[2J")  #clears the screen so the guesing player can't see the word
    while(counter < 6):

        
        #makes a list of the word that needs to be guessed, compares the used_leters list
        #with each index value of the ANS_word. prints the letter if its there, prints a - if not
        word_list = [letter if letter in used_letters else "-" for letter in ANS_word]        

        print("Current word: ", " ".join(word_list))
        
        #condition i was going to use to break the game but changed my mind
        # if "-" in word_list:
        #     game_going = True
        # else:
        #     game_going = False

        
        
        
        user_letter = input("Enter a letter, and guess the word\n").upper()
        if "-" in word_list:
            if user_letter in alphabet - used_letters:
                used_letters.add(user_letter)
                if user_letter not in ANS_word:
                    
                    draw_Hman(counter)
                    counter += 1

            elif user_letter in used_letters:
                print("You used that letter already. Please enter a different letter")
                print("Here are your used letters.")
                print(used_letters)
                draw_Hman(counter)
                counter += 1

            else:
                print("You entered a non valid answer.")
                print("Here are your used letters.")
                print(used_letters)
                draw_Hman(counter)
                counter += 1
        else:
            print("You gused the word. press enter.")
            break
    return ANS_word

#function that draws the hang man dude

def draw_Hman(counter):

    if counter == 0:
        print("---------")
    elif counter == 1:
        print("    |    ")
        print("    |    ")
        print("    |    ")
        print("---------")

    elif counter == 2:
        print("    -----")
        print("    |    ")
        print("    |    ")
        print("    |    ")
        print("---------")

    elif counter == 3:
        print("    -----")
        print("    |    o")
        print("    |    ")
        print("    |    ")
        print("---------")

    elif counter == 4:
        print("    -----")
        print("    |    o")
        print("    |   /|^")
        print("    |    ")
        print("---------")

    elif counter == 5:
        hangDood = Hang_man()
        print("    -----")
        print("    |    o")
        print("    |   /|^")
        print("    |    A")
        print("---------")
        print("You lose!")
        print(hangDood.ANS_word)
       

Hang_man()