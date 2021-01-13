import random

class Deal:
    def __init__(self):
        self.cards = []
        self.score = 0
        self.i = 0

    def new_card(self):
        self.cards.append(random.randint(1,52)) #cards go from 1-52, adds a new card to list
        self.i += 1 #increases i value for tracking next card

    def compare(self, guess): 
        result = False

        if self.cards[self.i - 2] > self.cards[self.i - 1]: #checks the two card variables and compares
            firstIsHigher = True
        else:
            firstIsHigher = False

        if firstIsHigher == True and guess == 'l': #returns true or false based on user input
            print("Condition 1")
            result = True

        elif firstIsHigher == True and guess == 'h':
            print("Condition 2")
            result = False

        elif firstIsHigher == False and guess == 'h':
            print("Condition 3")
            result = True

        elif firstIsHigher == False and guess == 'l':
            print("Condition 4")
            result = False

        return result


class Hilo:
    def __init__(self):
        pass

    def start_game(self):
        deal = Deal()
        deal.new_card()
        playing = True
        while playing:
            print("\nThe card is: ", deal.cards[deal.i - 1]) #card number is the previous i number, compared card is the current i
            
            guess = input("Higher or lower? [h/l] ") #get user input here, should put check to make sure they type h or l

            deal.new_card()

            # Here the new card is compared to the guess
            result = deal.compare(guess)

            if result == True:   #Announces the winner and gives points
                print("\nYou won! +100 points\n") 
                deal.score = deal.score + 100
            elif result == False:
                print("\nBetter luck next time! -50 points\n")
                deal.score = deal.score - 50

            print("The new card was: ", deal.cards[deal.i -1], "\n") #declare the new card

            print("Your score is: ", deal.score) #print calculated score
            if deal.score > 0:      #test if game end and prompt user to play again
                playing = input("Keep playing? [y/n] ") in ['y']
            else:
                print("Sorry! Game over!")
                playing = False


if __name__ == "__main__":
    hilo = Hilo()
    hilo.start_game()