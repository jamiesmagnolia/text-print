from game import Game
from player import Player
from room import Room

# Pre-game

# Player
player = Player("Harker", 1000, 500)

# Room initialisation
room1 = Room("Bedroom", "There's a single bed pushed against the corner.")
room2 = Room("Living Room", "Ignoring the single worn out couch, it looks quite barren.")
room3 = Room("Kitchen", "Slightly more homey compared to the rest of the rooms")
room4 = Room("Backyard", "Nothing but grass and a single mango tree.")

rooms = [room1, room2, room3, room4]

# Connecting rooms to each other
room1.add_exit(room2)
room2.add_exits([room1, room3, room4])
room3.add_exit(room2)
room4.add_exit(room2)

# Create Game
game = Game(player, rooms)

# Start game
game.run()
