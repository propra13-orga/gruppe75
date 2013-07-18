''' Dies ist der map  Editor.
 
'''
import pygame
import graphics
import room
import tile
import os
import sys

def map_editor():
    level = 1
    pygame.init()
    pygame.display.set_mode(graphics.screen_size)
    pygame.display.set_caption("Dungeon Crawler")
    pygame.mouse.set_visible(1)
    pygame.key.set_repeat(1, 30)
    clock = pygame.time.Clock()
    tile.init()
    screen = pygame.display.get_surface()
    running = True
    curser_position = (0,0)
    name_sign_dict = {"floor":" ","wall": "#","warp":"+","finish":"-","trap":"T","back":"B","sword":"S","interact":"I","shopping":"G","managain":"M","healthgain":"H","cashgain":"C","quest":"Q","interact2":"L"} 
    name_list = ["floor","wall","warp","finish","trap","back","sword","interact","shopping","managain","healthgain","cashgain","quest","interact2"]
    while running:
        # run game with 10 frames
        clock.tick(10)
        # screen surface black
        screen.fill((0, 0, 0))
        map = room.load(os.path.join("data", "level" + str(level) + ".txt"))
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    sys.exit()
                elif event.key == pygame.K_a:#Levelauswahl
                    if level < 9:
                        level = level + 1
                    else:
                        pass
                elif event.key == pygame.K_z:
                    if level > 1:
                        level = level - 1
                    else:
                        pass
                elif event.key == pygame.K_UP:#cursersteuerung
                    if curser_position[1]-32 < 0:
                        pass
                    elif curser_position[1]-32 > 448:
                        pass
                    else:
                        curser_position = (curser_position[0], curser_position[1]-32)
                
                elif event.key == pygame.K_DOWN:
                    if curser_position[1]+32 < 0:
                        pass
                    elif curser_position[1]+32 > 448:
                        pass
                    else:
                        curser_position = (curser_position[0], curser_position[1]+32)
                
                elif event.key == pygame.K_LEFT:
                    if curser_position[0]-32 < 0:
                        pass
                    elif curser_position[1]-32 > 608:
                        pass
                    else:
                        curser_position = (curser_position[0]-32, curser_position[1])
                        
                elif event.key == pygame.K_RIGHT:
                    if curser_position[0]+32 < 0:
                        pass
                    elif curser_position[0]+32 > 608:
                        pass
                    else:
                        curser_position = (curser_position[0]+32, curser_position[1])
                elif event.key == pygame.K_RETURN:#Aenderung des Spielfelds
                    dict = map.get_coordinates_and_tiles()
                    block = dict[curser_position]
                    name = block.get_name()
                    z = 0
                    for f in range(10):
                        if name == name_list[f]:
                            z = f
                    if z > 8: 
                        z = 0
                    else:
                        z = z + 1
                    file = open(os.path.join("data","level" + str(level) + ".txt"), "w")
                    string = ""
                    for x in range(15):
                        for y in range(20):
                            if (y*tile.width, x*tile.height) == curser_position:
                                string = string + str(name_sign_dict[name_list[z]])
                            else:
                                string = string +  str(name_sign_dict[dict[(y*tile.width, x*tile.height)].get_name()])
                        string = string + "\n"
                    file.write(string)
                    file.close()
                    
        map.draw(screen)
        curser = pygame.image.load(os.path.join(os.path.join("tiles"), "marker.png")).convert_alpha()
        screen.blit(curser,curser_position)
        pygame.display.flip()