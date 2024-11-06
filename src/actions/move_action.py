from __future__ import annotations

from actions.action import Action
from room import Room


class MoveAction(Action):
    """
    Move Action class.

    Move Action is used/executed when the Player tries to navigate across all the
    different available rooms at that current room.
    """

    def __init__(self, target_room: Room):
        self.target_room = target_room

    def execute(self, player, game):
        game.current_room = self.target_room
