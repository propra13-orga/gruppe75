import pygame
import os

def check_for_enemy( player1, enemy1, boss, position):
    liste = [player1.get_position(),enemy1.get_position(),boss.get_position()]
    if position in liste:
        return liste
    

def check_for_collision(player_pos,map):
    solid_list = map.list_solid_tiles()
    if player_pos in solid_list:
        return True
    else:
        return False 


class spell(object):
    def __init__(self, position, direction, damage, image):
        self.position = position
        self.direction = direction
        self.damage = damage
        self.image = image
        
    def get_position(self):
        return self.position
    def get_direction(self):
        return self.direction
    def get_damage(self):
        return self.damage
    def get_image(self):
        return self.image
    def set_position(self, new_position):
        self.position = new_position
    def move(self, map, player1, enemy1, boss):
        if self.direction == "UP":
            solid = check_for_collision((self.position[0],self.position[1]-32),map)
            enemy = check_for_enemy(playe1, enemy1, boss, (self.position[0],self.position[1]-32))
            if solid == False:
                self.position = (self.position[0],self.position[1]-32)
                return True
            elif solid == True:
                return False
        elif self.direction == "DOWN":
            solid = check_for_collision((self.position[0],self.position[1]+32),map)
            enemy = check_for_enemy(playe1, enemy1, boss, (self.position[0],self.position[1]+32))
            if solid == False:
                self.position = (self.position[0],self.position[1]+32)
                return True
            elif solid == True:
                return False
        elif self.direction == "LEFT":
            solid = check_for_collision((self.position[0]-32,self.position[1]),map)
            enemy = check_for_enemy(playe1, enemy1, boss, (self.position[0]-32,self.position[1]))
            if solid == False:
                self.position = (self.position[0]-32,self.position[1])
                return True
            elif solid == True:
                return False
        elif self.direction == "RIGHT":
            solid = check_for_collision((self.position[0]+32,self.position[1]),map)
            enemy = check_for_enemy(playe1, enemy1, boss, (self.position[0]+32,self.position[1]))
            if solid == False:
                self.position = (self.position[0]+32,self.position[1])
                return True
            elif solid == True:
                return False