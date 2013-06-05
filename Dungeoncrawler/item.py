class item(object):
    def __init__(self, name):
        self.name = name
        
        
class weapon(item):
    def __init__(self, name, damage, range):
        item.__init__(self, name)
        self.damage = damage
        self.range = range

class armor(item):
    def __init__(self, name, damage_reduction, image):
        self.image = image
        self.name = name
        self.damage_reduction = damage_reduction