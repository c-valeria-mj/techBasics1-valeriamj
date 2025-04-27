# Assignment 3 - due 28.04.25
# ASCII art with user input (3 user inputs - 1 str and 2 int, 1 nested loop & 1 conditional statement, use random & list)

# import libraries we need for our program here
import time,os,sys,random,copy

defaultBunny = [ # this list holds the template of the bunny that the user can customize
    "+--------------------+",
    "|   your text here   |",
    "+--------------------+",
    "    o ",
    "   ° ",
    "(\__/) ",
    "( o.o) ",
    "/ > (your icon here)"
]

bunnyEyesClosed = [] # this list holds the user's custom bunny but with its eyes closed

emptyBunny = [ # this list holds an empty template to which we add the user's customizations
    "",
    "",
    "",
    "    o ",
    "   ° ",
    "(\__/) ",
    "",
    ""
]

iconOptions = [ # this list holds the icons the user can choose for their bunny to hold
    ["1) Heart: ",  "♡"],
    ["2) Star: ", "★"],
    ["3) Music Note: ", "𝄞"],
    ["4) Smiley: ","☺︎"],
    ["5) Umbrella: ", "☂︎"],
    ["6) Sun: ", "☀︎"],
    ["7) Moon: ", "☾"],
    ["8) Random"]
]

faceOptions = [ # this list holds the face expressions they can choose for their bunny
    ["1) Happy: ", "( ^o^)"],
    ["2) Sad: ", "( ._.)"],
    ["3) Surprised: ", "( *O*)"],
    ["4) Angry: ", "( >_<)"],
    ["5) Loving: ", "( ♡.♡)"],
    ["6) Sleepy: ", "( 9_9)"],
    ["7) Incredulous: ", "( o_O)"],
    ["8) Random"]
]

def printASCII(asciiArt): # iterates over an array holding ascii art and prints each line
    for i in asciiArt:
        print(i)

def typingPrint(text):  # prints text character by character for a cool effect
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)

def waitAndClearScreen(seconds): # waits an amount of seconds and then clears the screen
    typingPrint("\nLoading")
    for i in range(seconds):
        typingPrint(".")
        time.sleep(1)
    os.system("clear")

'''
    Program starts here!
'''
os.system("clear")
print("Welcome! This program allows you to print your own ASCII art like this:\n")
printASCII(defaultBunny)
waitAndClearScreen(3)
for row in iconOptions: # iterate over list to show user the icon options
    for element in row:
        print(element, end=" ")
    print()
print("\nFirst, choose the icon you want your bunny to hold from the options above.")
while True: # get user to pick the icon for their bunny to hold & validate that input
    try:
        userIconChoice = int(input("Select a character by typing the corresponding number: "))
        if int(userIconChoice) < 1 or int(userIconChoice) > len(iconOptions):
            print("Invalid option!")
        else:
            break
    except ValueError:
        print("Invalid input!")
if userIconChoice == 8:
    userIconChoice = random.randrange(1, 7)
list = iconOptions[userIconChoice - 1]
userIcon = list[-1]
waitAndClearScreen(3)
for row in faceOptions: # iterate over list to show user the face options
    for element in row:
        print(element, end=" ")
    print()
print("\nNext, choose the face you want for your bunny from the options above: ")
while True: # get user to pick the face of their bunny & validate that input
    try:
        userFaceChoice = int(input("Select a character by typing the corresponding number: "))
        if int(userFaceChoice) < 1 or int(userFaceChoice) > len(faceOptions):
            print("Invalid option!")
        else:
            break
    except ValueError:
        print("Invalid input!")
if userFaceChoice == 8:
    userFaceChoice = random.randrange(1, 7)
list = faceOptions[userFaceChoice - 1]
userFace = list[-1]
waitAndClearScreen(3)
while True:
    userText = input("Last but not least, type the message you want the bunny to say: ")
    if len(userText) > 75:
        print("Your message is too long! Please type something shorter, thank you :D")
    else:
        break

''' TEST
userText = "Hello this is a super cool test!"
userFace = "( 9_9)"
userIcon = "♡"
'''
necessaryDashes = ""
userLength = len(userText)
for x in range(len(defaultBunny)): # this loop iterates the emptyBunny list and adds the user's custom choices for printing
    if x == 0:
        for y in range(userLength + 2):
            necessaryDashes += "-"
        emptyBunny[0] = "+" + necessaryDashes + "+"
    elif x == 1:
        emptyBunny[1] = "| " + userText + " |"
    elif x == 2:
        emptyBunny[2] = "+" + necessaryDashes + "+"
    elif x == 6:
        emptyBunny[6] = userFace
    elif x == 7:
        emptyBunny[7] = "/  > " + userIcon

bunnyEyesClosed = copy.deepcopy(emptyBunny)
bunnyEyesClosed[6] = "( -.-)"

os.system("clear")
for i in range(5):
    printASCII(emptyBunny)
    time.sleep(1)
    os.system("clear")
    printASCII(bunnyEyesClosed)
    time.sleep(1)
    os.system("clear")