class Item(object):
    def __init__(self, name):
        self.name = name
        
        
class Weapon(Item):
    def __init__(self, name, damage, range):
        item.__init__(self, name)
        self.damage = damage
        self.range = range