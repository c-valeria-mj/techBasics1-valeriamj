# Assignment 3 - due 28.04.25
# ASCII art with user input (3 user inputs - 1 str and 2 int, 1 nested loop & 1 conditional statement, use random & list)

defaultBunny = [ # this list holds the template of the bunny that the user can costumize
    "|￣￣￣￣￣￣￣￣￣￣￣|",
    "       ( your ) ",
    "    ( text here ) ",
    "|＿＿＿＿＿＿＿＿＿＿＿| ",
    "       o ",
    "      ° ",
    "(\__/) ",
    "( o.o) ",
    "/ > (ur icon here)"
]

iconOptions = { # this dictionary holds the icons the user can choose for their bunny to hold
    "1) Heart" : "♡",
    "2) Star" : "★",
    "3) Music Note" : "𝄞",
    "4) Smiley" : "☺︎",
    "5) Umbrella" : "☂︎",
    "6) Sun" : "☀︎",
    "7) Moon" : "☾"
}

faceOptions = { # this dictionary holds the face expressions they can choose for their bunny
    "1) Happy" : "*(^o^)*",
    "2) Sad" : "(._.)",
    "3) Surprised" : "(*O*)",
    "4) Angry" : "(>_<)",
    "5) Loving" : "(♡.♡)",
    "6) Sleepy" : "(9_9)",
}

def printASCII(asciiArt): # iterates over an array holding ascii art and prints each line
    for i in asciiArt:
        print(i)

'''
    Program starts here!
'''
print("Welcome! This program allows you to print your own ASCII art like this:\n")
printASCII(defaultBunny)
# clearScreen
for x, y in iconOptions.items(): # iterate over dictionary to show user the icon options
    print(f"{x} - {y}")
print("First, choose the icon you want your bunny to hold from the options above: ")
#clearScreen
for x, y in faceOptions.items(): # iterate over dictionary to show user the face options
    print(f"{x} - {y}")
print("First, choose the face you want for your bunny from the options above: ")
