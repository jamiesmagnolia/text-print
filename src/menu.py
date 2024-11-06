from __future__ import annotations

from actions.action import Action


class Menu:
    def __init__(self, actions: list[Action]):
        self.actions = actions

    def display(self) -> None:
        pass
