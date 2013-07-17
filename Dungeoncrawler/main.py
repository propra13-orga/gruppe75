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
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0,parentdir) 
from Mastermind import *

global leben
global spell_var1
global spell_var2
global spell_var3
# Init 
pygame.init()
pygame.mouse.set_visible(1)

# Farben
white = 255,255,255
black = 0,0,0

ip = "localhost"
port = 6317

demo = 0
if demo == 0:
    ClassClient = MastermindClientTCP
    ClassServer = MastermindServerTCP
else:
    ClassClient = MastermindClientUDP
    ClassServer = MastermindServerUDP
    
class Server(MastermindServerCallbacksEcho,MastermindServerCallbacksDebug,ClassServer):
    def __init__(self):
        ClassServer.__init__(self)
        
        
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

def check_for_interact2(player_pos,map):
    interact2_list = map.list_interact2_tiles()
    if player_pos in interact2_list:
        return True
    else:
        return False
        
def check_for_quest(player_pos,map):
    quest_list = map.list_quest_tiles()
    if player_pos in quest_list:
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

def check_for_mana(player_pos,map):
    mana_list = map.list_mana_tiles()
    if player_pos in mana_list:
        return True
    else:
        return False

def check_for_health(player_pos,map):
    health_list = map.list_health_tiles()
    if player_pos in health_list:
        return True
    else:
        return False
    
def check_for_cash(player_pos,map):
    cash_list = map.list_cash_tiles()
    if player_pos in cash_list:
        return True
    else:
        return False
        
def damage_manager(aggressor,opfer):
    damage = aggressor.get_damage()
    opfer_health = opfer.get_health()
    opfer_health = opfer_health - damage
    if opfer_health <= 0:
        opfer.set_health(0)
        del opfer
    else:
        opfer.set_health(opfer_health)
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

story_level_1 = ["",
                 "The murderer in the Rue Morgue was:",
                 "A:     The sailor",
                 "B:     Dupin",
                 "C:     The orangutan",
                 "       A, B or C?",
                 "",
                 ""]
story_level_2 = ["",
                 "The detective from the Orient Express", 
                 "Nun antworte mir: Nun antworte mir",
                 "A: Sherlock Holmes",
                 "B: Miss Marple",
                 "C: Hercule Poirot",
                 "Now give me the answer:",
                 "A, B or C?"]
story_level_3 = ["Level 3",
                 "The detective from the Orient Express", 
                 "Nun antworte mir: Nun antworte mir",
                 "A: Sherlock Holmes",
                 "B: Miss Marple",
                 "C: Hercule Poirot",
                 "Now give me the answer:",
                 "A, B or C?"]
story_level_4 = ["Level 4", 
                 "",
                 "The murderer in the Rue Morgue was:",
                 "A:     The sailor",
                 "B:     Dupin",
                 "C:     The orangutan",
                 "",
                 "A, B or C?"]
story_level_5 = ["Level 5",
                 "The detective from the Orient Express", 
                 "Nun antworte mir: Nun antworte mir",
                 "A: Sherlock Holmes",
                 "B: Miss Marple",
                 "C: Hercule Poirot",
                 "Now give me the answer:",
                 "A, B or C?"]
story_level_6 = ["Level 6", 
                 "",
                 "The murderer in the Rue Morgue was:",
                 "A:     The sailor",
                 "B:     Dupin",
                 "C:     The orangutan",
                 "",
                 "A, B or C?"]
story_level_7 = ["Level 7",
                 "The detective from the Orient Express", 
                 "Nun antworte mir: Nun antworte mir",
                 "A: Sherlock Holmes",
                 "B: Miss Marple",
                 "C: Hercule Poirot",
                 "Now give me the answer:",
                 "A, B or C?"]
story_level_8 = ["Level 8", 
                 "",
                 "The murderer in the Rue Morgue was:",
                 "A:     The sailor",
                 "B:     Dupin",
                 "C:     The orangutan",
                 "",
                 "A, B or C?"]
story_level_9 = ["Level 9",
                 "The detective from the Orient Express", 
                 "Nun antworte mir: Nun antworte mir",
                 "A: Sherlock Holmes",
                 "B: Miss Marple",
                 "C: Hercule Poirot",
                 "Now give me the answer:",
                 "A, B or C?"]
story = [story_level_1, story_level_2, story_level_3, story_level_4, story_level_5, story_level_6, story_level_7, story_level_8, story_level_9]

