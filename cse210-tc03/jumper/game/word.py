import random

class Word():
    """A code template for getting a word for the user to guess. The responsibility of this
    class object is to retrieve a word from a large list and check to see if the letter that
    is guessed by the user is in the word or not.

    Stereotype:
        Information Holder

    Attributes:
        wordList (list): The list of words from the txt given text file.
        correctWordList (string): Selects a new random word from the wordList file for each game.
        correctWord (string): The word that will be used throughout the game session.
    """
    def __init__(self): #constructs the correctWord Variable from given text list.
        """Class constructor. Declares and initializes instance attributes.

        Args:
            self (word): An instance of Word.
        """
        f = open("wordlist.txt", "r")
        wordList = []
        self.correctWordList = ""
        self.correctWord = ""
        for line in f:  #Converts text file into array
            stripped_line = line.strip()
            line_list = stripped_line.split()
            wordList.append(line_list)
        f.close()

        self.correctWordList = wordList[random.randint(0 , len(wordList))] #Selects a random word between 0 and the length of the list. 

        self.correctWord = self.correctWord.join(self.correctWordList)

    def checkLetter(self, guess):
        """Checks to see if the letter entered by the user is in the word and places it in the correct placement.

        Args:
            self (Word): An instance of Word.

        Returns:
            list: Updates the positions of the correct letters guessed.
        """
        positionsOfCorrect = []
        i = 0 #i is the current position being scanned. 

        for char in self.correctWord:

            if char == guess: 
                positionsOfCorrect.append(i) #i begins at zero, iterates after checking and posting the value
                i = i + 1
            
            else: 
                i = i + 1 #After checking position, i becomes new position .

        #Returns the array that tell the program the POSITION of what answers were correct.
        #Use the update array function to do array[positionsOfCorrect[i]] = guess
        #Where i is the position of the positionsOfCorrect Variable

        return positionsOfCorrect # this method is called in director
