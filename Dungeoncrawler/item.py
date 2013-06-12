class item(object):
    def __init__(self, name):
        self.name = name
    def get_name(self):
        return self.name
        
class weapon(item):
    def __init__(self, name, damage, range):
        item.__init__(self, name)
        self.damage = damage
        self.range = range
    def get_damage(self):
        return self.damage

class armor(item):
    def __init__(self, name, damage_reduction, image):
        item.__init__(self, name)
        self.image = image
        self.damage_reduction = damage_reduction