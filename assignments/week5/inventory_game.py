# Assignment 5 - due 12.05.2025
# This is a mini game that lets the user collect fruit and interact with it to make a smoothie

# --- Game State ---]
import random

inventory = []
items_in_room = [
    {"name": "mango", "type": "fruit", "emoji": "🥭"},
    {"name": "pineapple", "type": "fruit", "emoji": "🍍"},
    {"name": "strawberry", "type": "fruit", "emoji": "🍓"},
    {"name": "kiwi", "type": "fruit", "emoji": "🥝"},
    {"name": "peach", "type": "fruit", "emoji": "🍑"},
    {"name": "banana", "type": "fruit", "emoji": "🍌"},
    {"name": "watermelon", "type": "fruit", "emoji": "🍉"},
    {"name": "cherry", "type": "fruit", "emoji": "🍒"},

    {"name": "milk", "type": "liquid", "emoji": "🥛"},
    {"name": "water", "type": "liquid", "emoji": "🚰"},

    {"name": "sugar", "type": "sweetener", "emoji": "🍚"},
    {"name": "honey", "type": "sweetener", "emoji": "🍯"}
] # length shall be larger than max inventory size if there is only one room
MAX_INVENTORY_SIZE = 5
ROTTEN_INGREDIENT = False

# --- Functions ---

def show_inventory():
    # list all names of items in the inventory, consider the case when the list is empty
    if len(inventory) == 0:
        print("Your inventory is empty! Go find some items first and check back later :D")
    else:
        for items in inventory:
            print(items)

def show_room_items():
    # list all items in current room
    for i in range(len(items_in_room)):
        current_item_emoji = items_in_room[i]["emoji"]
        current_item = items_in_room[i]["name"]
        print(f"{current_item_emoji} - {current_item}")

def pick_up(item_name):
    # pick up an item from the room if inventory limit is not met yet
    if len(inventory) == MAX_INVENTORY_SIZE:
        print("Your inventory is full! You can discard an item if you want.")
    else:
        inventory.append(item_name)
        print(f"{item_name} added to inventory.")
        print(f"You have {MAX_INVENTORY_SIZE - len(inventory)} space(s) left.")

def discard(item_name:str):
    # drop an item from your inventory, at the same time append it back to the list of items for the room
    if len(inventory) == 0:
        print("Your inventory is empty! There is nothing to discard")
    else:
        inventory.remove(item_name)
        print(f"{item_name} removed from inventory.")

def use(item_name):
    # Ex: use the item differently depends on the type
    for i in range(len(items_in_room)):
        if items_in_room[i]["type"] == "fruit" and items_in_room[i]["name"] == item_name:
            print(f"You ate the {item_name}! You may add another fruit to your inventory.")
            inventory.remove(item_name)
        elif items_in_room[i]["type"] == "liquid" and items_in_room[i]["name"] == item_name:
            print(f"You drank the {item_name}! You should add another liquid to your inventory.")
            inventory.remove(item_name)
        elif items_in_room[i]["type"] == "sweetener" and items_in_room[i]["name"] == item_name:
            print(f"I can't believe you ate that {item_name} like that, you should get some more...")
            inventory.remove(item_name)

def examine(item_name):
    # you can only examine an item if it's in your inventory
    if item_name in inventory:
        ROTTEN_INGREDIENT = determine_fruit_freshness()
        for i in range(len(items_in_room)):
            if items_in_room[i]["type"] == "fruit" and items_in_room[i]["name"] == item_name:
                if ROTTEN_INGREDIENT:
                    print(f"Oh no! The {item_name} is rotten, you should discard it and get a new fruit")
                else:
                    print(f"This {item_name} is perfectly ripe!")
            else:
                if items_in_room[i]["type"] == "liquid" and items_in_room[i]["name"] == item_name:
                    print(f"This {item_name} looks good!")
                elif items_in_room[i]["type"] == "sweetener" and items_in_room[i]["name"] == item_name:
                    print(f"This {item_name} looks good!")
    else:
        print("The item you are trying to examine is not in your inventory!")

def determine_fruit_freshness():
    freshness = ("fresh", "rotten")
    fruit_freshness = random.choice(freshness)
    if fruit_freshness == "fresh":
        return True
    else:
        return False

def blend():
    smoothie = []
    for x in range(len(inventory)):
        for y in range(len(items_in_room)):
            if items_in_room[y]["name"] == inventory[x]:
                smoothie += items_in_room[y]["emoji"]
    print("Your smoothie has: ", end=" ")
    for i in smoothie:
        print(i, end=" ")

# --- Game Loop ---

def game_loop():
    print("Welcome to the Smoothie Bar!")
    print("Type 'help' for a list of commands.")

    while True:
        command = input("\n> ").strip().lower()
        if command == "help":
            # You can also rename the commands according to your own needs
            print("Commands: inventory, look, pickup [item], discard [item], use [item], examine [item], make smoothie, quit")
        elif command == "inventory":
            show_inventory()
        elif command == "look":
            show_room_items()
        elif command.startswith("pickup "):
            item_name = command[7:]
            pick_up(item_name)
        elif command.startswith("discard "):
            item_name = command[8:]
            discard(item_name)
        elif command.startswith("use "):
            item_name = command[4:]
            use(item_name)
        elif command.startswith("examine "):
            item_name = command[8:]
            examine(item_name)
        elif command == "make smoothie":
            blend()
            break
        elif command == "quit":
            print("Thanks for playing!")
            break
        else:
            print("Unknown command. Type 'help' to see available commands.")

if __name__ == "__main__":
    game_loop()

