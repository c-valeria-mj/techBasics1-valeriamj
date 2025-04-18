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

def typingInput(text):
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    value = input()
    return value

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
typingPrint("Welcome Adventurer! \n")
time.sleep(1)
typingPrint("Your party is about to head out on an exciting quest to find the magical object.\n")
time.sleep(1)
# have the user pick their class (wizard, healer or warrior)
typingPrint("Before you set out on your quest you must first decide what you want to be:\n")
time.sleep(1)
typingPrint("[Please select one of the following characters by typing the corresponding number]\n")
for x, y in chacracterOptions.items():
    typingPrint(x)
    typingPrint(y)
playerChoice = typingInput("Select a character by typing 1, 2 or 3: ")
clearScreen()

# print text explaining the quest to the user
typingPrint("The king of these land has entrusted you and your companions with recovering the magical object.\n"
            "A daunting task that promises not only fame and glory but a sizeable reward in gold and silver.\n")
# have the user pick whether to go in front of the party or the back

# have the user pick between left or right

    # left is the battle

    # right there is nothing

# battle the bad guy

# print conclusion text
