class Enemy(object):
    def __init__(self, name, weapon, health, mana, armor, image):
        self.image
        self.name = name
        self.weapon = weapon
        self.health = health
        self.mana = mana
        self.armor = armor
    def set_mana(self, new_mana):
        self.mana = new_mana
    def set_health(self, new_health):
        self.health = new_health