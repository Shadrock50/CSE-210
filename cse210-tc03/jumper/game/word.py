import random

class Word():
    def __init__(self): #constructs the correctWord Variable from given text list.
        """ good luck shad """
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