def quest_menu(level, quest_mana, quest_money):
    background = black
    x_offset = 40
    y_offset = 50
    y_step = 40
    maximum_mana_per_player_quest = 3000
    maximum_money_per_player_quest = 30000
    statuszeile = ""
    screen = backGroundScreen(background)
    been_there_done_that = 0
    done = False
    while not done:
        header = pygame.image.load(os.path.join(os.path.join("tiles"), "quest_image.png")).convert_alpha()
        screen.blit(header,(0,0))
        font = pygame.font.Font(None, 40)
        text_quest_mana = font.render("Mana:"+str(quest_mana), 1, (0, 0, 0))
        text_quest_money = font.render("Money:"+str(quest_money), 1, (0, 0, 0))
        screen.blit(text_quest_mana, (280,10))
        screen.blit(text_quest_money, (450,10))
        for text_line_no in range(8):
            # range(8) = 0..7
            text_single_line = font.render(story[level-1][text_line_no], 1, (0, 0, 0))
            screen.blit(text_single_line, (x_offset,y_offset+text_line_no*y_step))
        text_leave = font.render("Leave: Press L", 1, (0, 0, 0))
        statuszeilenausgabe = font.render(statuszeile, 1, (0, 0, 0))
        screen.blit(statuszeilenausgabe, (40,320))
        screen.blit(text_leave, (40,390))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                # leave quest
                if event.key == pygame.K_l:
                    done = True
                #print "Already done"
                if been_there_done_that == 1: 
                    statuszeile = "Already answered!"
                elif event.key == pygame.K_a:
                    # zu viel Mana nicht erlaubt
                    if quest_mana - 10 >= 0:
                        # zu wenig Geld geht auch nicht
                        if quest_money -200 >= 0:
                            quest_mana = quest_mana - 10
                            quest_money = quest_money - 200
                            been_there_done_that = 1
                            statuszeile = u"Falsch!"
                elif event.key == pygame.K_b:
                    # zu wenig Mana nicht erlaubt
                    if quest_mana - 10 >= 0:
                        # zu wenig Geld geht auch nicht
                        if quest_money -200 >= 0:
                            quest_mana = quest_mana - 10
                            quest_money = quest_money - 200
                            been_there_done_that = 1
                            statuszeile = u"Nein!"
                elif event.key == pygame.K_c:
                    # zu wenig Mana nicht erlaubt
                    if quest_mana + 10 < maximum_mana_per_player_quest:
                        # zu wenig Geld geht auch nicht
                        if quest_money + 200 < maximum_money_per_player_quest:
                            quest_mana = quest_mana + 10
                            quest_money = quest_money + 200
                            been_there_done_that = 1
                            statuszeile = u"Richtig!"
        # END OF for event in ...
    if done == True:
        return (level, quest_mana, quest_money)
                              
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
    global spell_var1
    global spell_var2
    global spell_var3
    spell_var2 = False
    spell_var3 = False
    spell_var1 = False
    spell_type = "fire"
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
    enemy2 = enemy("gegner", 10, 20, 0, 0, (320, 256),pygame.image.load(os.path.join(os.path.join("tiles"), "gegner.png")).convert_alpha(),"fire")    
    enemy1 = enemy("gegner", 10, 20, 0, 0, (256, 256),pygame.image.load(os.path.join(os.path.join("tiles"), "gegner.png")).convert_alpha(),"fire")
    boss = enemy("boss", 30, 200, 3000, 0, (-320,-64), pygame.image.load(os.path.join(os.path.join("tiles"), "endgegner.png")).convert_alpha(),"fire")
    # running = True, game loop
    schritt = 0
    running = True
    while running:
        # run game with 30 frames
        clock.tick(10)
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
                    cash = check_for_cash((player_pos[0],player_pos[1]-32),map)
                    health = check_for_health((player_pos[0],player_pos[1]-32),map)
                    mana = check_for_mana((player_pos[0],player_pos[1]-32),map)
                    sword = check_for_swords((player_pos[0],player_pos[1]-32),map)
                    back = check_for_back((player_pos[0],player_pos[1]-32),map)
                    fireballs = check_for_fireballs((player_pos[0],player_pos[1]-32),map)
                    traps = check_for_trap((player_pos[0],player_pos[1]-32),map)
                    finish = check_for_finish((player_pos[0],player_pos[1]-32),map)
                    warp = check_for_warppoint((player_pos[0],player_pos[1]-32),map)
                    collision = check_for_collision((player_pos[0],player_pos[1]-32),map)
                    quest = check_for_quest((player_pos[0],player_pos[1]-32),map)
                    shopping = check_for_shopping((player_pos[0],player_pos[1]-32),map)
                    interact = check_for_interact((player_pos[0],player_pos[1]-32),map)
                    interact2 = check_for_interact2((player_pos[0],player_pos[1]-32),map)
                    if collision == False:
                        if warp == True:
                            if boss.get_alife() == True:
                                pass
                            elif boss.get_alife() == False:
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
                                if((level/3)%2==1):
                                    enemy1 = enemy("gegner", 10, 20, 0, 0, (256, 256),pygame.image.load(os.path.join(os.path.join("tiles"), "gegner.png")).convert_alpha(),"fire")
                                if((level/3)%2==0):
                                    enemy1 = enemy("gegner", 10, 20, 0, 0, (256, 256),pygame.image.load(os.path.join(os.path.join("tiles"), "gegner2.png")).convert_alpha(),"water")
                                player1.change_position((32,32))
                                enemy1.change_position((320,256))
                                if level == 3 or level == 6 or level ==9:
                                    boss.change_position((320,256))
                                    boss.set_health(200)
                                    boss.set_alife(True)
                                else:
                                    boss.change_position((-320,-64))
                        elif cash == True:
                            player1.set_money(player1.get_money()+100)
                            player1.change_position((player_pos[0],player_pos[1]-32))
                        elif mana == True:
                            player1.set_mana(player1.get_mana()+30)
                            player1.change_position((player_pos[0],player_pos[1]-32))
                        elif health == True:
                            player1.set_health(player1.get_health()+20)
                            player1.change_position((player_pos[0],player_pos[1]-32))
                        elif finish == True:
                            if boss.get_alife() == True:
                                pass
                            elif boss.get_alife() == False:
                                win = pygame.image.load(os.path.join(os.path.join("tiles"), "win.png")).convert_alpha()
                                screen.blit(win,(0,0))
                                pygame.display.flip()
                                time.sleep(3)
                                menu()
                        elif traps == True:
                            fail = pygame.image.load(os.path.join(os.path.join("tiles"), "lost.png")).convert_alpha()
                            screen.blit(fail,(0,0))
                            player1.set_health(100)
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
                                boss.change_position((-320,-320))
                            else:
                                menu()
                        elif back == True:
                            level=level-1
                            map = room.load(os.path.join("data", "level"+ str(level) +".txt"))
                            player1.change_position((32,32))
                            if((level/3)%2==1):
                                enemy1 = enemy("gegner", 10, 20, 0, 0, (256, 256),pygame.image.load(os.path.join(os.path.join("tiles"), "gegner.png")).convert_alpha(),"fire")
                            if((level/3)%2==0):
                                enemy1 = enemy("gegner", 10, 20, 0, 0, (256, 256),pygame.image.load(os.path.join(os.path.join("tiles"), "gegner2.png")).convert_alpha(),"water")
                            enemy1.change_position((320,256))
                        elif interact == True:
                            interact_image = pygame.image.load(os.path.join(os.path.join("tiles"), "interact_image.png")).convert_alpha()
                            screen.blit(interact_image,(0,0))
                            pygame.display.flip()
                            time.sleep(2)
                        elif interact2 == True:
                            interact2_image = pygame.image.load(os.path.join(os.path.join("tiles"), "interact_image2.png")).convert_alpha()
                            screen.blit(interact2_image,(0,0))
                            pygame.display.flip()
                            time.sleep(2)
                        elif quest == True:
                            quest_image = pygame.image.load(os.path.join(os.path.join("tiles"), "quest_image.png")).convert_alpha()
                            screen.blit(quest_image,(0,0))
                            pygame.display.flip()
                            mana = player1.get_mana()
                            money = player1.get_money()
                            font = pygame.font.Font(None, 70)
                            text2 = font.render("Mana:"+str(mana), 1, (255, 255, 255))
                            text3 = font.render("Money:"+str(money), 1, (255, 255, 255))
                            screen.blit(text2, (100,50))
                            screen.blit(text3, (330,50))
                            pygame.display.flip()
                            mana_money_tupel_quest = quest_menu(level, mana, money)
                            player1.set_mana(mana_money_tupel_quest[1])
                            player1.set_money(mana_money_tupel_quest[2])
                           
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
                    cash = check_for_cash((player_pos[0],player_pos[1]+32),map)
                    health = check_for_health((player_pos[0],player_pos[1]+32),map)
                    mana = check_for_mana((player_pos[0],player_pos[1]+32),map)
                    sword = check_for_swords((player_pos[0],player_pos[1]+32),map)
                    back = check_for_back((player_pos[0],player_pos[1]+32),map)
                    fireballs = check_for_fireballs((player_pos[0],player_pos[1]+32),map)
                    traps = check_for_trap((player_pos[0],player_pos[1]+32),map)
                    finish = check_for_finish((player_pos[0],player_pos[1]+32),map)
                    warp = check_for_warppoint((player_pos[0],player_pos[1]+32),map)
                    collision = check_for_collision((player_pos[0],player_pos[1]+32),map)
                    interact = check_for_interact((player_pos[0],player_pos[1]+32),map)
                    interact2 = check_for_interact2((player_pos[0],player_pos[1]+32),map)
                    quest = check_for_quest((player_pos[0],player_pos[1]+32),map)
                    shopping = check_for_shopping((player_pos[0],player_pos[1]+32),map)
                    if collision == False:
                        if warp == True:
                            if boss.get_alife() == True:
                                pass
                            elif boss.get_alife() == False:
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
                                if((level/3)%2==1):
                                    enemy1 = enemy("gegner", 10, 20, 0, 0, (256, 256),pygame.image.load(os.path.join(os.path.join("tiles"), "gegner.png")).convert_alpha(),"fire")
                                if((level/3)%2==0):
                                    enemy1 = enemy("gegner", 10, 20, 0, 0, (256, 256),pygame.image.load(os.path.join(os.path.join("tiles"), "gegner2.png")).convert_alpha(),"water")
                                player1.change_position((32,32))
                                enemy1.change_position((320,256))
                                if level == 3 or level == 6 or level ==9:
                                    boss.change_position((320,256))
                                    boss.set_health(200)
                                    boss.set_alife(True)
                                else:
                                    boss.change_position((-320,-64))
                        elif cash == True:
                            player1.set_money(player1.get_money()+100)
                            player1.change_position((player_pos[0],player_pos[1]+32))
                        elif mana == True:
                            player1.set_mana(player1.get_mana()+30)
                            player1.change_position((player_pos[0],player_pos[1]+32))
                        elif health == True:
                            player1.set_health(player1.get_health()+20)
                            player1.change_position((player_pos[0],player_pos[1]+32))
                        elif finish == True and level == 3:
                            if boss.get_alife() == True:
                                pass
                            elif boss.get_alife() == False:
                                win = pygame.image.load(os.path.join(os.path.join("tiles"), "win.png")).convert_alpha()
                                screen.blit(win,(0,0))
                                pygame.display.flip()
                                time.sleep(3)
                                menu()
                        elif traps == True:
                            fail = pygame.image.load(os.path.join(os.path.join("tiles"), "lost.png")).convert_alpha()
                            screen.blit(fail,(0,0))
                            player1.set_health(100)
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
                                boss.change_position((-320,-320))
                                player1.change_position((32,32))
                                enemy1.change_position((320,256))
                            else:
                                menu()
                        elif back == True:
                            level=level-1
                            map = room.load(os.path.join("data", "level"+ str(level) +".txt"))
                            if((level/3)%2==1):
                                enemy1 = enemy("gegner", 10, 20, 0, 0, (256, 256),pygame.image.load(os.path.join(os.path.join("tiles"), "gegner.png")).convert_alpha(),"fire")
                            if((level/3)%2==0):
                                enemy1 = enemy("gegner", 10, 20, 0, 0, (256, 256),pygame.image.load(os.path.join(os.path.join("tiles"), "gegner2.png")).convert_alpha(),"water")
                            player1.change_position((32,32))
                            enemy1.change_position((320,256))
                        elif interact == True:
                            interact_image = pygame.image.load(os.path.join(os.path.join("tiles"), "interact_image.png")).convert_alpha()
                            screen.blit(interact_image,(0,0))
                            pygame.display.flip()
                            time.sleep(2)
                            map = room.load(os.path.join("data", "level"+ str(level) +".txt"))
                        elif interact2 == True:
                            interact2_image = pygame.image.load(os.path.join(os.path.join("tiles"), "interact_image2.png")).convert_alpha()
                            screen.blit(interact2_image,(0,0))
                            pygame.display.flip()
                            time.sleep(2)
                            map = room.load(os.path.join("data", "level"+ str(level) +".txt"))
                        elif quest == True:
                            quest_image = pygame.image.load(os.path.join(os.path.join("tiles"), "quest_image.png")).convert_alpha()
                            screen.blit(quest_image,(0,0))
                            pygame.display.flip()
                            mana = player1.get_mana()
                            money = player1.get_money()
                            font = pygame.font.Font(None, 70)
                            text2 = font.render("Mana:"+str(mana), 1, (255, 255, 255))
                            text3 = font.render("Money:"+str(money), 1, (255, 255, 255))
                            screen.blit(text2, (100,50))
                            screen.blit(text3, (330,50))
                            pygame.display.flip()
                            mana_money_tupel_quest = quest_menu(level, mana, money)
                            player1.set_mana(mana_money_tupel_quest[1])
                            player1.set_money(mana_money_tupel_quest[2])
                           
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
                    cash = check_for_cash((player_pos[0]-32,player_pos[1]),map)
                    health = check_for_health((player_pos[0]-32,player_pos[1]),map)
                    mana = check_for_mana((player_pos[0]-32,player_pos[1]),map)
                    sword = check_for_swords((player_pos[0]-32,player_pos[1]),map)
                    back = check_for_back((player_pos[0]-32,player_pos[1]),map)
                    fireballs = check_for_fireballs((player_pos[0]-32,player_pos[1]),map)
                    traps = check_for_trap((player_pos[0]-32,player_pos[1]),map)
                    finish = check_for_finish((player_pos[0]-32,player_pos[1]),map)
                    warp = check_for_warppoint((player_pos[0]-32,player_pos[1]),map)
                    collision = check_for_collision((player_pos[0]-32,player_pos[1]),map)
                    interact = check_for_interact((player_pos[0]-32,player_pos[1]),map)
                    interact2 = check_for_interact2((player_pos[0]-32,player_pos[1]),map)
                    quest = check_for_quest((player_pos[0]-32,player_pos[1]),map)
                    shopping = check_for_shopping((player_pos[0]-32,player_pos[1]),map)
                    if collision == False:
                        if warp == True:
                            if boss.get_alife() == True:
                                pass
                            elif boss.get_alife() == False:
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
                                if((level/3)%2==1):
                                    enemy1 = enemy("gegner", 10, 20, 0, 0, (256, 256),pygame.image.load(os.path.join(os.path.join("tiles"), "gegner.png")).convert_alpha(),"fire")
                                if((level/3)%2==0):
                                    enemy1 = enemy("gegner", 10, 20, 0, 0, (256, 256),pygame.image.load(os.path.join(os.path.join("tiles"), "gegner2.png")).convert_alpha(),"water")
                                player1.change_position((32,32))
                                enemy1.change_position((320,256))
                                if level == 3 or level == 6 or level ==9:
                                    boss.change_position((320,256))
                                    boss.set_health(200)
                                    boss.set_alife(True)
                                else:
                                    boss.change_position((-320,-64))
                        elif cash == True:
                            player1.set_money(player1.get_money()+100)
                            player1.change_position((player_pos[0]-32,player_pos[1]))
                        elif mana == True:
                            player1.set_mana(player1.get_mana()+30)
                            player1.change_position((player_pos[0]-32,player_pos[1]))
                        elif health == True:
                            player1.set_health(player1.get_health()+20)
                            player1.change_position((player_pos[0]-32,player_pos[1]))
                        elif finish == True:
                            if boss.get_alife() == True:
                                pass
                            elif boss.get_alife() == False:
                                win = pygame.image.load(os.path.join(os.path.join("tiles"), "win.png")).convert_alpha()
                                screen.blit(win,(0,0))
                                pygame.display.flip()
                                time.sleep(3)
                                menu()
                        elif traps == True:
                            fail = pygame.image.load(os.path.join(os.path.join("tiles"), "lost.png")).convert_alpha()
                            screen.blit(fail,(0,0))
                            player1.set_health(100)
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
                                boss.change_position((-320,-320))
                                player1.change_position((32,32))
                                enemy1.change_position((320,256))
                            else:
                                menu()
                        elif back == True:
                            level=level-1
                            map = room.load(os.path.join("data", "level"+ str(level) +".txt"))
                            if((level/3)%2==1):
                                enemy1 = enemy("gegner", 10, 20, 0, 0, (256, 256),pygame.image.load(os.path.join(os.path.join("tiles"), "gegner.png")).convert_alpha(),"fire")
                            if((level/3)%2==0):
                                enemy1 = enemy("gegner", 10, 20, 0, 0, (256, 256),pygame.image.load(os.path.join(os.path.join("tiles"), "gegner2.png")).convert_alpha(),"water")
                            player1.change_position((32,32))
                            enemy1.change_position((320,256))
                            if level == 3 or level == 6 or level ==9:
                                boss.change_position((320,256))
                                boss.set_health(200)
                            else:
                                boss.change_position((-320,-64))
                        elif interact == True:
                            interact_image = pygame.image.load(os.path.join(os.path.join("tiles"), "interact_image.png")).convert_alpha()
                            screen.blit(interact_image,(0,0))
                            pygame.display.flip()
                            time.sleep(2)
                            map = room.load(os.path.join("data", "level"+ str(level) +".txt"))
                        elif interact2 == True:
                            interact2_image = pygame.image.load(os.path.join(os.path.join("tiles"), "interact_image2.png")).convert_alpha()
                            screen.blit(interact2_image,(0,0))
                            pygame.display.flip()
                            time.sleep(2)
                            map = room.load(os.path.join("data", "level"+ str(level) +".txt"))
                        elif quest == True:
                            quest_image = pygame.image.load(os.path.join(os.path.join("tiles"), "quest_image.png")).convert_alpha()
                            screen.blit(quest_image,(0,0))
                            pygame.display.flip()
                            mana = player1.get_mana()
                            money = player1.get_money()
                            font = pygame.font.Font(None, 70)
                            text2 = font.render("Mana:"+str(mana), 1, (255, 255, 255))
                            text3 = font.render("Money:"+str(money), 1, (255, 255, 255))
                            screen.blit(text2, (100,50))
                            screen.blit(text3, (330,50))
                            pygame.display.flip()
                            mana_money_tupel_quest = quest_menu(level, mana, money)
                            player1.set_mana(mana_money_tupel_quest[1])
                            player1.set_money(mana_money_tupel_quest[2])
                            
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
                    cash = check_for_cash((player_pos[0]+32,player_pos[1]),map)
                    health = check_for_health((player_pos[0]+32,player_pos[1]),map)
                    mana = check_for_mana((player_pos[0]+32,player_pos[1]),map)
                    sword = check_for_swords((player_pos[0]+32,player_pos[1]),map)
                    back = check_for_back((player_pos[0]+32,player_pos[1]),map)
                    fireballs = check_for_fireballs((player_pos[0]+32,player_pos[1]),map)
                    traps = check_for_trap((player_pos[0]+32,player_pos[1]),map)
                    finish = check_for_finish((player_pos[0]+32,player_pos[1]),map)
                    warp = check_for_warppoint((player_pos[0]+32,player_pos[1]),map)
                    collision = check_for_collision((player_pos[0]+32,player_pos[1]),map)
                    interact = check_for_interact((player_pos[0]+32,player_pos[1]),map)
                    interact2 = check_for_interact2((player_pos[0]+32,player_pos[1]),map)
                    quest = check_for_quest((player_pos[0]+32,player_pos[1]),map)
                    shopping = check_for_shopping((player_pos[0]+32,player_pos[1]),map)
                    if collision == False:
                        if warp == True:
                            if boss.get_alife() == True:
                                pass
                            elif boss.get_alife() == False:
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
                                if((level/3)%2==1):
                                    enemy1 = enemy("gegner", 10, 20, 0, 0, (256, 256),pygame.image.load(os.path.join(os.path.join("tiles"), "gegner.png")).convert_alpha(),"fire")
                                if((level/3)%2==0):
                                    enemy1 = enemy("gegner", 10, 20, 0, 0, (256, 256),pygame.image.load(os.path.join(os.path.join("tiles"), "gegner2.png")).convert_alpha(),"water")
                                player1.change_position((32,32))
                                enemy1.change_position((320,256))
                                if level == 3 or level == 6 or level ==9:
                                    boss.change_position((320,256))
                                    boss.set_health(200)
                                    boss.set_alife(True)
                                else:
                                    boss.change_position((-320,-64))
                        elif cash == True:
                            player1.set_money(player1.get_money()+100)
                            player1.change_position((player_pos[0]+32,player_pos[1]))
                        elif mana == True:
                            player1.set_mana(player1.get_mana()+30)
                            player1.change_position((player_pos[0]+32,player_pos[1]))
                        elif health == True:
                            player1.set_health(player1.get_health()+20)
                            player1.change_position((player_pos[0]+32,player_pos[1]))
                        elif finish == True:
                            if boss.get_alife() == True:
                                pass
                            elif boss.get_alife() == False:
                                win = pygame.image.load(os.path.join(os.path.join("tiles"), "win.png")).convert_alpha()
                                screen.blit(win,(0,0))
                                pygame.display.flip()
                                time.sleep(3)
                                menu()
                        elif traps == True:
                            fail = pygame.image.load(os.path.join(os.path.join("tiles"), "lost.png")).convert_alpha()
                            screen.blit(fail,(0,0))
                            player1.set_health(100)
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
                                boss.change_position((-320,-320))
                                player1.change_position((32,32))
                                enemy1.change_position((320,256))
                            else:
                                menu()
                        elif back == True:
                            level=level-1
                            map = room.load(os.path.join("data", "level"+ str(level) +".txt"))
                            if((level/3)%2==1):
                                enemy1 = enemy("gegner", 10, 20, 0, 0, (256, 256),pygame.image.load(os.path.join(os.path.join("tiles"), "gegner.png")).convert_alpha(),"fire")
                            if((level/3)%2==0):
                                enemy1 = enemy("gegner", 10, 20, 0, 0, (256, 256),pygame.image.load(os.path.join(os.path.join("tiles"), "gegner2.png")).convert_alpha(),"water")
                            player1.change_position((32,32))
                            enemy1.change_position((320,256))
                            if level == 3 or level == 6 or level ==9:
                                boss.change_position((320,256))
                                boss.set_health(200)
                            else:
                                boss.change_position((-320,-64))
                        elif interact == True:
                            interact_image = pygame.image.load(os.path.join(os.path.join("tiles"), "interact_image.png")).convert_alpha()
                            screen.blit(interact_image,(0,0))
                            pygame.display.flip()
                            time.sleep(5)
                            map = room.load(os.path.join("data", "level"+ str(level) +".txt"))
                        elif interact2 == True:
                            interact2_image = pygame.image.load(os.path.join(os.path.join("tiles"), "interact_image2.png")).convert_alpha()
                            screen.blit(interact2_image,(0,0))
                            pygame.display.flip()
                            time.sleep(5)
                            map = room.load(os.path.join("data", "level"+ str(level) +".txt"))
                        elif quest == True:
                            quest_image = pygame.image.load(os.path.join(os.path.join("tiles"), "quest_image.png")).convert_alpha()
                            screen.blit(quest_image,(0,0))
                            pygame.display.flip()
                            mana = player1.get_mana()
                            money = player1.get_money()
                            font = pygame.font.Font(None, 70)
                            text2 = font.render("Mana:"+str(mana), 1, (255, 255, 255))
                            text3 = font.render("Money:"+str(money), 1, (255, 255, 255))
                            screen.blit(text2, (100,50))
                            screen.blit(text3, (330,50))
                            pygame.display.flip()
                            mana_money_tupel_quest = quest_menu(level, mana, money)
                            player1.set_mana(mana_money_tupel_quest[1])
                            player1.set_money(mana_money_tupel_quest[2])
                            
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
                elif event.key == pygame.K_1:
                        spell_type = "fire"
                elif event.key == pygame.K_2:
                        spell_type = "water"
                elif event.key == pygame.K_w:
                    mana = player1.get_mana()
                    if mana < 10:
                        pass
                    elif mana >= 10:
                        player1.set_mana(player1.get_mana()-10)
                        
                        spell_pic = player1.launch_spell("UP",spell_type)
                        spell1 = spell(player1.get_position(),"UP",10,spell_pic,spell_type)
                        spell_var1 = True
                
                elif event.key == pygame.K_s:
                    mana = player1.get_mana()
                    if mana < 10:
                        pass
                    elif mana >= 10:
                        player1.set_mana(player1.get_mana()-10)
                        
                        spell_pic = player1.launch_spell("DOWN",spell_type)
                        spell1 = spell(player1.get_position(),"DOWN",10,spell_pic,spell_type)
                        spell_var1 = True
                 
                elif event.key == pygame.K_a:
                    mana = player1.get_mana()
                    if mana < 10:
                        pass
                    elif mana >= 10:
                        player1.set_mana(player1.get_mana()-10)
                        
                        spell_pic = player1.launch_spell("LEFT",spell_type)
                        spell1 = spell(player1.get_position(),"LEFT",10,spell_pic,spell_type)
                        spell_var1 = True
        
                elif event.key == pygame.K_d:
                    mana = player1.get_mana()
                    if mana < 10:
                        pass
                    elif mana >= 10:
                        player1.set_mana(player1.get_mana()-10)
                        
                        spell_pic = player1.launch_spell("RIGHT",spell_type)
                        spell1 = spell(player1.get_position(),"RIGHT",10,spell_pic,spell_type)
                        spell_var1 = True    
        schritt = schritt + 1
        if schritt == 5:
            spell2 = spell(boss.get_position(),"RIGHT",20,pygame.image.load(os.path.join(os.path.join("tiles"), "32x32r.png")).convert_alpha(),"fire")
            spell3 = spell(boss.get_position(),"LEFT",20,pygame.image.load(os.path.join(os.path.join("tiles"), "32x32r.png")).convert_alpha(),"fire")
            spell_var2 = True
            spell_var3 = True
            schritt = 0
        # draw map on screen
        map.draw(screen)
        enemy1.move(map)
        if enemy1.get_position() == player1.get_position():
            damage_manager(enemy1,player1)
            if player1.get_health() <=0 :
                fail = pygame.image.load(os.path.join(os.path.join("tiles"), "lost.png")).convert_alpha()
                screen.blit(fail,(0,0))
                player1.set_health(100)
                pygame.display.flip()
                boss.set_alife(False)
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
        elif enemy1.get_position() == (player1.get_position()[0]+32,player1.get_position()[1]):
            try:
                damage_manager(player1,enemy1)
                screen.blit(enemy1.get_image(),enemy1.get_position())
            except:
                if((level/3)%2==1):
                    enemy1 = enemy("gegner", 10, 20, 0, 0, (256, 256),pygame.image.load(os.path.join(os.path.join("tiles"), "gegner.png")).convert_alpha(),"fire")
                if((level/3)%2==0):
                    enemy1 = enemy("gegner", 10, 20, 0, 0, (256, 256),pygame.image.load(os.path.join(os.path.join("tiles"), "gegner2.png")).convert_alpha(),"water")
                enemy1.change_position((-32,-32))
        if spell_var1 == True:
            spell_var1 = spell1.move(map, player1, enemy1, enemy2, boss)
            if spell_var1 == False:
                del spell1
            elif spell_var1 == True:
                screen.blit(spell1.get_image(), spell1.get_position())
        if spell_var2 == True:
            spell_var2 = spell2.move(map, player1, enemy1, enemy2, boss)
            if spell_var2 == False:
                del spell2
            elif spell_var2 == True:
                screen.blit(spell2.get_image(), spell2.get_position())
        if spell_var3 == True:
            spell_var3 = spell3.move(map, player1, enemy1, enemy2, boss)
            if spell_var3 == False:
                del spell3
            elif spell_var3 == True:
                screen.blit(spell3.get_image(), spell3.get_position())
        if player1.get_health() > 0:
            screen.blit(player1.get_image(),player1.get_position())
        else:
            fail = pygame.image.load(os.path.join(os.path.join("tiles"), "lost.png")).convert_alpha()
            screen.blit(fail,(0,0))
            player1.set_health(100)
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
                boss.change_position((-320,-320))
            else:
                menu()
        if player1.get_position() == boss.get_position() or player1.get_position() == (boss.get_position()[0]+32,boss.get_position()[1]) or player1.get_position() == (boss.get_position()[0],boss.get_position()[1]+32) or player1.get_position() == (boss.get_position()[0]+32,boss.get_position()[1]+32):
            player1.take_damage(40,boss.type)
        
        if enemy1.get_health() <= 0:
            pass
        else:
            screen.blit(enemy1.get_image(), enemy1.get_position())
        if boss.get_health() > 0:
            screen.blit(boss.get_image(),boss.get_position())
            boss.move(map)
        else:
            boss.set_alife(False)
        mana = player1.get_mana()
        health = player1.get_health()
        money = player1.get_money()
        font = pygame.font.Font(None, 36)
        text1 = font.render("Health:"+str(health), 1, (255, 255, 255))
        text2 = font.render("Mana:"+str(mana), 1, (255, 255, 255))
        text3 = font.render("Money:"+str(money), 1, (255, 255, 255))
        text4 = font.render(spell_type, 1, (255, 255, 255))
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
        screen.blit(text4, (600,0))
        pygame.display.flip()
        
def main():
    game()
        
# call main method
if __name__ == "__main__":
    main()
    server = Server()
    server.connect(ip,port)
    server.accepting_allow()
    client = ClassClient(1.0,1.0)
    client.connect(ip,port)
    print()
    
    client.disconnect()
    print()

    server.accepting_disallow()
    server.disconnect_clients()
    server.disconnect()
