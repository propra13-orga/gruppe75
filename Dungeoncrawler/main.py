import pygame
import graphics
import room
import tile
import os
import time
import sys
from player import*
from item import*
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

# Wait
# Loop
done = False
while not done:
    header = pygame.image.load(os.path.join(os.path.join("tiles"), "menu.png")).convert_alpha()
    position = (0,0)
    screen.blit(header,position)
    
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if (event.key == pygame.K_RETURN):
                done = True
            if event.key == pygame.K_ESCAPE:
                sys.exit()
    pygame.display.flip()
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

def check_for_trap(player_pos,map):
    trap_list = map.list_trap_tiles()
    if player_pos in trap_list:
        return True
    else:
        return False

def check_for_fireballs(player_pos,map):
    fireball_list = map.list_fireball_tiles()
    if player_pos in fireball_list:
        return True
    else:
        return False

def check_for_back(player_pos,map):
    back_list = map.list_back_tiles()
    if player_pos in back_list:
        return True
    else:
        return False

def menu():
    background = black
    screen = backGroundScreen(background)
    done = False
    while not done:
        header = pygame.image.load(os.path.join(os.path.join("tiles"), "menu.png")).convert_alpha()
        position = (0,0)
        screen.blit(header,position)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    done = True
                if event.key == pygame.K_ESCAPE:
                    sys.exit()
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
    map = room.load(os.path.join("data", "level1.txt"))
    screen = pygame.display.get_surface()
    fist = weapon("fist",1,32)
    none = armor("none",0,"bild")
    player1 = player("player1",fist,none,100,50,1000,[],pygame.image.load(os.path.join(os.path.join("tiles"), "player.png")).convert_alpha())
    player1.change_position((32,32))
    # running = True, game loop
    
    running = True
    while running:
        # run game with 30 frames
        clock.tick(30)
        # screen surface black
        screen.fill((0, 0, 0))
        player_pos = player1.get_position()
        # end game if finding a quit event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        # end game when escape is pressed
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.event.post(pygame.event.Event(pygame.QUIT))
                #Steuerung
                if event.key == pygame.K_UP:
                    #check, welches Feld wir betreten
                    back = check_for_back((player_pos[0],player_pos[1]-32),map)
                    fireballs = check_for_fireballs((player_pos[0],player_pos[1]-32),map)
                    traps = check_for_trap((player_pos[0],player_pos[1]-32),map)
                    finish = check_for_finish((player_pos[0],player_pos[1]-32),map)
                    warp = check_for_warppoint((player_pos[0],player_pos[1]-32),map)
                    collision = check_for_collision((player_pos[0],player_pos[1]-32),map)
                    if collision == False:
                        if warp == True:
                            level=level+1
                            if level == 4:
                                next = pygame.image.load(os.path.join(os.path.join("tiles"), "level_2.png")).convert_alpha()
                                screen.blit(next, (0,0))
                                pygame.display.flip()
                                time.sleep(3)
                            elif level == 7:
                                next = pygame.image.load(os.path.join(os.path.join("tiles"), "level_3.png")).convert_alpha()
                                screen.blit(next, (0,0))
                                pygame.display.flip()
                                time.sleep(3)
                            map = room.load(os.path.join("data", "level"+ str(level) +".txt"))
                            player_1.change_position((32,32))
                        elif finish == True:
                            win = pygame.image.load(os.path.join(os.path.join("tiles"), "win.png")).convert_alpha()
                            screen.blit(win,(0,0))
                            pygame.display.flip()
                            time.sleep(3)
                            menu()
                        elif traps == True:
                            fail = pygame.image.load(os.path.join(os.path.join("tiles"), "lost.png")).convert_alpha()
                            screen.blit(fail,(0,0))
                            pygame.display.flip()
                            time.sleep(3)
                            menu()
                        elif back == True:
                            level=level-1
                            map = room.load(os.path.join("data", "level"+ str(level) +".txt"))
                            player1.change_position((32,32))
                        else:
                            player1.change_position((player_pos[0],player_pos[1]-32))
                    elif collision == True:
                        pass
                    
                if event.key == pygame.K_DOWN:
                    #check, welches Feld wir betreten
                    back = check_for_back((player_pos[0],player_pos[1]+32),map)
                    fireballs = check_for_fireballs((player_pos[0],player_pos[1]+32),map)
                    traps = check_for_trap((player_pos[0],player_pos[1]+32),map)
                    finish = check_for_finish((player_pos[0],player_pos[1]+32),map)
                    warp = check_for_warppoint((player_pos[0],player_pos[1]+32),map)
                    collision = check_for_collision((player_pos[0],player_pos[1]+32),map)
                    if collision == False:
                        if warp == True:
                            level=level+1
                            if level == 4:
                                next = pygame.image.load(os.path.join(os.path.join("tiles"), "level_2.png")).convert_alpha()
                                screen.blit(next, (0,0))
                                pygame.display.flip()
                                time.sleep(3)
                            elif level == 7:
                                next = pygame.image.load(os.path.join(os.path.join("tiles"), "level_3.png")).convert_alpha()
                                screen.blit(next, (0,0))
                                pygame.display.flip()
                                time.sleep(3)
                            map = room.load(os.path.join("data", "level"+str(level)+".txt"))
                            player1.change_position((32,32))
                        elif finish == True and level == 3:
                            win = pygame.image.load(os.path.join(os.path.join("tiles"), "win.png")).convert_alpha()
                            screen.blit(win,(0,0))
                            pygame.display.flip()
                            time.sleep(3)
                            menu()
                        elif traps == True:
                            fail = pygame.image.load(os.path.join(os.path.join("tiles"), "lost.png")).convert_alpha()
                            screen.blit(fail,(0,0))
                            pygame.display.flip()
                            time.sleep(3)
                            menu()
                        elif back == True:
                            level=level-1
                            map = room.load(os.path.join("data", "level"+ str(level) +".txt"))
                            player1.change_position((32,32))
                        else:
                            player1.change_position((player_pos[0],player_pos[1]+32))
                    elif collision == True:
                        pass
                
                if event.key == pygame.K_LEFT:
                    #check, welches Feld wir betreten
                    back = check_for_back((player_pos[0]-32,player_pos[1]),map)
                    fireballs = check_for_fireballs((player_pos[0]-32,player_pos[1]),map)
                    traps = check_for_trap((player_pos[0]-32,player_pos[1]),map)
                    finish = check_for_finish((player_pos[0]-32,player_pos[1]),map)
                    warp = check_for_warppoint((player_pos[0]-32,player_pos[1]),map)
                    collision = check_for_collision((player_pos[0]-32,player_pos[1]),map)
                    if collision == False:
                        if warp == True:
                            level=level+1
                            if level == 4:
                                next = pygame.image.load(os.path.join(os.path.join("tiles"), "level_2.png")).convert_alpha()
                                screen.blit(next, (0,0))
                                pygame.display.flip()
                                time.sleep(3)
                            elif level == 7:
                                next = pygame.image.load(os.path.join(os.path.join("tiles"), "level_3.png")).convert_alpha()
                                screen.blit(next, (0,0))
                                pygame.display.flip()
                                time.sleep(3)
                            map = room.load(os.path.join("data", "level"+str(level)+".txt"))
                            player1.change_position((32,32))
                        elif finish == True:
                            win = pygame.image.load(os.path.join(os.path.join("tiles"), "win.png")).convert_alpha()
                            screen.blit(win,(0,0))
                            pygame.display.flip()
                            time.sleep(3)
                            menu()
                        elif traps == True:
                            fail = pygame.image.load(os.path.join(os.path.join("tiles"), "lost.png")).convert_alpha()
                            screen.blit(fail,(0,0))
                            pygame.display.flip()
                            time.sleep(3)
                            menu()
                        elif back == True:
                            level=level-1
                            map = room.load(os.path.join("data", "level"+ str(level) +".txt"))
                            player1.change_position((32,32))
                        else:
                            player1.change_position((player_pos[0]-32,player_pos[1]))
                    elif collision == True:
                        pass
                
                if event.key == pygame.K_RIGHT:
                    #check, welches Feld wir betreten
                    back = check_for_back((player_pos[0]+32,player_pos[1]),map)
                    fireballs = check_for_fireballs((player_pos[0]+32,player_pos[1]),map)
                    traps = check_for_trap((player_pos[0]+32,player_pos[1]),map)
                    finish = check_for_finish((player_pos[0]+32,player_pos[1]),map)
                    warp = check_for_warppoint((player_pos[0]+32,player_pos[1]),map)
                    collision = check_for_collision((player_pos[0]+32,player_pos[1]),map)
                    if collision == False:
                        if warp == True:
                            level=level+1
                            if level == 4:
                                next = pygame.image.load(os.path.join(os.path.join("tiles"), "level_2.png")).convert_alpha()
                                screen.blit(next, (0,0))
                                pygame.display.flip()
                                time.sleep(3)
                            elif level == 7:
                                next = pygame.image.load(os.path.join(os.path.join("tiles"), "level_3.png")).convert_alpha()
                                screen.blit(next, (0,0))
                                pygame.display.flip()
                                time.sleep(3)    
                            map = room.load(os.path.join("data", "level"+str(level)+".txt"))
                            player1.change_position((32,32))
                        elif finish == True:
                            win = pygame.image.load(os.path.join(os.path.join("tiles"), "win.png")).convert_alpha()
                            screen.blit(win,(0,0))
                            pygame.display.flip()
                            time.sleep(3)
                            menu()
                        elif traps == True:
                            fail = pygame.image.load(os.path.join(os.path.join("tiles"), "lost.png")).convert_alpha()
                            screen.blit(fail,(0,0))
                            pygame.display.flip()
                            time.sleep(3)
                            menu()
                        elif back == True:
                            level=level-1
                            map = room.load(os.path.join("data", "level"+ str(level) +".txt"))
                            player1.change_position((32,32))
                        else:
                            player1.change_position((player_pos[0]+32,player_pos[1]))
                    elif collision == True:
                        pass
                     
        
        
        # draw map on screen
        map.draw(screen)
        screen.blit(player1.get_image(),player1.get_position())

        
        mana = player1.get_mana()
        health = player1.get_health()
        money = player1.get_money()
        font = pygame.font.Font(None, 36)
        text1 = font.render("Health:"+str(health), 1, (255, 255, 255))
        text2 = font.render("Mana:"+str(mana), 1, (255, 255, 255))
        text3 = font.render("Money:"+str(money), 1, (255, 255, 255))
        screen.blit(text1, (0,0))
        screen.blit(text2, (150,0))
        screen.blit(text3, (300,0))
        pygame.display.flip()
        
def main():
    game()
        
# call main method
if __name__ == "__main__":
    main()
