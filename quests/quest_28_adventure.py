# Quest 28: The Adventure Begins
# A text-based "Choose Your Own Adventure" game with functions for locations
# and at least two different endings

# --- Location / scene functions ---

def start():
    """The starting point of the adventure."""
    print("=== The Adventure Begins ===\n")
    print("You wake up at the edge of a dark forest.")
    print("A sign reads: 'Danger ahead — choose wisely.'\n")
    print("Do you go into the forest or head toward the mountain?")
    choice = input("Type 'forest' or 'mountain': ").strip().lower()

    if choice == "forest":
        forest()
    elif choice == "mountain":
        mountain()
    else:
        print("You stand there, confused, and a wolf eats you. Game over.")

def forest():
    """The forest location — leads to two possible endings."""
    print("\nYou enter the dark forest. Owls hoot above you.")
    print("You find a fork in the path. Left goes to a cave, right to a river.\n")
    choice = input("Type 'left' (cave) or 'right' (river): ").strip().lower()

    if choice == "left":
        cave_ending()
    elif choice == "right":
        river_ending()
    else:
        print("You wander in circles and fall asleep. Nothing happens. Game over.")

def mountain():
    """The mountain location — leads to the victory ending."""
    print("\nYou climb the mountain. The view is breathtaking!")
    print("At the top you find a chest with a golden key.\n")
    choice = input("Do you 'take' the key or 'leave' it? ").strip().lower()

    if choice == "take":
        mountain_victory_ending()
    else:
        print("You leave the key and head home, wondering what it opened. Game over.")

# --- Ending functions ---

def cave_ending():
    """Ending 1: The cave — a bad ending."""
    print("\nYou enter the cave. It's warm… but something growls in the dark.")
    print("A dragon wakes up and roasts you like a marshmallow.")
    print("\n💀 ENDING 1: Crispy Hero. Better luck next time!")

def river_ending():
    """Ending 2: The river — a neutral ending."""
    print("\nYou follow the river downstream and reach a village.")
    print("The villagers welcome you and you live a quiet, peaceful life.")
    print("\n🏡 ENDING 2: The Peaceful Life. Not bad at all!")

def mountain_victory_ending():
    """Ending 3: The mountain victory — the best ending."""
    print("\nThe golden key glows in your hand. You feel unstoppable.")
    print("You descend the mountain, unlock the ancient gate at its base,")
    print("and discover a kingdom that has been waiting for its true ruler — YOU.")
    print("\n👑 ENDING 3: The True King/Queen. You win!")

# --- Run the game ---
start()
