from __future__ import annotations

from abc import ABC, abstractmethod

from player import Player


class Action(ABC):
    """
    Action abstract base class.
    """

    @abstractmethod
    def execute(self, player: Player, game) -> None:  # TODO: return string desc of action execution?
        """
        Executes the action.
        :param player: The player to execute the action.
        :param game: The game to play on.
        :return:
        """
        pass
