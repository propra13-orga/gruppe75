import pygame
import graphics
import room
import tile
import os
import time
import sys
from player import*
from item import*
from enemy import*
from spell import*

global leben
global spell_var
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
        
def check_for_interact(player_pos,map):
    interact_list = map.list_interact_tiles()
    if player_pos in interact_list:
        return True
    else:
        return False       

def check_for_shopping(player_pos,map):
    shopping_list = map.list_shopping_tiles()
    if player_pos in shopping_list:
        return True
    else:
        return False

def check_for_swords(player_pos,map):
    sword_list = map.list_sword_tiles()
    if player_pos in sword_list:
        return True
    else:
        return False

def damage_manager(aggressor,opfer):
    damage = aggressor.get_damage()
    opfer_health = opfer.get_health()
    opfer_health = opfer_health - damage
    if opferhealth <= 0:
        del opfer
        
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
        #game()
        return 0
       
def shop_menu(shop_mana, shop_money):
# one mana unit is ... money units
    mana_to_money_ratio = 10
    maximum_mana_per_player = 30000
    background = black
    screen = backGroundScreen(background)
    done = False
    while not done:
        header = pygame.image.load(os.path.join(os.path.join("tiles"), "shopping.png")).convert_alpha()
        screen.blit(header,(0,0))
        font = pygame.font.Font(None, 40)
        text_mana = font.render("Mana:"+str(shop_mana), 1, (0, 0, 0))
        text_money = font.render("Money:"+str(shop_money), 1, (0, 0, 0))
        text_shop_menue_1 = font.render("For 1 Mana: Press O", 1, (0, 0, 0))
        text_shop_menue_2 = font.render("For 10 Mana: Press T", 1, (0, 0, 0))
        text_shop_menue_3 = font.render("Leave the shop: Press L", 1, (0, 0, 0))
        screen.blit(text_mana, (100,100))
        screen.blit(text_money, (330,100))
        screen.blit(text_shop_menue_1, (100,200))
        screen.blit(text_shop_menue_2, (100,270))
        screen.blit(text_shop_menue_3, (300,400))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                # leave the shop
                if event.key == pygame.K_l:
                    done = True
                # buy one mana unit
                elif event.key == pygame.K_o:
                    # zu viel Mana nicht erlaubt
                    if shop_mana + 1 < maximum_mana_per_player:
                        # zu wenig Geld geht auch nicht
                        if shop_money - mana_to_money_ratio >= 0:
                            shop_mana = shop_mana + 1
                            shop_money = shop_money - mana_to_money_ratio
                # buy ten mana units
                elif event.key == pygame.K_t:
                    # zu viel Mana nicht erlaubt
                    if shop_mana + 1 < maximum_mana_per_player:
                        # zu wenig Geld geht auch nicht 
                        if shop_money - mana_to_money_ratio >= 0:
                            shop_mana = shop_mana + 10
                            shop_money = shop_money - 10 * mana_to_money_ratio
        # END OF for event in ...
    if done == True:
        # game()
        # egal, ob die Werte von shop_mana und shop_money geaendert wurden,
        # uebergeben wir die Werte als Tupel (shop_mana, shop_money) zurueck
        return (shop_mana, shop_money)

