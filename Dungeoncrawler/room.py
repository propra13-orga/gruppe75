import tile
import graphics

rows = graphics.screen_h/ tile.height
cols = graphics.screen_w/ tile.width

# room loader, load and read .txt file 
def load(file_in):
    file_des = open(file_in)
    lines = file_des.readlines()
    file_des.close()
    
    tiles = []
    for c in range(cols):
        tiles.append([])
        for r in range(rows):
            tiles[c].append(tile.tile[lines[r][c]]) # notice: transposition over here! [r][c] isntead of [c][r]
            
    return Room(tiles)  

    
# Room class later: new roomes where they lead to etc.    
      
class Room(object):
    def __init__(self, tiles):
        self.tiles = tiles
    
    def get_tiles_and_coordinates(self):
        dict = {}
        for x in range(cols):
            for y in range(rows):
                dict.update({self.tiles[x][y]:(x*tile.width, y*tile.height)})
        return dict
    
    def draw(self, surface):
        for x in range(cols):
            for y in range(rows):
                surface.blit(self.tiles[x][y].surface, (x*tile.width, y*tile.height))
    #prueft auf feste Elemente
    def list_solid_tiles(self):
        solid_tile_list = []
        for x in range(cols):
            for y in range(rows):
                if self.tiles[x][y].solid == True:
                    solid_tile_list.append((x*tile.width, y*tile.height))
        return solid_tile_list
    #prueft auf Level-Ende
    def list_warp_tiles(self):
        warp_tile_list = []
        for x in range(cols):
            for y in range(rows):
                if self.tiles[x][y].name == "warp":
                    warp_tile_list.append((x*tile.width, y*tile.height))
        return warp_tile_list
    #prueft auf gewinn-Feld
    def list_finish_tiles(self):
        finish_tile_list = []
        for x in range(cols):
            for y in range(rows):
                if self.tiles[x][y].name == "finish":
                    finish_tile_list.append((x*tile.width, y*tile.height))
        return finish_tile_list
    #prueft auf fallen
    def list_trap_tiles(self):
        trap_tile_list = []
        for x in range(cols):
            for y in range(rows):
                if self.tiles[x][y].name == "trap":
                    trap_tile_list.append((x*tile.width, y*tile.height))
        return trap_tile_list
    #prueft auf feuerball
    def list_fireball_tiles(self):
        fireball_tile_list = []
        for x in range(cols):
            for y in range(rows):
                if self.tiles[x][y].name == "fireball":
                    fireball_tile_list.append((x*tile.width, y*tile.height))
        return fireball_tile_list
    #prueft auf zurueck
    def list_back_tiles(self):
        back_tile_list = []
        for x in range(cols):
            for y in range(rows):
                if self.tiles[x][y].name == "back":
                    back_tile_list.append((x*tile.width, y*tile.height))
        return back_tile_list
    # prueft auf interact
    def list_interact_tiles(self):
        interact_tile_list = []
        for x in range(cols):
            for y in range(rows):
                if self.tiles[x][y].name == "interact":
                    interact_tile_list.append((x*tile.width, y*tile.height))
        return interact_tile_list
      #prueft auf shopping
    def list_shopping_tiles(self):
        shopping_tile_list = []
        for x in range(cols):
            for y in range(rows):
                if self.tiles[x][y].name == "shopping":
                    shopping_tile_list.append((x*tile.width, y*tile.height))
        return shopping_tile_list

    def list_sword_tiles(self):
        sword_tile_list = []
        for x in range(cols):
            for y in range(rows):
                if self.tiles[x][y].name == "sword":
                    sword_tile_list.append((x*tile.width, y*tile.height))
        return sword_tile_list
    
    def list_mana_tiles(self):
        mana_tile_list = []
        for x in range(cols):
            for y in range(rows):
                if self.tiles[x][y].name == "managain":
                    mana_tile_list.append((x*tile.width, y*tile.height))
        return mana_tile_list
    
    def list_health_tiles(self):
        health_tile_list = []
        for x in range(cols):
            for y in range(rows):
                if self.tiles[x][y].name == "healthgain":
                    health_tile_list.append((x*tile.width, y*tile.height))
        return health_tile_list
    
    def list_cash_tiles(self):
        cash_tile_list = []
        for x in range(cols):
            for y in range(rows):
                if self.tiles[x][y].name == "cashgain":
                    cash_tile_list.append((x*tile.width, y*tile.height))
        return cash_tile_list