# Assignment 2 - due 21.04.2025
# This is a mini Dungeons and Dragons game inspired by Stardew Valley's mini-game: Solarion Chronicles

# Import libraries needed
import time,os,sys

# These are the functions we will need to run our game
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

def waitAndClearScreen(seconds): # waits an amount of seconds and then clears the screen
    typingPrint("\nLoading")
    for i in range(seconds):
        typingPrint(".")
        time.sleep(1)
    clearScreen()

def printASCII(asciiArt): # iterates over an array holding ascii art and prints each line
    for i in asciiArt:
        print(i)

# this dictionay hold the different character options the user can play as
chacracterOptions = {
    "1) Warrior 🥷" : " - I like a direct approach.\n",
    "2) Healer 🧝‍♀️" : " - I prefer to help others.\n",
    "3) Wizard 🧙‍" : " - A sharp mind is the most powerful blade of all."
}

# these arrays hold the ascii art for the game
'''
    ASCII art from https://www.asciiart.eu
'''
title = [
    " _____ _            ____                       _          __  ",
    "|_   _| |__   ___  / ___|_      _____  _ __ __| |   ___  / _|",
    "  | | | '_ \ / _ \ \___ \ \ /\ / / _ \| '__/ _` |  / _ \| |_",
    "  | | | | | |  __/  ___) \ V  V / (_) | | | (_| | | (_) |  _|",
    "  |_| |_| |_|\___|_|____/ \_/\_/ \___/|_|  \__,_|  \___/|_|",
    "              |  _ \  ___  ___| |_(_)_ __  _   _",
    "              | | | |/ _ \/ __| __| | '_ \| | | |",
    "              | |_| |  __/\__ \ |_| | | | | |_| |",
    "              |____/ \___||___/\__|_|_| |_|\__, |",
    "                                           |___/ "
]
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
mountains = [
    "           _    .  ,   .           .",
    "       *  / \_ *  / \_      _  *        *   /\'__        *",
    "         /    \  /    \,   ((        .    _/  /  \  *'.",
    "    .   /\/\  /\/ :' __ \_  `          _^/  ^/    `--.",
    "       /    \/  \  _/  \-'\      *    /.' ^_   \_   .'\  *",
    "     /\  .-   `. \/     \ /==~=-=~=-=-;.  _/ \ -. `_/   \ ",
    "    /  `-.__ ^   / .-'.--\ =-=~_=-=~=^/  _ `--./ .-'  `-",
    "   /       `.  / /       `.~-^=-=~=^=.-'      '-._ `._"
]
tower = [
    "                                               |>>>",
    "                                               |",
    "                                           _  _|_  _",
    "                                           |;|_|;|_|;|",
    "                                           \ .    .  / ",
    "                                            \ :  .  / ",
    "                                             ||:   |",
    "                                             ||:.  |",
    "                                             ||:  .|",
    "                                             ||:   |       \,/ ",
    "                                             ||: , |            /` \ ",
    "                                             ||:   |",
    "                                             ||: . |",
    "              __                            _||_   |",
    "     ____--`~    '--~~__            __ ----~    ~`---,              ___",
    "-~--~                   ~---__ ,--~'                  ~~----_____-~'   `~----~~"
]
monster = [
    "                \||/",
    "                |  @___oo",
    "      /\  /\   / (__,,,,|",
    "     ) /^\) ^\/ _)",
    "     )   /^\/   _)",
    "     )   _ /  / _)",
    " /\  )/\/ ||  | )_)",
    "<  >      |(,,) )__)",
    " ||      /    \)___)\ ",
    " | \____(      )___) )___",
    "  \______(_______;;; __;;;"
]
mage = [
    "                  .",
    "                   .",
    "         /^\     .",
    '    /\   "V"',
    "   /__\   I      O  o",
    "  / .. \  I     .",
    "  \].`[/  I",
    "  /l\/j\  (]    .  O",
    " /. ~~ ,\/I          .",
    " \ L__j^\/I       o",
    "  \/--v}  I     o   .",
    "  |    |  I   _________",
    "  |    |  I c(`       ')o",
    "  |    l  I   \.     ,/",
    "_/j  L l\_!  _//^---^\ \_"
]

