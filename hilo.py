class Deal:
    def __init__(self):
        self.cards = []
        self.score = 0

    def new_card(self):


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
            print("Your score is: ") #print calculated score
            print("Keep playing? [y/n] ") #get user input here