import random
import sys
from english_words import get_english_words_set
englishDictionary = get_english_words_set(['web2'], lower=True)
fiveLetterWords = [word for word in englishDictionary if len(word) == 5]

GREEN = '\033[92m'
YELLOW = '\033[93m'
GRAY = '\033[90m'
RESET = '\033[0m'

keyboardLayout = [
    "Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P",
    "A", "S", "D", "F", "G", "H", "J", "K", "L",
    "Z", "X", "C", "V", "B", "N", "M"
]

letterColors = {}

def colorKeyboard(guess, colors):
    for letter, color in zip(guess, colors):
        letterColors[letter.upper()] = color
    
    colored_layout = []
    for letter in keyboardLayout:
        if letter in letterColors:
            color = letterColors[letter]
            if color == 'green':
                colored_layout.append(GREEN + letter + RESET)
            elif color == 'yellow':
                colored_layout.append(YELLOW + letter + RESET)
            elif color == 'gray':
                colored_layout.append(GRAY + letter + RESET)
        else:
            colored_layout.append(letter)
    
    for row in [colored_layout[:10], colored_layout[10:19], colored_layout[19:]]:
        print(" ".join(row))

wordList = fiveLetterWords
guessNum = -1
gameOver = False
word = random.choice(wordList)
inputWord = ""

guesses = ["", "", "", "", "", ""]

def makeBoard(text, colors):
    word = ""
    if guessNum == -1:
        for i in range(6):
            guesses[i] = "_ _ _ _ _"
        printBoard(guesses)
    else:
        for letter, color in zip(text, colors):
            if color == 'green':
                word += GREEN + letter + RESET + " "
            elif color == 'yellow':
                word += YELLOW + letter + RESET + " "
            elif color == 'gray':
                word += GRAY + letter + RESET + " "
        guesses[guessNum] = word
        printBoard(guesses)

def get_colors(guess, secret_word):
    colors = ['gray'] * len(guess)
    guess = guess.upper()
    secret_word = secret_word.upper()

    secret_letters = list(secret_word)

    for i, letter in enumerate(guess):
        if letter == secret_word[i]:
            colors[i] = 'green'
            secret_letters.remove(letter)
    for i, letter in enumerate(guess):
        if colors[i] == 'gray' and letter in secret_letters:
            colors[i] = 'yellow'
            secret_letters.remove(letter)

    return colors

def printBoard(lines):
    clearScreen()
    for guess in guesses:
        print(guess)

def checkGuess(inputWord):
    if (inputWord == word):
        return True
    else:
        return False

def clearScreen():
    sys.stdout.write("\033[2J\033[H\033[3J")
    sys.stdout.flush()

#MAIN GAME LOOP
while (guessNum < 5):
    if guessNum == -1:
        makeBoard(None, None)
        colorKeyboard(inputWord, get_colors(inputWord, word))
        while True:
            inputWord = input("Make your guess: ")

            if len(inputWord) != 5:
                print("Please enter a 5 letter word!")
                continue

            if inputWord not in englishDictionary:
                print("Please enter a valid English word!")
                continue

            break
    else:
        makeBoard(inputWord, get_colors(inputWord, word))
        colorKeyboard(inputWord, get_colors(inputWord, word))
        while True:
            inputWord = input("Make your guess: ")

            if len(inputWord) != 5:
                print("Please enter a 5 letter word!")
                continue
            break
    
    if checkGuess(inputWord):
        gameOver = True
        print("You Win!")
        guessNum += 1
        break
    else:
        guessNum += 1

makeBoard(inputWord, get_colors(inputWord, word))
print("The correct word was: " + word)
if gameOver == True:
    print("You solved in " + str(guessNum + 1) + " guesses")