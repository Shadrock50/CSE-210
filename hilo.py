import random

class Deal:
    def __init__(self):
        self.cards = []
        self.score = 0

    def new_card(self):
        pass #for now

    def guess(self):
        pass #for now


class Hilo:
    def __init__(self):
        pass

    def start_game(self):
        deal = Deal()
        deal.new_card()
        playing = True
        while playing:
            print("The card is: ") #insert card number here
            print("Higher or lower? [h/l] ") #get user input here
            deal.new_card()

            # Here the new card is compared to the guess

            print("Your score is: ", deal.score) #print calculated score
            if deal.score > 0:
                playing = input("Keep playing? [y/n] ") in ['y']
            else:
                print("Sorry! Game over!")
                playing = False

if __name__ == "__main__":
    hilo = Hilo()
    hilo.start_game()