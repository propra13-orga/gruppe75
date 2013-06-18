import os
import pygame

# Tile dimensions


height = 32
width = 32
size = (width, height)

image_path = os.path.join("tiles")

tile_info = {
# code: ( name, solid, image_file)
    " " : ("floor", False, "floor.png"),
    "#" : ("wall", True, "wall.png"),
    "P" : ("player", True, "player.png"),
    "+" : ("warp", False, "floor.png"),
    "-" : ("finish", False, "floor.png"),
    "T" : ("trap", False, "trap.png"),
    "F" : ("fireball", False, "fireball.png"),
    "B" : ("back", False, "floor.png"),
    "S" : ("sowrd", False, "sword.png")
    }
    
class Tile(object):
    def __init__(self, name, solid, surface):
        self.name = name
        self.solid = solid
        self.surface = surface
        
        
def init():
    global tile
    tile = {}
    
    for t in tile_info.keys():
        name = tile_info[t][0]
        solid = tile_info[t][1]
        surface = pygame.image.load(os.path.join(image_path, tile_info[t][2])).convert_alpha()
        tile[t] = Tile(name, solid, surface)
