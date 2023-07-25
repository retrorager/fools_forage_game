from simple_colors import *


class Enemy:
    def __init__(self):
        self.race = None
        self.hp = 0
        self.start_hp = 0
        self.damage = 0
        self.action = []

    def deal_damage(self):
        return self.damage

    def take_damage(self, opponent_damage):
        self.hp = self.hp - opponent_damage
        return self.hp


class Troll(Enemy):
    def __init__(self):
        super().__init__()
        self.race = green("Troll")
        self.hp = 200
        self.start_hp = 200
        self.damage = 20
        self.action = [green("smash", "italic"), green("rock toss", "italic")]


class Bogoblin(Enemy):
    def __init__(self):
        super().__init__()
        self.race = magenta("Bogoblin")
        self.hp = 95
        self.start_hp = 95
        self.damage = 8
        self.action = [magenta("rush", "italic"), magenta("scratch", "italic")]


class LakeMaiden(Enemy):
    def __init__(self):
        super().__init__()
        self.race = blue("Lake Maiden")
        self.hp = 120
        self.start_hp = 120
        self.damage = 14
        self.action = [blue("screech", "italic"), blue("water blast", "italic")]

