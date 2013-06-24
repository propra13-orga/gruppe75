import pygame
import graphics
import os

class player(object):
    #Variablentypen
    #name: string, weapon: weapon object, armor: armor object, health: int,
    #mana: int, money:int, items: Liste, image: "geladenes"Bild 
    def __init__(self, name, weapon, armor , health, mana, money, items, image):
        self.position = (0,0)
        self.image = image
        self.name = name
        self.mana = mana
        self.health = health
        self.armor = armor
        self.weapon = weapon
        self.money = money
        self.items = items
    def set_mana(self, new_mana):
        self.mana = new_mana
    def set_health(self, new_health):
        self.health = new_health
    def set_money(self, new_money):
        self.money = new_money
    def add_item(self, item):
        self.items.append(item)
    def loose_item(self, item):
        self.items.remove(item)
    # wechselt die Waffe und steckt die alte Waffe in die Itemliste(Inventar)
    def change_weapon(self, new_weapon):
        self.add_item(self.weapon)
        self.weapon = new_weapon
    # kann auch fuer bewegung benutzt werden
    def change_image(self, new_image):
        self.image = new_image
    # new_position ist ein Tupel (x,y)
    def change_position(self, new_position):
        self.position = new_position
    def get_position(self):
        return self.position
    def get_image(self):
        return self.image
    def get_mana(self):
        return self.mana
    def get_health(self):
        return self.health
    def get_money(self):
        return self.money
    def get_name(self):
        return self.name
    def get_weapon(self):
        return self.weapon
    def get_armor(self):
        return self.armor
    def get_items(self):
        return self.items
    def take_damage(self, damage):
        health = self.health - damage
        if health <= 0:
            self.health = health
        else:
            self.health = health
    def launch_spell(self, direction):
        if direction == "UP" or direction == "DOWN":
            spell = pygame.image.load(os.path.join(os.path.join("tiles"), "32x32t.png")).convert_alpha()
            return spell
        elif direction == "LEFT" or direction == "RIGHT":
            spell = pygame.image.load(os.path.join(os.path.join("tiles"), "32x32r.png")).convert_alpha()
            return spell