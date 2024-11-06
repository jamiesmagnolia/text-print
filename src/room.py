from __future__ import annotations

from player import Player


class Room:
    """
    Room class.

    Room object:
    An area containing other game objects and actors that the Player
    can interact with. A "room" does not necessarily have to mean
    "an indoor room" and instead means a fixed-sized general area that
    the Player can explore.
    """

    def __init__(self, name: str = "Unknown", desc: str = "An unexplored room."):
        """
        Create a Room object.
        :param name: The name of the room.
        :param desc: The description of the room.

        Attributes:
        name: The name of the room.
        desc: The description of the room.
        exits: The exits of the room (which room the player can navigate to next).
        items: Player Inventory list / A list of items the Player currently holds.
        """
        self.name = name
        self.desc = desc + "\n"
        self.exits = []
        self.items = []

    def __str__(self) -> str:
        return self.name

    def __repr__(self):
        return f"Room: ('{self.name}')\nDescription: ('{self.desc}')\nExits: ('{self.exits}')"

    def move_player(self, player: Player):
        pass

    def add_exit(self, new_exit: Room) -> None:
        """Add a single exit to the room's current exits"""
        self.exits.append(new_exit)

    def add_exits(self, new_exits: list[Room]) -> None:
        """Add a list of exits to the room's current exits"""
        self.exits.extend(new_exits)
