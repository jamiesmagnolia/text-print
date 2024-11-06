class Room:
    """
    Room class.

    Room object:
    An area containing other game objects and actors that the Player
    can interact with. A "room" does not necessarily have to mean
    "an indoor room" and instead means a fixed-sized general area that
    the Player can explore.
    """

    def __init__(self, name="Unknown", desc="An unexplored room."):
        """
        Create a Room object.
        :param name: The name of the room.
        :param desc: The description of the room.
        """
        self.name = name
        self.desc = desc + "\n"
        self.exits = []
        self.items = []

    def __str__(self):
        return self.name

    def __repr__(self):
        result = f"Room: ('{self.name}')\nDescription: ('{self.desc}')\nExits: ('{self.exits}')"

    def add_exit(self, new_exit):
        """Add a single exit"""
        self.exits.append(new_exit)

    def add_exits(self, new_exits):
        """Add a list of exits to the room's current exits"""
        self.exits.extend(new_exits)
