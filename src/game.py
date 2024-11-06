from __future__ import annotations

from actions.move_action import MoveAction
from player import Player
from room import Room
from utility import clear_screen


class Game:
    """
    Game class.
    """

    def __init__(self, player: Player, rooms: list[Room]):
        self.player = player
        self.rooms = rooms
        self.current_room = rooms[0]

    def run(self) -> None:
        while True:
            clear_screen()
            print(f"\nYou're in {self.current_room}.")
            print(self.current_room.desc)

            # Player stats
            self.player.display_stats()

            # Available actions: Move to next room
            actions = [
                MoveAction(target_room) for target_room in self.current_room.exits
            ]

            print("\nWhat will you do next?")
            # Display navigation options
            for i, room, in enumerate(self.current_room.exits, 1):
                print(f"{i}. Go to {room}")

            # Getting player input
            choice = input("Select option (or 'q' to quit/exit): ")

            # Handle player input
            if choice.isdigit():
                choice = int(choice) - 1

                # Use Action execution
                if 0 <= choice < len(self.current_room.exits):
                    actions[int(choice)].execute(self.player, self)
                    # self.current_room = self.current_room.exits[choice]
                else:
                    print("That's not a valid option.")
            elif choice == 'q':  # End game
                print("Thanks for playing!")
                break
            else:
                print("That's not a valid option.")
