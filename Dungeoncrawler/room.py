import tile
import graphics

rows = graphics.screen_h/ tile.height
cols = graphics.screen_w/ tile.width

# room loader: 
def load(file_in):
    file_des = open(file_in)
    lines = file_des.readlines()
    file_des.close()
    
    tiles = []
    for c in range(cols):
        tiles.append([])
        for r in range(rows):
            tiles[c].append(tile.tile[lines[r][c]])
            
    return Room(tiles)        
      # Room class later: new roomes where they lead to etc.    
      
class Room(object):
    def __init__(self, tiles):
        self.tiles = tiles
        
    def draw(self, surface):
        for x in range(cols):
            for y in range(rows):
                surface.blit(self.tiles[x][y].surface, (x*tile.width, y*tile.height))