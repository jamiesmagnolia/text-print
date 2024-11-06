from __future__ import annotations

from actions.action import Action
from player import Player
from room import Room


class MoveAction(Action):
    """
    Move Action class.

    Move Action is used/executed when the Player tries to navigate across all the
    different available rooms at that current room.
    """

    def __init__(self, target_room: 'Room'):
        self.target_room = target_room

    def execute(self, player: 'Player'):
        """
        Navigate to the target room.
        """
        pass
        #
        # from game import Game
        # game.current_room = self.target_room
        # return self.menu_desc(player)

    def menu_desc(self, actor) -> str:
        return f"{actor} heads towards {self.target_room.name}."
