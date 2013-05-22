import pygame
import graphics
import room
import tile
import os


def check_for_collision(player_pos,map):
    solid_list = map.list_solid_tiles()
    if player_pos in solid_list:
        return True
    else:
        return False 
        
def check_for_warppoint(player_pos,map):
    warp_list = map.list_warp_tiles()
    if player_pos in solid_list:
        return True
    else:
        return False
def game():    
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
                    collision = check_for_collision((player_pos[0],player_pos[1]-32),map)
                    if collision == False:
                        player_pos = (player_pos[0],player_pos[1]-32)
                    elif collision == True:
                        pass
                    
                if event.key == pygame.K_DOWN:
                    collision = check_for_collision((player_pos[0],player_pos[1]+32),map)
                    if collision == False:
                        player_pos = (player_pos[0],player_pos[1]+32)
                    elif collision == True:
                        pass
                
                if event.key == pygame.K_LEFT:
                    collision = check_for_collision((player_pos[0]-32,player_pos[1]),map)
                    if collision == False:
                        player_pos = (player_pos[0]-32,player_pos[1])
                    elif collision == True:
                        pass
                
                if event.key == pygame.K_RIGHT:
                    collision = check_for_collision((player_pos[0]+32,player_pos[1]),map)
                    if collision == False:
                        player_pos = (player_pos[0]+32,player_pos[1])
                    elif collision == True:
                        pass
        
        # draw map on screen
        map.draw(screen)
        screen.blit(player,player_pos)
        pygame.display.flip()
        
        
def main():
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
                    collision = check_for_collision((player_pos[0],player_pos[1]-32),map)
                    if collision == False:
                        player_pos = (player_pos[0],player_pos[1]-32)
                    elif collision == True:
                        pass
                    
                if event.key == pygame.K_DOWN:
                    collision = check_for_collision((player_pos[0],player_pos[1]+32),map)
                    if collision == False:
                        player_pos = (player_pos[0],player_pos[1]+32)
                    elif collision == True:
                        pass
                
                if event.key == pygame.K_LEFT:
                    collision = check_for_collision((player_pos[0]-32,player_pos[1]),map)
                    if collision == False:
                        player_pos = (player_pos[0]-32,player_pos[1])
                    elif collision == True:
                        pass
                
                if event.key == pygame.K_RIGHT:
                    collision = check_for_collision((player_pos[0]+32,player_pos[1]),map)
                    if collision == False:
                        player_pos = (player_pos[0]+32,player_pos[1])
                    elif collision == True:
                        pass
        
        # draw map on screen
        map.draw(screen)
        screen.blit(player,player_pos)
        pygame.display.flip()
        
# call main method
if __name__ == "__main__":
    main()