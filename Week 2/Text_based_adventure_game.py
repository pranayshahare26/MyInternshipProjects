import time

class Player:
    def __init__(self):
        self.inventory = []
        self.progress = []

def show_intro():
    print("Welcome to the Mysterious Island Adventure!")
    print("You're on an island full of secrets, searching for a powerful artifact.")
    print("Let the journey begin!\n")

def show_choices(options):
    print("What will you do?")
    for i, (key, value) in enumerate(options.items(), 1):
        print(f"{i}. {value}")

def get_choice(options):
    show_choices(options)
    choice = input("Enter your choice: ")
    while choice not in options:
        print("Invalid choice. Please enter a valid number.")
        choice = input("Enter your choice: ")
    return choice

def explore_cave(player):
    print("\nYou enter a dark cave...")
    time.sleep(1)
    print("Inside, you find a glowing crystal.")
    time.sleep(1)
    choices = {"1": "Take the crystal", "2": "Leave the cave"}
    user_choice = get_choice(choices)

    if user_choice == "1":
        print("\nCongratulations! You obtained the magical crystal.")
        player.inventory.append("Magical Crystal")
    else:
        print("\nYou decide to leave the cave empty-handed.")

def encounter_friendly_creature(player):
    print("\nYou meet a friendly creature that guides you to the artifact.")
    player.progress.append("Artifact Found")

def lose_your_way(player):
    print("\nYou lose your way and must retrace your steps.")

def talk_to_guide(player):
    print("\nThe guide offers advice...")
    time.sleep(1)
    print("He warns of a tricky forest ahead, guarded by ancient magic.")
    time.sleep(1)
    choices = {"1": "Enter the forest", "2": "Ask for more information"}
    user_choice = get_choice(choices)

    if user_choice == "1":
        print("\nYou venture into the forest...")
        time.sleep(1)
        forest_choices = {"1": "Meet a friendly creature", "2": "Lose your way"}
        forest_choice = get_choice(forest_choices)

        if forest_choice == "1":
            encounter_friendly_creature(player)
        else:
            lose_your_way(player)
    else:
        print("\nThe guide shares more information...")
        time.sleep(1)

def reset_progress(player):
    player.inventory = []
    player.progress = []
    print("\nThe island's whispers bring you back to the start...")

def show_ending(player):
    if "Artifact Found" in player.progress:
        print("\nThe artifact's power hums within you. You've reshaped destiny!")
        print("But whispers of another challenge linger on the wind...\n")
    elif len(player.inventory) >= 3:
        print("\nThe island's secrets overwhelm you. Your quest remains unfinished.")
        print("Will you try again, adventurer?\n")
    else:
        print("\nYour journey continues, filled with promise and peril.")
        print("The island awaits, its secrets ready to be unveiled...\n")

def show_end_message():
    print("Thank you for playing the Mysterious Island Adventure!")
    print("We hope you enjoyed the journey. Until next time!")

def main():
    player = Player()
    show_intro()

    while True:
        print("\nInventory:", player.inventory)
        print("Progress:", player.progress)

        choices = {"1": "Explore the cave", "2": "Talk to the guide", "3": "Start over", "4": "Quit"}
        user_choice = get_choice(choices)

        if user_choice == "1":
            explore_cave(player)
        elif user_choice == "2":
            talk_to_guide(player)
        elif user_choice == "3":
            reset_progress(player)
        elif user_choice == "4":
            break

        # Check for game-ending conditions
        show_ending(player)

    show_end_message()

if __name__ == "__main__":
    main()
