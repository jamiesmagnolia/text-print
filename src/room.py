class Room:

    def __init__(self, name, desc):
        """
        Constructor.
        :param name: The name of the room.
        """
        self.name = name
        self.desc = desc
        self.exits = {}


