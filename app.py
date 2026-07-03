import random
import sys
from english_words import get_english_words_set
englishDictionary = get_english_words_set(['web2'], lower=True)

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

wordList = words = [
    "About", "Alert", "Argue", "Beach",
    "Above", "Alike", "Arise", "Began",
    "Abuse", "Alive", "Array", "Begin",
    "Actor", "Allow", "Aside", "Begun",
    "Acute", "Alone", "Asset", "Being",
    "Admit", "Along", "Audio", "Below",
    "Adopt", "Alter", "Audit", "Bench",
    "Adult", "Among", "Avoid", "Billy",
    "After", "Anger", "Award", "Birth",
    "Again", "Angle", "Aware", "Black",
    "Agent", "Angry", "Badly", "Blame",
    "Agree", "Apart", "Baker", "Blind",
    "Ahead", "Apple", "Bases", "Block",
    "Alarm", "Apply", "Basic", "Blood",
    "Album", "Arena", "Basis", "Board",
    "Boost", "Buyer", "China", "Cover",
    "Booth", "Cable", "Chose", "Craft",
    "Bound", "Calif", "Civil", "Crash",
    "Brain", "Carry", "Claim", "Cream",
    "Brand", "Catch", "Class", "Crime",
    "Bread", "Cause", "Clean", "Cross",
    "Break", "Chain", "Clear", "Crowd",
    "Breed", "Chair", "Click", "Crown",
    "Brief", "Chart", "Clock", "Curve",
    "Bring", "Chase", "Close", "Cycle",
    "Broad", "Cheap", "Coach", "Daily",
    "Broke", "Check", "Coast", "Dance",
    "Brown", "Chest", "Could", "Dated",
    "Build", "Chief", "Count", "Dealt",
    "Built", "Child", "Court", "Death",
    "Debut", "Entry", "Forth", "Group",
    "Delay", "Equal", "Forty", "Grown",
    "Depth", "Error", "Forum", "Guard",
    "Doing", "Event", "Found", "Guess",
    "Doubt", "Every", "Frame", "Guest",
    "Dozen", "Exact", "Frank", "Guide",
    "Draft", "Exist", "Fraud", "Happy",
    "Drama", "Extra", "Fresh", "Harry",
    "Drawn", "Faith", "Front", "Heart",
    "Dream", "False", "Fruit", "Heavy",
    "Dress", "Fault", "Fully", "Hence",
    "Drill", "Fibre", "Funny", "Night",
    "Drink", "Field", "Giant", "Horse",
    "Drive", "Fifth", "Given", "Hotel",
    "Drove", "Fifty", "Glass", "House",
    "Dying", "Fight", "Globe", "Human",
    "Eager", "Final", "Going", "Ideal",
    "Early", "First", "Grace", "Image",
    "Earth", "Fixed", "Grade", "Index",
    "Eight", "Flash", "Grand", "Inner",
    "Elite", "Fleet", "Grant", "Input",
    "Empty", "Floor", "Grass", "Issue",
    "Enemy", "Fluid", "Great", "Irony",
    "Enjoy", "Focus", "Green", "Juice",
    "Enter", "Force", "Gross", "Joint",
    "Judge", "Metal", "Media", "Newly",
    "Known", "Local", "Might", "Noise",
    "Label", "Logic", "Minor", "North",
    "Large", "Loose", "Minus", "Noted",
    "Laser", "Lower", "Mixed", "Novel",
    "Later", "Lucky", "Model", "Nurse",
    "Laugh", "Lunch", "Money", "Occur",
    "Layer", "Lying", "Month", "Ocean",
    "Learn", "Magic", "Moral", "Offer",
    "Lease", "Major", "Motor", "Often",
    "Least", "Maker", "Mount", "Order",
    "Leave", "March", "Mouse", "Other",
    "Legal", "Music", "Mouth", "Ought",
    "Level", "Match", "Movie", "Paint",
    "Light", "Mayor", "Needs", "Paper",
    "Limit", "Meant", "Never", "Party",
    "Peace", "Power", "Radio", "Round",
    "Panel", "Press", "Raise", "Route",
    "Phase", "Price", "Range", "Royal",
    "Phone", "Pride", "Rapid", "Rural",
    "Photo", "Prime", "Ratio", "Scale",
    "Piece", "Print", "Reach", "Scene",
    "Pilot", "Prior", "Ready", "Scope",
    "Pitch", "Prize", "Refer", "Score",
    "Place", "Proof", "Right", "Sense",
    "Plain", "Proud", "Rival", "Serve",
    "Plane", "Prove", "River", "Seven",
    "Plant", "Queen", "Quick", "Shall",
    "Plate", "Sixth", "Stand", "Shape",
    "Point", "Quiet", "Roman", "Share",
    "Pound", "Quite", "Rough", "Sharp",
    "Sheet", "Spare", "Style", "Times",
    "Shelf", "Speak", "Sugar", "Tired",
    "Shell", "Speed", "Suite", "Title",
    "Shift", "Spend", "Super", "Today",
    "Shirt", "Spent", "Sweet", "Topic",
    "Shock", "Split", "Table", "Total",
    "Shoot", "Spoke", "Taken", "Touch",
    "Short", "Sport", "Taste", "Tough",
    "Shown", "Staff", "Taxes", "Tower",
    "Sight", "Stage", "Teach", "Track",
    "Since", "Stake", "Teeth", "Trade",
    "Sixty", "Start", "Texas", "Treat",
    "Sized", "State", "Thank", "Trend",
    "Skill", "Steam", "Theft", "Trial",
    "Sleep", "Steel", "Their", "Tried",
    "Slide", "Stick", "Theme", "Tries",
    "Small", "Still", "There", "Truck",
    "Smart", "Stock", "These", "Truly",
    "Smile", "Stone", "Thick", "Trust",
    "Smith", "Stood", "Thing", "Truth",
    "Smoke", "Store", "Think", "Twice",
    "Solid", "Storm", "Third", "Under",
    "Solve", "Story", "Those", "Undue",
    "Sorry", "Strip", "Three", "Union",
    "Sound", "Stuck", "Threw", "Unity",
    "South", "Study", "Throw", "Until",
    "Space", "Stuff", "Tight", "Upper",
    "Upset", "Whole", "Waste", "Wound",
    "Urban", "Whose", "Watch", "Write",
    "Usage", "Woman", "Water", "Wrong",
    "Usual", "Train", "Wheel", "Wrote",
    "Valid", "World", "Where", "Yield",
    "Value", "Worry", "Which", "Young",
    "Video", "Worse", "While", "Youth",
    "Virus", "Worst", "White", "Worth",
    "Visit", "Would", "Vital", "Voice"
]
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
    if (inputWord.lower() == word.lower()):
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
print("The correct word was: " + word.upper())
if gameOver == True:
    print("You solved in " + str(guessNum + 1) + " guesses")