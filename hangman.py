#To do list
#1. 
#2. in wordle project make alternative capital letter for green, lowercse for yellow, underscore for incorrect
import random
import os
#print hangman function
def printMan():
    if guesses == 6:
        print("\t________\n"
               "\t|     |\n"           
               "\t|      \n"          
               "\t|      \n"          
               "\t|      \n"          
               "\t|      \n"  
               "\t————————\n"        
                            )
    if guesses == 5:
        print("\t________\n"
               "\t|     |\n"           
               "\t|     O \n"          
               "\t|      \n"          
               "\t|      \n"          
               "\t|      \n"  
               "\t————————\n"        
                            )
    if guesses == 4:
        print("\t________\n"
               "\t|     |\n"           
               "\t|     O \n"          
               "\t|     | \n"          
               "\t|      \n"          
               "\t|      \n"  
               "\t————————\n"        
                            )
    if guesses == 3:
        print("\t________\n"
               "\t|     |\n"           
               "\t|     O \n"          
               "\t|    —| \n"          
               "\t|      \n"          
               "\t|      \n"  
               "\t————————\n"        
                            )
    if guesses == 2:
        print("\t________\n"
               "\t|     |\n"           
               "\t|     O \n"          
               "\t|    —|— \n"          
               "\t|      \n"          
               "\t|      \n"  
               "\t————————\n"        
                            )
    if guesses == 1:
        print("\t________\n"
               "\t|     |\n"           
               "\t|     O \n"          
               "\t|    —|— \n"          
               "\t|    / \n"          
               "\t|      \n"  
               "\t————————\n"        
                            )
    if guesses == 0:
        print("\t________\n"
               "\t|     |\n"           
               "\t|     O \n"          
               "\t|    —|— \n"          
               "\t|    / \\\n"          
               "\t|      \n"  
               "\t————————\n"        
                            )
complete = False
alreadyGuessed = False
guesses = 7
numWrong = 0
guess = ""
wordStatus = ""
wrongGuesses = ""
guessedLetters = ""
#function to clear console
def clearConsole():
    os.system('clear')
    
clearConsole()
# Open the file in read mode
with open("AllWords.txt", "r") as file:
    allText = file.read()
    words = list(map(str, allText.split()))
    
    # assign selected string as word
    word = (random.choice(words))
#make word uppercase
word = word.upper()
 #copy equivalent number of underscores into wordStatus
wordStatus = "_"*len(word)
wordStatus = list(wordStatus)
print("A random word has been generated.")
#cycle through guesses
while guesses != 0 and complete == False:
    correct = False
    reGuess = False
    print("Your current word status: " + ''.join(wordStatus))
    while guess.isalpha == False or len(guess) != 1 or alreadyGuessed == True:
        alreadyGuessed = False 
        guess = input("What letter would you like to guess?: ")
        guess = guess.upper()
        if len(guess) == 1:
            for i in range(len(guessedLetters)):
                if guessedLetters[i] == guess:
                    alreadyGuessed = True
        if alreadyGuessed == True:
            print("You already guessed that letter!")
    guessedLetters += guess
    for i in range(len(word)):
        if guess == word[i]:
            wordStatus[i] = guess
            correct = True
    if correct == False:
        wrongGuesses = wrongGuesses + guess
        numWrong += 1
        guesses -= 1
    clearConsole()
    if guesses <= 6:
        printMan()
        print("Incorrect letters you have guessed: " + wrongGuesses)
    #reset guess
    guess = ''
    if word == ''.join(wordStatus):
        print(word)
        print("Congratulations! You figured out the word!")
        complete = True
    if guesses == 0:
        print("You failed to guess the word...The word was " + word)