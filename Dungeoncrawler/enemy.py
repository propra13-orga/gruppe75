class Enemy(object):
    def __init__(self, name, weapon, health, mana, armor, image):
        self.image = image
        self.name = name
        self.weapon = weapon
        self.health = health
        self.mana = mana
        self.armor = armor
    def get_image(self):
        return self.image
    def get_name(self):
        return self.name
    def get_weapon(self):
        return self.weapon
    def get_health(self):
        return self.health
    def get_mana(self):
        return self.mana
    def get_armor(self):
        return self.armor
    def set_mana(self, new_mana):
        self.mana = new_mana
    def set_health(self, new_health):
        self.health = new_health