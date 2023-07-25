class Player:
    def __init__(self):
        self.character = None
        self.username = None
        self.race = None
        self.hp = None
        self.start_hp = None
        self.weapon = None
        self.damage = 0
        self.magic = None
        self.armour = None
        self.defend = 0
        self.potions = 0
        self.start_pot = 0
        self.items = {
            "bangle": None,
            "brew": None,
            "halo": None,
            "key": None,
            "sharpstone": None,
        }

    def deal_damage(self):
        return self.damage

    def take_damage(self, opponent_damage):
        self.hp = self.hp - opponent_damage
        return self.hp

    def heal(self):
        self.hp = self.start_hp
        return self.hp


class Human(Player):
    def __init__(self):
        super().__init__()
        self.hp = 90
        self.start_hp = 90
        self.damage = 10
        self.defend = 20
        self.potions = 3
        self.start_pot = 3
        self.race = "Human"


class Elf(Player):
    def __init__(self):
        super().__init__()
        self.hp = 95
        self.start_hp = 95
        self.damage = 15
        self.defend = 15
        self.potions = 2
        self.start_pot = 2
        self.race = "Elf"


class Dwarf(Player):
    def __init__(self):
        super().__init__()
        self.hp = 100
        self.start_hp = 100
        self.damage = 20
        self.defend = 10
        self.potions = 1
        self.start_pot = 1
        self.race = "Dwarf"
