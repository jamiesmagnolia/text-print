import os

from room import Room

# Pre-game

# Room initialisation
room1 = Room("Bedroom", "There's a single bed pushed against the corner.")
room2 = Room("Living Room", "Ignoring the single worn out couch, it looks quite barren.")
room3 = Room("Kitchen", "Slightly more homey compared to the rest of the rooms")
room4 = Room("Backyard", "Nothing but grass and a single mango tree.")

# Connecting rooms to each other
room1.add_exit(room2)
room2.add_exits([room1, room3, room4])
room3.add_exit(room2)
room4.add_exit(room2)


# Util functions
def clear_screen():
    # Clear command for Windows vs Unix-based systems (Linux, macOS)
    os.system('cls' if os.name == 'nt' else 'clear')


# Game loop starts
def game_loop():
    # Starting room
    current_room = room1
    while True:
        # Start every choice with a cleared terminal
        clear_screen()

        print(f"\nYou're in {current_room}.")
        print(current_room.desc)
        print("\nWhere would you like to go?")

        # Display navigation options
        for i, room, in enumerate(current_room.exits, 1):
            print(f"{i}. Go to {room}")

        # Getting player input
        choice = input("Select option (or 'q' to quit/exit): ")

        # Handle player input
        if choice.isdigit():
            choice = int(choice) - 1
            if 0 <= choice < len(current_room.exits):
                current_room = current_room.exits[choice]
            else:
                print("That's not a valid option.")
        elif choice == 'q':
            print("Thanks for playing!")
            break
        else:
            print("That's not a valid option.")


# Start game
game_loop()
