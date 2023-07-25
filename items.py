class Item:
    def __init__(self):
        self.name = None
        self.value = None
        self.acquired = None

    def add_item(self, player):
        player.items[self.name] = self
        return player


class Halo(Item):
    def __init__(self):
        super().__init__()
        self.name = "Halo of Hardihood"
        self.value = 25
        self.acquired = True

    def powerup(self, player):
        player.start_hp += self.value
        return player


class Bangle(Item):
    def __init__(self):
        super().__init__()
        self.name = "Bangle of Brawn"
        self.value = 10
        self.acquired = True

    def powerup(self, player):
        player.defend += self.value
        return player


class Key(Item):
    def __init__(self):
        super().__init__()
        self.name = "Mysterious Key"
        self.acquired = True


class Brew(Item):
    def __init__(self):
        super().__init__()
        self.name = "Brew of Bloom"
        self.acquired = True
        self.value = 50

    def powerup(self, player):
        player.start_hp += self.value
        player.hp = player.start_hp
        return player


class Sharpstone(Item):
    def __init__(self):
        super().__init__()
        self.name = "Sharpening Stone"
        self.value = 10
        self.acquired = True

    def powerup(self, player):
        player.damage += self.value
        return player
