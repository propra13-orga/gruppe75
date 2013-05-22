import pygame
import graphics
import room
import tile
import os
import time

# Init
pygame.init()
pygame.mouse.set_visible(1)

# Farben
white = 255,255,255
black = 0,0,0

# hintergrund
def backGroundScreen(colour):
   screen = pygame.display.set_mode((640,480))  
   backgrnd = colour
   screen.fill(backgrnd)
   pygame.display.flip()
   return screen

background = black
screen = backGroundScreen(background)

# Schrift
def getFont(name = None, size = 20):
   font = pygame.font.Font(name, size)
   return font

# Rendern
def putText(fontOBJ, message = "", position = (150,10),
            forecolour = black, backcolour = white):
    antialias = True
    text = fontOBJ.render(message, antialias, forecolour, backcolour)
    textRect = text.get_rect()
    textRect.topleft = position
    screen.blit(text, textRect)
    pygame.display.update()

# Header
headerfont = getFont(None,34)
header = "Druecke Enter zum starten"
position = 150,10
putText(headerfont, header, position, 
    forecolour = white,	
    backcolour = background)
    
# Wait
# Loop
done = False
while not done:
   for event in pygame.event.get():
      if event.type == pygame.KEYDOWN:
         if (event.key == pygame.K_RETURN):
            done = True


def check_for_collision(player_pos,map):
    solid_list = map.list_solid_tiles()
    if player_pos in solid_list:
        return True
    else:
        return False 
        
def check_for_warppoint(player_pos,map):
    warp_list = map.list_warp_tiles()
    if player_pos in warp_list:
        return True
    else:
        return False

def check_for_finish(player_pos,map):
    finish_list = map.list_finish_tiles()
    if player_pos in finish_list:
        return True
    else:
        return False
        
def menu():
    background = black
    screen = backGroundScreen(background)
    headerfont = getFont(None,34)
    header = "Druecke Enter zum starten"
    position = 150,10
    putText(headerfont, header, position, 
        forecolour = white,	
        backcolour = background)
    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if (event.key == pygame.K_RETURN):
                    done = True
    if done == True:
        game()
global level
level = 1
def game():
    global level
    level = 1
    pygame.init()
    pygame.display.set_mode(graphics.screen_size)
    pygame.display.set_caption("Dungeon Crawler")
    pygame.mouse.set_visible(1)
    pygame.key.set_repeat(1, 30)
    clock = pygame.time.Clock()
    tile.init()
    map = room.load(os.path.join("data", "level.txt"))
    screen = pygame.display.get_surface()
    player = pygame.image.load(os.path.join(os.path.join("tiles"), "player.png")).convert_alpha()
    player_pos = (32,32)
    # running = True, game loop
    
    running = True
    while running:
        # run game with 30 frames
        clock.tick(30)
        # screen surface black
        screen.fill((0, 0, 0))
        
        # end game if finding a quit event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        # end game when escape is pressed
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.event.post(pygame.event.Event(pygame.QUIT))
                
                if event.key == pygame.K_UP:
                    finish = check_for_finish((player_pos[0],player_pos[1]-32),map)
                    warp = check_for_warppoint((player_pos[0],player_pos[1]-32),map)
                    collision = check_for_collision((player_pos[0],player_pos[1]-32),map)
                    if collision == False:
                        if warp == True:
                            level=level+1
                            map = room.load(os.path.join("data", "level"+ str(level) +".txt"))
                            player_pos = (32,32)
                        elif finish == True:
                            win = pygame.image.load(os.path.join(os.path.join("tiles"), "win.png")).convert_alpha()
                            screen.blit(win,(50,100))
                            time.sleep(3)
                            menu()
                        else:
                            player_pos = (player_pos[0],player_pos[1]-32)
                    elif collision == True:
                        pass
                    
                if event.key == pygame.K_DOWN:
                    finish = check_for_finish((player_pos[0],player_pos[1]+32),map)
                    warp = check_for_warppoint((player_pos[0],player_pos[1]+32),map)
                    collision = check_for_collision((player_pos[0],player_pos[1]+32),map)
                    if collision == False:
                        if warp == True:
                            level=level+1
                            map = room.load(os.path.join("data", "level"+str(level)+".txt"))
                            player_pos = (32,32)
                        elif finish == True:
                            win = pygame.image.load(os.path.join(os.path.join("tiles"), "win.png")).convert_alpha()
                            screen.blit(win,(50,100))
                            time.sleep(3)
                            menu()
                        else:
                            player_pos = (player_pos[0],player_pos[1]+32)
                    elif collision == True:
                        pass
                
                if event.key == pygame.K_LEFT:
                    finish = check_for_finish((player_pos[0]-32,player_pos[1]),map)
                    warp = check_for_warppoint((player_pos[0]-32,player_pos[1]),map)
                    collision = check_for_collision((player_pos[0]-32,player_pos[1]),map)
                    if collision == False:
                        if warp == True:
                            level=level+1
                            map = room.load(os.path.join("data", "level"+str(level)+".txt"))
                            player_pos = (32,32)
                        elif finish == True:
                            win = pygame.image.load(os.path.join(os.path.join("tiles"), "win.png")).convert_alpha()
                            screen.blit(win,(50,100))
                            time.sleep(3)
                            menu()
                        else:
                            player_pos = (player_pos[0]-32,player_pos[1])
                    elif collision == True:
                        pass
                
                if event.key == pygame.K_RIGHT:
                    finish = check_for_finish((player_pos[0]+32,player_pos[1]),map)
                    warp = check_for_warppoint((player_pos[0]+32,player_pos[1]),map)
                    collision = check_for_collision((player_pos[0]+32,player_pos[1]),map)
                    if collision == False:
                        if warp == True:
                            level=level+1
                            map = room.load(os.path.join("data", "level"+str(level)+".txt"))
                            player_pos = (32,32)
                        elif finish == True:
                            win = pygame.image.load(os.path.join(os.path.join("tiles"), "win.png")).convert_alpha()
                            screen.blit(win,(1,1))
                            time.sleep(3)
                            menu()
                        else:
                            player_pos = (player_pos[0]+32,player_pos[1])
                    elif collision == True:
                        pass
        
        # draw map on screen
        map.draw(screen)
        screen.blit(player,player_pos)
        pygame.display.flip()
        
        
def main():
    game()
        
# call main method
if __name__ == "__main__":
    main()