"""
    This is where the game starts 
"""

# print welcome message for the user
clearScreen()
printASCII(title)
typingPrint("Welcome Adventurer! \n"
            "Your party is about to head out on an exciting quest to find The Sword of Destiny.\n")

# have the user pick their class (wizard, healer or warrior)
typingPrint("Before you set out on your quest you must first decide what you want to be:\n")
typingPrint("[Please select one of the following characters by typing the corresponding number]\n")
for x, y in chacracterOptions.items():
    print(x)
    print(y)

while True:
    try:
        playerChoice = int(typingInput("\nSelect a character by typing 1, 2 or 3: "))
        if int(playerChoice) != 1 and playerChoice != 2 and playerChoice != 3:
            typingPrint("Invalid option! \n")
        else:
            break
    except ValueError:
        typingPrint("Invalid input! \n")

waitAndClearScreen(3)

# print text explaining the quest to the user

time.sleep(1)
printASCII(castle)

typingPrint("\nThe king of these lands has entrusted you and your companions with recovering The Sword of Destiny.\n"
            "A daunting task that promises not only fame and glory but a sizeable reward in gold and silver.\n")

waitAndClearScreen(3)

printASCII(mountains)

typingPrint("\nAfter a long month of journeying across unforgiving lands you stop atop a mountain. \n"
            "Looming in the distance, you can finally see your destination. \n"
            "A tower, dark and imposing that radiates danger and evilness. \n"
            "You continue on, knowing that obtaining The Sword of Destiny will not come easy. \n")
waitAndClearScreen(3)

# have the user pick whether to go in front of the party or the back
printASCII(tower)

typingPrint("\nAt last! You reach your destination, the tower that is home to the evil mage that stole The Sword of Destiny.\n"
            "Ahead lie many dangers to you and your companions.\n"
            "Standing at the entrance to the tower do you...\n"
            "   Go in the front. Fortune favors the bold.\n"
            "   Search for a back entrance. It's better to remain hidden.\n"
            )
while True:
    entranceChoice = typingInput("Type 'front' or 'back' to choose: ")
    if entranceChoice.lower() != 'front' and entranceChoice.lower() != 'back':
        # print(entranceChoice)
        typingPrint("Invalid option! Please type a valid option.\n")
    else:
        break

waitAndClearScreen(3)

if entranceChoice == 'front':
    printASCII(monster)
    typingPrint("\nA monster is guarding the hallway, blocking your path!\n"
                "Do you...\n"
                "   Fight the monster.\n"
                "   Run away.\n")
    while True:
        monsterChoice = typingInput("Type 'fight' or 'run' to choose: ")
        if monsterChoice.lower() != 'fight' and monsterChoice.lower()!= 'run':
            typingPrint("Invalid option! Please type a valid option.\n")
        else:
            break
    if monsterChoice.lower() == 'fight':
        typingPrint("The monster lunges at you with unnatural speed!\n"
                    "Do you...\n"
                    "   Raise your shield.\n"
                    "   Swing your weapon.\n")
        while True:
            fightChoice = typingInput("Type 'shield' or 'weapon' to choose: ")
            if fightChoice.lower() != 'shield' and fightChoice.lower() != 'weapon':

                typingPrint("Invalid option! Please type a valid option.\n")
            else:
                break
        if monsterChoice.lower() == 'weapon':
            typingPrint("The monster is too quick! While you raise your weapon it attacks.\n"
                        "You're sent flying back with the force of their attack.\n"
                        "One of your companions holds it back, while you and the rest of \n"
                        "the party run away. Deeper into the tower")
            waitAndClearScreen(3)
        else:
            typingPrint("You dodge the monster's attack, allowing your companions to hit it.\n"
                        "It crumbles to dust before you, now you can proceed deeper into the tower.\n")
            waitAndClearScreen(3)
    else:
        typingPrint("You ran away! Returning in shame and empty handed to the king. Will you try again?\n")
        os.abort()

# this is the endgame
printASCII(mage)
typingPrint("\nYou make your way to a long hallway with a single door at the end of it.\n"
            "You know beyond it is the mage who stole The Sword of Destiny.\n"
            "It is time to face your destiny.\n")
