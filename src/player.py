class Player:

    def __init__(self, name, hp=1000, stamina=1000 // 2):
        self.name = name
        self.hp = hp
        self.stamina = stamina
        self.inventory = []

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"Player\nName: {self.name}\nHP: {self.hp}\nStamina: {self.stamina}\nInventory: {self.inventory}"

    def alive(self) -> bool:
        return self.hp > 0

    def display_stats(self):
        print("Stats: ")
        print("HP: ", self.hp)
        print("Stamina: ", self.stamina)
        print("Inventory:", len(self.inventory))

    def pickup_item(self, new_item):
        self.inventory.append(new_item)

    def drop_item(self, item_index):
        self.inventory.pop(item_index - 1)
