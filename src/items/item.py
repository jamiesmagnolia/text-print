from __future__ import annotations

from abc import ABC


class Item(ABC):
    def __init__(self, name, desc, durability=1000, portable=True):
        self.name = name
        self.desc = desc
        self.durability = durability
        self.portable = portable

    def __str__(self):
        return self.name

    def __repr__(self):
        return f'<Item: {self.name}\nDesc: {self.desc}>'
