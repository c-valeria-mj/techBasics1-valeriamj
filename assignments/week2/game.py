# Assignment 2 - due 21.04.2025
# This is a mini Dungeons and Dragons game inspired by Stardew Valley's mini-game: Solarion Chronicles

# Import libraries needed
import time,os,sys

# These are the fuctions we will need to run our game

def typingPrint(text):  # prints text character by character for a cool effect
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)

def clearScreen(): # clears terminal in-between text output for better user experience
  os.system("clear")

def typingInput(text): # prints input prompt text character by character for a cool effect
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    value = input()
    return value

def checkInt(integerInput): # checks if user input is a valid integer
    while True:
        try:
            userInput = int(input(integerInput))
        except ValueError:
            print("Not a valid input! Please choose a character option (1, 2 or 3) to continue")
            continue
        else:
            return userInput
            break

        # this dictionary holds the text that is displayed to the user and allows them to play the game
gameText = {
    "welcomeText" : "Welcome Adventurer! \nYour party is about to head out on an exciting quest to find th ",
    "decideClass" : "Before you set out on  your quest you must first decide what you want to be",

}

chacracterOptions = {
    "1) Warrior 🥷" : " - I like a direct approach.\n",
    "2) Healer 🧝‍♀️" : " - I prefer to help others.\n",
    "3) Wizard 🧙‍" : " - A sharp mind is the most powerful balde of all.\n"
}

# print welcome message for the user
clearScreen()
typingPrint("Welcome Adventurer! \n")
time.sleep(1)
typingPrint("Your party is about to head out on an exciting quest to find the magical object.\n")
time.sleep(1)
# have the user pick their class (wizard, healer or warrior)
typingPrint("Before you set out on your quest you must first decide what you want to be:\n")
time.sleep(1)
typingPrint("[Please select one of the following characters by typing the corresponding number]\n")
for x, y in chacracterOptions.items():
    print(x)
    print(y)

while True:
    try:
        playerChoice = int(typingInput("\n Select a character by typing 1, 2 or 3: "))
        if int(playerChoice) != 1 and playerChoice != 2 and playerChoice != 3:
            typingPrint("Invalid option!")
        else:
            break
    except ValueError:
        print ("Invalid input!")

time.sleep(5)
clearScreen()

# print text explaining the quest to the user
castle = [
    "                             -|             |-",
    "         -|                  [-_-_-_-_-_-_-_-]                  |-",
    "         [-_-_-_-_-]          |             |          [-_-_-_-_-]",
    "          | o   o |           [  0   0   0  ]           | o   o |",
    "           |     |    -|       |           |       |-    |     |",
    "           |     |_-___-___-___-|         |-___-___-___-_|     |",
    "           |  o  ]              [    0    ]              [  o  |",
    "           |     ]   o   o   o  [ _______ ]  o   o   o   [     | ----__________",
    "_____----- |     ]              [ ||||||| ]              [     |",
    "           |     ]              [ ||||||| ]              [     |",
    "       _-_-|_____]--------------[_|||||||_]--------------[_____|-_-_",
    "      ( (__________------------_____________-------------_________) )"
]
time.sleep(1)
for i in castle:
    print(i)

typingPrint("\nThe king of these land has entrusted you and your companions with recovering \nthe magical object.\n"
            "A daunting task that promises not only fame and glory but a sizeable reward in \ngold and silver.\n")

time.sleep(5)
clearScreen()

mountains = [
"           _    .  ,   .           .",
"       *  / \_ *  / \_      _  *        *   /\'__        *",
"         /    \  /    \,   ((        .    _/  /  \  *'.",
"    .   /\/\  /\/ :' __ \_  `          _^/  ^/    `--.",
"       /    \/  \  _/  \-'\      *    /.' ^_   \_   .'\  *",
"     /\  .-   `. \/     \ /==~=-=~=-=-;.  _/ \ -. `_/   \ ",
"    /  `-.__ ^   / .-'.--\ =-=~_=-=~=^/  _ `--./ .-'  `-",
"   /       `.  / /       `.~-^=-=~=^=.-'      '-._ `._",
]

for i in mountains:
    print(i)

typingPrint("After a long month of journeying across unforgiving lands you stop atop \na mountain. \n"
            "Looming in the distance, you can finally see your destination. \n"
            "A tower, dark and imposing that radiates danger and evilness. \n"
            "You continue on, knowing that obtaining the magical object will not \ncome easy. \n")
time.sleep(5)

# have the user pick whether to go in front of the party or the back

# have the user pick between left or right

    # left is the battle

    # right there is nothing

# battle the bad guy

# print conclusion text
