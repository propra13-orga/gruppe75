import pygame
import os
from main import check_for_collision

global direction
direction = "up"
class enemy(object):
    def __init__(self, name, damage, health, mana, damage_reduction, position, image):
        self.position = position
        self.image = image
        self.name = name
        self.damage = damage
        self.health = health
        self.mana = mana
        self.damage_reduction = damage_reduction
    def get_image(self):
        return self.image
    def get_name(self):
        return self.name
    def get_damage(self):
        return self.damage
    def get_health(self):
        return self.health
    def get_mana(self):
        return self.mana
    def get_damage_reduction(self):
        return self.damage_reduction
    def set_mana(self, new_mana):
        self.mana = new_mana
    def set_health(self, new_health):
        self.health = new_health
    def get_position(self):
        return self.position
    def change_position(self, new_position):
        self.position = new_position
    def move(self, map):
        global direction
        if direction == "up":
            collision = check_for_collision((self.position[0],self.position[1]-32),map)
            if collision == False:
                self.position = (self.position[0],self.position[1]-32)
            else:
                collision = check_for_collision((self.position[0],self.position[1]+32),map)
                if collision == False:
                    self.position = (self.position[0],self.position[1]+32)
                    direction = "down"
                else:
                    collision = check_for_collision((self.position[0]-32,self.position[1]),map)
                    if collision == False:
                        self.position = (self.position[0]-32,self.position[1])
                        direction = "left"
                    else:
                        collision = check_for_collision((self.position[0]+32,self.position[1]),map)
                        if collision == False:
                            self.position = (self.position[0]+32,self.position[1])
                            direction = "right"
        elif direction == "down":
            collision = check_for_collision((self.position[0],self.position[1]+32),map)
            if collision == False:
                self.position = (self.position[0],self.position[1]+32)
            else:
                collision = check_for_collision((self.position[0],self.position[1]-32),map)
                if collision == False:
                    self.position = (self.position[0],self.position[1]-32)
                    direction = "up"
                else:
                    collision = check_for_collision((self.position[0]-32,self.position[1]),map)
                    if collision == False:
                        self.position = (self.position[0]-32,self.position[1])
                        direction = "left"
                    else:
                        collision = check_for_collision((self.position[0]+32,self.position[1]),map)
                        if collision == False:
                            self.position = (self.position[0]+32,self.position[1])
                            direction = "right"
        elif direction == "left":
            collision = check_for_collision((self.position[0]-32,self.position[1]),map)
            if collision == False:
                self.position = (self.position[0]-32,self.position[1])
            else:
                collision = check_for_collision((self.position[0],self.position[1]-32),map)
                if collision == False:
                    self.position = (self.position[0],self.position[1]-32)
                    direction = "up"
                else:
                    collision = check_for_collision((self.position[0],self.position[1]+32),map)
                    if collision == False:
                        self.position = (self.position[0],self.position[1]+32)
                        direction = "down"
                    else:
                        collision = check_for_collision((self.position[0]+32,self.position[1]),map)
                        if collision == False:
                            self.position = (self.position[0]+32,self.position[1])
                            direction = "right"
        elif direction == "right":
            collision = check_for_collision((self.position[0]+32,self.position[1]),map)
            if collision == False:
                self.position = (self.position[0]+32,self.position[1])
            else:
                collision = check_for_collision((self.position[0],self.position[1]-32),map)
                if collision == False:
                    self.position = (self.position[0],self.position[1]-32)
                    direction = "up"
                else:
                    collision = check_for_collision((self.position[0],self.position[1]+32),map)
                    if collision == False:
                        self.position = (self.position[0],self.position[1]+32)
                        direction = "down"
                    else:
                        collision = check_for_collision((self.position[0]-32,self.position[1]),map)
                        if collision == False:
                            self.position = (self.position[0]+32,self.position[1])
                            direction = "left"