from __future__ import annotations

from abc import ABC, abstractmethod

from player import Player


class Action(ABC):
    """
    Action abstract base class.
    """

    @abstractmethod
    def execute(self, player: 'Player') -> str:
        """
        Executes the action.
        :param player: The player to execute the action.
        :return: A description of the executed action.
        """
        pass

    @abstractmethod
    def menu_desc(self, actor) -> str:
        """
        Describes the action that could be performed shown on the menu page.
        :param actor:
        :return: A description of the action shown on the menu page.
        """
        pass