if playerChoice == 1: # ending if player chose warrior
    typingPrint("You stand beside you wizard companion and prepare to attack the evil mage.\n"
                "Do you...\n"
                "   Rush the enemy first, taking advantage of the element of surprise.\n"
                "   Wait for a window of opportunity when to best strike the evil mage.\n")
    while True:
        warriorChoice = typingInput("Type 'rush' or 'wait' to choose: ")
        if warriorChoice.lower() != 'rush' and warriorChoice.lower() != 'wait':
            typingPrint("Invalid option! Please type a valid option.\n")
        else:
            break
    if warriorChoice.lower() == 'wait':
        typingPrint("The wizard in your party casts a spell to paralyze the evil mage.\n"
                    "Allowing you the perfect opportunity to land the killing blow on the evil mage\n"
                    "Your companions and you have succeeded! The Sword of Destiny is once again\n"
                    "in your hands and the world is safe.")
    else:
        typingPrint("The evil mage easily predicts your move and hits you with a powerful spell.\n"
                    "You fall unconscious, and can only hope the healer will help you soon.\n"
                    "After a while you awake to find your companions have defeated the evil mage.\n"
                    "You breathe a sigh of relief, the Sword of Destiny is safe.")
elif playerChoice == 2: # ending if player chose healer
    typingPrint("You stand behind your companions and prepare to attack the evil mage.\n"
                "Without hesitation the evil mage throws a fireball at your party.\n"
                "The warrior and wizard take the brunt of the damage. Both are severely \n"
                "injured in the process.\n"
                "Do you...\n"
                "   Heal the warrior.\n"
                "   Heal the wizard.\n")
    while True:
        healerChoice = typingInput("Type 'warrior' or 'wizard' to choose: ")
        if healerChoice.lower() != 'warrior' and healerChoice.lower() != 'wizard':
            typingPrint("Invalid option! Please type a valid option.\n")
        else:
            break
    if healerChoice.lower() == 'warrior':
        typingPrint("You heal the warrior. They immediately rush at the evil mage and hit them with a sword.\n"
                    "It's not enough the evil mage is still standing. You have to improvise.\n"
                    "You search in your bag for something that might help and stumble upon a vial of\n"
                    "acid. You throw it at the evil mage and hope for the best.\n"
                    "It works! Your companions and you have succeeded, The Sword of Destiny is once again\n"
                    "in your hands and the world is safe.")
    else:
        typingPrint("You heal the wizard. It allows them enough time to throw a fireball of their own at\n"
                    "the evil mage. It does enough damage to defeat the evil mage. \n"
                    "Your companions and you have succeeded! The Sword of Destiny is once again\n"
                    "in your hands and the world is safe.\n")
else: # ending if player chose wizard
    typingPrint("You stand beside your warrior companion and prepare to attack the evil mage.\n"
                "Do you...\n"
                "   Cast a protective spell on your party anticipating the evil mage's next move.\n"
                "   Cast a strong spell at the evil mage and hope it's enough.\n")
    while True:
        wizardChoice = typingInput("Type 'protect' or 'attack' to choose: ")
        if wizardChoice.lower() != 'protect' and wizardChoice.lower() != 'attack':
            typingPrint("Invalid option! Please type a valid option.\n")
        else:
            break
    if wizardChoice.lower() == 'protect':
        typingPrint("As you predicted, the evil mage casts their strongest spell\n"
                    "Protecting your companions allows the warrior to rush the evil mage.\n"
                    "Distracting the enemy for long enough to prepare your next spell and \n"
                    "finish the evil mage once and for all. You and your companions have succeeded!\n"
                    "The Sword of Destiny is once again in your hands and the world is safe.\n")
    else:
        typingPrint("You attack the evil mage but it's not enough. They retaliate by casting a spell at\n"
                    "your healer companion, rendering them unconscious. You rush to protect them, allowing\n"
                    "the warrior to charge at the evil mage and finish the job. You and your companions have\n"
                    "succeeded! The Sword of Destiny is once again in your hands and the world is safe.\n")
