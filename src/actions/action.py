from abc import ABC, abstractmethod


class Action(ABC):
    """
    Action abstract base class.
    """

    @abstractmethod
    def execute(self):
        pass
