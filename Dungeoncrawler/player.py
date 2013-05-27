import pygame

class player(object):
    #Variablentypen
    #name: string, weapon: weapon object, armor: armor object, health: int, mana: int, money:int, items: Liste
    def __init__(self, name, weapon, armor , health, mana, money, items):
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
