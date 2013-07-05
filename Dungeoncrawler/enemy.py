import pygame
import os

def check_for_collision(player_pos,map):
    solid_list = map.list_solid_tiles()
    if player_pos in solid_list:
        return True
    else:
        return False 

global direction
direction = "up"
class enemy(object):
    def __init__(self, name, damage, health, mana, damage_reduction, position, image, type):
        self.position = position
        self.image = image
        self.name = name
        self.damage = damage
        self.health = health
        self.mana = mana
        self.damage_reduction = damage_reduction
        self.type=type
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
    def take_damage(self, damage, type):

        if(self.type==type):
            #no damage
            self.health=self.health+(damage/10)
        
        if(self.type=="fire" and type=="water"):
            #full damage
            self.health=self.health-damage
        if(self.type=="fire" and type=="air"):
            #half damage 
            self.health=self.health-(damage/2)
        if(self.type=="fire" and type=="earth"):
            #quarter damage
            self.health=self.health-(damage/4)
        if(self.type=="water" and type=="fire"):
            #full damage
            self.health=self.health-damage
        if(self.type=="water" and type=="earth"):
            #half damage
            self.health=self.health-(damage/2)
        if(self.type=="water" and type=="air"):
            #quarter damage
            self.health=self.health-(damage/10)
        if(self.type=="air" and type=="fire"):
            #full damage
            self.health=self.health-damage
        if(self.type=="air" and type=="water"):
            #half damage
            self.health=self.health-(damage/2)
        if(self.type=="air" and type=="earth"):
            #quarter damage
            self.health=self.health-(damage/4)
        if(self.type=="earth" and type=="earth"):
            #full damage
            self.health=self.health-damage
        if(self.type=="earth" and type=="water"):
            #full damage
            self.health=self.health-damage
        if(self.type=="earth" and type=="air"):
            #half damage
            self.health=self.health-(damage/2)
        if(self.type=="earth" and type=="fire"):
            #quarter damage
            self.health=self.health-(damage/4)
                
        if self.health <= 0:
            self.health = 0

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
    def launch_spell(self, direction):
        if direction == "UP" or direction == "DOWN":
            spell = pygame.image.load(os.path.join(os.path.join("tiles"), "32x32t.png")).convert_alpha()
            return spell
        elif direction == "LEFT" or direction == "RIGHT":
            spell = pygame.image.load(os.path.join(os.path.join("tiles"), "32x32r.png")).convert_alpha()
            return spell