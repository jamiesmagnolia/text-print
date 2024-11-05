class Room:
    num_exits = 0

    def __init__(self, name: str):
        self.name = name
        self.exits = {}

    def connect(self, next_room):
        """

        :type next_room: object
        """
        Room.num_exits += 1
        self.exits[Room.num_exits] = next_room