global level
level = 1
def game():
    global leben
    leben = 3
    global spell_var
    spell_var = False
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
    sword1 = weapon("sword1", 50,32)
    sword2 = weapon("sword2", 50,32)
    sword3 = weapon("sword3", 50,32)
    sword4 = weapon("sword4", 50,32)
    none = armor("none",0,"bild")
    player1 = player("player1",fist,none,100,50,1000,[],pygame.image.load(os.path.join(os.path.join("tiles"), "player.png")).convert_alpha())
    player1.change_position((32,32))
    enemy1 = enemy("gegner", 10, 20, 0, 0, (320, 256),pygame.image.load(os.path.join(os.path.join("tiles"), "gegner.png")).convert_alpha())
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
                elif event.key == pygame.K_UP:
                    #check, welches Feld wir betreten
                    sword = check_for_swords((player_pos[0],player_pos[1]-32),map)
                    back = check_for_back((player_pos[0],player_pos[1]-32),map)
                    fireballs = check_for_fireballs((player_pos[0],player_pos[1]-32),map)
                    traps = check_for_trap((player_pos[0],player_pos[1]-32),map)
                    finish = check_for_finish((player_pos[0],player_pos[1]-32),map)
                    warp = check_for_warppoint((player_pos[0],player_pos[1]-32),map)
                    collision = check_for_collision((player_pos[0],player_pos[1]-32),map)
                    interact = check_for_interact((player_pos[0],player_pos[1]-32),map)
                    shopping = check_for_shopping((player_pos[0],player_pos[1]-32),map)
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
                            player1.change_position((32,32))
                            enemy1.change_position((320,256))
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
                            if leben > 0:
                                leben = leben -1
                                if level == 1 or level == 2 or level == 3:
                                    level = 1
                                elif level == 4 or level == 5 or level == 6:
                                    level = 4
                                elif level == 7 or level == 8 or level == 9:
                                    level = 7
                                map = room.load(os.path.join("data", "level"+ str(level) +".txt"))
                                player1.change_position((32,32))
                                enemy1.change_position((320,256))
                            else:
                                menu()
                        elif back == True:
                            level=level-1
                            map = room.load(os.path.join("data", "level"+ str(level) +".txt"))
                            player1.change_position((32,32))
                            enemy1.change_position((320,256))
                        elif interact == True:
                            interact_image = pygame.image.load(os.path.join(os.path.join("tiles"), "interact_image.png")).convert_alpha()
                            screen.blit(interact_image,(0,0))
                            pygame.display.flip()
                            time.sleep(2)
                        elif shopping == True:
                            map.draw(screen)
                            shopping_image = pygame.image.load(os.path.join(os.path.join("tiles"), "shopping.png")).convert_alpha()
                            screen.blit(shopping_image,(0,0))
                            mana = player1.get_mana()
                            money = player1.get_money()
                            font = pygame.font.Font(None, 70)
                            text2 = font.render("Mana:"+str(mana), 1, (255, 170, 100))
                            text3 = font.render("Money:"+str(money), 1, (30, 255, 180))
                            screen.blit(text2, (100,200))
                            screen.blit(text3, (330,200))
                            pygame.display.flip()
                            mana_money_tupel = shop_menu(mana, money)
                            player1.set_mana(mana_money_tupel[0])
                            player1.set_money(mana_money_tupel[1])
                        elif sword == True:
                            player1.change_weapon(sword1)
                            playerimage = pygame.image.load(os.path.join(os.path.join("tiles"), "player_sword.png")).convert_alpha()
                            player1.change_image(playerimage)
                        else:
                            player1.change_position((player_pos[0],player_pos[1]-32))
                    elif collision == True:
                        pass
                    
                elif event.key == pygame.K_DOWN:
                    #check, welches Feld wir betreten
                    sword = check_for_swords((player_pos[0],player_pos[1]+32),map)
                    back = check_for_back((player_pos[0],player_pos[1]+32),map)
                    fireballs = check_for_fireballs((player_pos[0],player_pos[1]+32),map)
                    traps = check_for_trap((player_pos[0],player_pos[1]+32),map)
                    finish = check_for_finish((player_pos[0],player_pos[1]+32),map)
                    warp = check_for_warppoint((player_pos[0],player_pos[1]+32),map)
                    collision = check_for_collision((player_pos[0],player_pos[1]+32),map)
                    interact = check_for_interact((player_pos[0],player_pos[1]+32),map)
                    shopping = check_for_shopping((player_pos[0],player_pos[1]+32),map)
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
                            enemy1.change_position((320,256))
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
                            if leben > 0:
                                leben = leben -1
                                if level == 1 or level == 2 or level == 3:
                                    level = 1
                                elif level == 4 or level == 5 or level == 6:
                                    level = 4
                                elif level == 7 or level == 8 or level == 9:
                                    level = 7
                                map = room.load(os.path.join("data", "level"+ str(level) +".txt"))
                                player1.change_position((32,32))
                                enemy1.change_position((320,256))
                            else:
                                menu()
                        elif back == True:
                            level=level-1
                            map = room.load(os.path.join("data", "level"+ str(level) +".txt"))
                            player1.change_position((32,32))
                            enemy1.change_position((320,256))
                        elif interact == True:
                            interact_image = pygame.image.load(os.path.join(os.path.join("tiles"), "interact_image.png")).convert_alpha()
                            screen.blit(interact_image,(0,0))
                            pygame.display.flip()
                            time.sleep(2)
                            map = room.load(os.path.join("data", "level"+ str(level) +".txt"))
                        elif shopping == True:
                            map.draw(screen)
                            shopping_image = pygame.image.load(os.path.join(os.path.join("tiles"), "shopping.png")).convert_alpha()
                            screen.blit(shopping_image,(0,0))
                            mana = player1.get_mana()
                            money = player1.get_money()
                            font = pygame.font.Font(None, 70)
                            text2 = font.render("Mana:"+str(mana), 1, (255, 170, 100))
                            text3 = font.render("Money:"+str(money), 1, (30, 255, 180))
                            screen.blit(text2, (100,200))
                            screen.blit(text3, (330,200))
                            pygame.display.flip()
                            mana_money_tupel = shop_menu(mana, money)
                            player1.set_mana(mana_money_tupel[0])
                            player1.set_money(mana_money_tupel[1])
                        elif sword == True:
                            player1.change_weapon(sword1)
                            playerimage = pygame.image.load(os.path.join(os.path.join("tiles"), "player_sword.png")).convert_alpha()
                            player1.change_image(playerimage)
                        else:
                            player1.change_position((player_pos[0],player_pos[1]+32))
                    elif collision == True:
                        pass
                
                elif event.key == pygame.K_LEFT:
                    #check, welches Feld wir betreten
                    sword = check_for_swords((player_pos[0]-32,player_pos[1]),map)
                    back = check_for_back((player_pos[0]-32,player_pos[1]),map)
                    fireballs = check_for_fireballs((player_pos[0]-32,player_pos[1]),map)
                    traps = check_for_trap((player_pos[0]-32,player_pos[1]),map)
                    finish = check_for_finish((player_pos[0]-32,player_pos[1]),map)
                    warp = check_for_warppoint((player_pos[0]-32,player_pos[1]),map)
                    collision = check_for_collision((player_pos[0]-32,player_pos[1]),map)
                    interact = check_for_interact((player_pos[0]-32,player_pos[1]),map)
                    shopping = check_for_shopping((player_pos[0]-32,player_pos[1]),map)
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
                            enemy1.change_position((320,256))
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
                            if leben > 0:
                                leben = leben -1
                                if level == 1 or level == 2 or level == 3:
                                    level = 1
                                elif level == 4 or level == 5 or level == 6:
                                    level = 4
                                elif level == 7 or level == 8 or level == 9:
                                    level = 7
                                map = room.load(os.path.join("data", "level"+ str(level) +".txt"))
                                player1.change_position((32,32))
                                enemy1.change_position((320,256))
                            else:
                                menu()
                        elif back == True:
                            level=level-1
                            map = room.load(os.path.join("data", "level"+ str(level) +".txt"))
                            player1.change_position((32,32))
                            enemy1.change_position((320,256))
                        elif interact == True:
                            interact_image = pygame.image.load(os.path.join(os.path.join("tiles"), "interact_image.png")).convert_alpha()
                            screen.blit(interact_image,(0,0))
                            pygame.display.flip()
                            time.sleep(2)
                            map = room.load(os.path.join("data", "level"+ str(level) +".txt"))
                        elif shopping == True:
                            map.draw(screen)
                            shopping_image = pygame.image.load(os.path.join(os.path.join("tiles"), "shopping.png")).convert_alpha()
                            screen.blit(shopping_image,(0,0))
                            mana = player1.get_mana()
                            money = player1.get_money()
                            font = pygame.font.Font(None, 70)
                            text2 = font.render("Mana:"+str(mana), 1, (255, 170, 100))
                            text3 = font.render("Money:"+str(money), 1, (30, 255, 180))
                            screen.blit(text2, (100,200))
                            screen.blit(text3, (330,200))
                            pygame.display.flip()
                            mana_money_tupel = shop_menu(mana, money)
                            player1.set_mana(mana_money_tupel[0])
                            player1.set_money(mana_money_tupel[1])
                        elif sword == True:
                            player1.change_weapon(sword1)
                            playerimage = pygame.image.load(os.path.join(os.path.join("tiles"), "player_sword.png")).convert_alpha()
                            player1.change_image(playerimage)
                        else:
                            player1.change_position((player_pos[0]-32,player_pos[1]))
                    elif collision == True:
                        pass
                
                elif event.key == pygame.K_RIGHT:
                    #check, welches Feld wir betreten
                    sword = check_for_swords((player_pos[0]+32,player_pos[1]),map)
                    back = check_for_back((player_pos[0]+32,player_pos[1]),map)
                    fireballs = check_for_fireballs((player_pos[0]+32,player_pos[1]),map)
                    traps = check_for_trap((player_pos[0]+32,player_pos[1]),map)
                    finish = check_for_finish((player_pos[0]+32,player_pos[1]),map)
                    warp = check_for_warppoint((player_pos[0]+32,player_pos[1]),map)
                    collision = check_for_collision((player_pos[0]+32,player_pos[1]),map)
                    interact = check_for_interact((player_pos[0]+32,player_pos[1]),map)
                    shopping = check_for_shopping((player_pos[0]+32,player_pos[1]),map)
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
                            enemy1.change_position((320,256))
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
                            if leben > 0:
                                leben = leben -1
                                if level == 1 or level == 2 or level == 3:
                                    level = 1
                                elif level == 4 or level == 5 or level == 6:
                                    level = 4
                                elif level == 7 or level == 8 or level == 9:
                                    level = 7
                                map = room.load(os.path.join("data", "level"+ str(level) +".txt"))
                                player1.change_position((32,32))
                                enemy1.change_position((320,256))
                            else:
                                menu()
                        elif back == True:
                            level=level-1
                            map = room.load(os.path.join("data", "level"+ str(level) +".txt"))
                            player1.change_position((32,32))
                            enemy1.change_position((320,256))
                        elif interact == True:
                            interact_image = pygame.image.load(os.path.join(os.path.join("tiles"), "interact_image.png")).convert_alpha()
                            screen.blit(interact_image,(0,0))
                            pygame.display.flip()
                            time.sleep(5)
                            map = room.load(os.path.join("data", "level"+ str(level) +".txt"))
                        elif shopping == True:
                            map.draw(screen)
                            shopping_image = pygame.image.load(os.path.join(os.path.join("tiles"), "shopping.png")).convert_alpha()
                            screen.blit(shopping_image,(0,0))
                            mana = player1.get_mana()
                            money = player1.get_money()
                            font = pygame.font.Font(None, 70)
                            text2 = font.render("Mana:"+str(mana), 1, (255, 170, 100))
                            text3 = font.render("Money:"+str(money), 1, (30, 255, 180))
                            screen.blit(text2, (100,200))
                            screen.blit(text3, (330,200))
                            pygame.display.flip()
                            mana_money_tupel = shop_menu(mana, money)
                            player1.set_mana(mana_money_tupel[0])
                            player1.set_money(mana_money_tupel[1])
                        elif sword == True:
                            player1.change_weapon(sword1)
                            playerimage = pygame.image.load(os.path.join(os.path.join("tiles"), "player_sword.png")).convert_alpha()
                            player1.change_image(playerimage)
                        else:
                            player1.change_position((player_pos[0]+32,player_pos[1]))
                    elif collision == True:
                        pass
                elif event.key == pygame.K_w:
                    mana = player1.get_mana()
                    if mana < 10:
                        pass
                    elif mana >= 10:
                        player1.set_mana(player1.get_mana()-10)
                        
                        spell_pic = player1.launch_spell("UP")
                        spell1 = spell(player1.get_position(),"UP",10,spell_pic)
                        spell_var = True
                
                elif event.key == pygame.K_s:
                    mana = player1.get_mana()
                    if mana < 10:
                        pass
                    elif mana >= 10:
                        player1.set_mana(player1.get_mana()-10)
                        
                        spell_pic = player1.launch_spell("DOWN")
                        spell1 = spell(player1.get_position(),"DOWN",10,spell_pic)
                        spell_var = True
                 
                elif event.key == pygame.K_a:
                    mana = player1.get_mana()
                    if mana < 10:
                        pass
                    elif mana >= 10:
                        player1.set_mana(player1.get_mana()-10)
                        
                        spell_pic = player1.launch_spell("LEFT")
                        spell1 = spell(player1.get_position(),"LEFT",10,spell_pic)
                        spell_var = True
        
                elif event.key == pygame.K_d:
                    mana = player1.get_mana()
                    if mana < 10:
                        pass
                    elif mana >= 10:
                        player1.set_mana(player1.get_mana()-10)
                        
                        spell_pic = player1.launch_spell("RIGHT")
                        spell1 = spell(player1.get_position(),"RIGHT",10,spell_pic)
                        spell_var = True    
        
        
        # draw map on screen
        map.draw(screen)
        enemy1.move(map)
        if spell_var == True:
            spell_var = spell1.move(map)
            if spell_var == False:
                del spell1
            elif spell_var == True:
                screen.blit(spell1.get_image(), spell1.get_position())
        screen.blit(player1.get_image(),player1.get_position())
        screen.blit(enemy1.get_image(), enemy1.get_position())
        
        mana = player1.get_mana()
        health = player1.get_health()
        money = player1.get_money()
        font = pygame.font.Font(None, 36)
        text1 = font.render("Health:"+str(health), 1, (255, 255, 255))
        text2 = font.render("Mana:"+str(mana), 1, (255, 255, 255))
        text3 = font.render("Money:"+str(money), 1, (255, 255, 255))
        if leben == 1:
            leben1 = pygame.image.load(os.path.join(os.path.join("tiles"), "1leben.png")).convert_alpha()
            screen.blit(leben1, (450,0))
        elif leben == 2:
            leben1 = pygame.image.load(os.path.join(os.path.join("tiles"), "2leben.png")).convert_alpha()
            screen.blit(leben1, (450,0))
        elif leben == 3:
            leben1 = pygame.image.load(os.path.join(os.path.join("tiles"), "3leben.png")).convert_alpha()
            screen.blit(leben1, (450,0))
        screen.blit(text1, (0,0))
        screen.blit(text2, (150,0))
        screen.blit(text3, (300,0))
        pygame.display.flip()
        
def main():
    game()
        
# call main method
if __name__ == "__main__":
    main()
