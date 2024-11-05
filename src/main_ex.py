# import os
#
#
# # Function to clear the terminal screen
# def clear_screen():
#     if os.name == 'nt':  # For Windows
#         os.system('cls')
#     else:  # For macOS and Linux
#         os.system('clear')
#
#
# # Room class definition
# class Room:
#     DIRECTIONS = {1: "north", 2: "east", 3: "south", 4: "west"}  # Numbered directions
#
#     def __init__(self, name, description):
#         self.name = name
#         self.description = description
#         self.exits = {}  # Dictionary to hold exits with numbered keys
#
#     def connect(self, number, other_room):
#         self.exits[number] = other_room
#
#     def display(self):
#         clear_screen()  # Clear screen each time room is displayed
#         print(f"You are in {self.name}.")
#         print(self.description)
#         print("Exits:")
#         for number, room in self.exits.items():
#             direction = self.DIRECTIONS.get(number, "unknown")
#             print(f" - {number}: {direction}")
#
#
# # Function to handle navigation
# def navigate(current_room):
#     while True:
#         current_room.display()
#         choice = input("Choose an exit by number: ").strip()
#
#         if choice.isdigit():
#             choice = int(choice)
#             if choice in current_room.exits:
#                 current_room = current_room.exits[choice]
#             else:
#                 print("Invalid choice. Try again.")
#         else:
#             print("Please enter a number.")
#
#
# # Define rooms and connections
# lobby = Room("Lobby", "A large, quiet lobby with echoing footsteps.")
# hallway = Room("Hallway", "A long, narrow corridor with flickering lights.")
# office = Room("Office", "A small, cluttered office filled with papers.")
# basement = Room("Basement", "A dark, musty basement with cobwebs.")
#
# # Connect rooms
# lobby.connect(1, hallway)  # 1 corresponds to "north"
# hallway.connect(3, lobby)  # 3 corresponds to "south"
# hallway.connect(2, office)  # 2 corresponds to "east"
# lobby.connect(4, basement)  # Adds a fourth exit to the basement
#
# # Start game
# navigate(lobby)
