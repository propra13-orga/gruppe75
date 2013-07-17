import pygame
import graphics
import room
import tile
from main import menu
import os
import sys
'''
black = (0,0,0)
white = (255,255,255)

def map_editor_menu():
    pygame.init()
    pygame.display.set_mode(graphics.screen_size)
    pygame.display.set_caption("Dungeon Crawler")
    pygame.mouse.set_visible(1)
    pygame.key.set_repeat(1, 30)
    clock = pygame.time.Clock()
    tile.init()
    screen = pygame.display.get_surface()
    screen1 = screen.get_surface()
    running = True
    while running:
        # run game with 30 frames
        clock.tick(30)
        # screen surface black
        screen.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.event.post(pygame.event.Event(pygame.QUIT))
                elif event.key == pygame.K_RETURN:
                    map_editor()
                elif event.key == pygame.K_BACK:
                    menu()
        
        pygame.display.flip()



def map_editor():
    pygame.init()
    pygame.display.set_mode(graphics.screen_size)
    pygame.display.set_caption("Dungeon Crawler")
    pygame.mouse.set_visible(1)
    pygame.key.set_repeat(1, 30)
    clock = pygame.time.Clock()
    tile.init()
    screen = pygame.display.get_surface()
    running = True
    while running:
        # run game with 30 frames
        clock.tick(30)
        # screen surface black
        screen.fill((0, 0, 0))
        pygame.display.flip()

pygame.init()
pygame.display.set_mode(graphics.screen_size)
pygame.display.set_caption("Dungeon Crawler")
pygame.mouse.set_visible(1)
pygame.key.set_repeat(1, 30)
clock = pygame.time.Clock()
tile.init()
screen = pygame.display.get_surface()
running = True
while running:
    # run game with 30 frames
    clock.tick(30)
    # screen surface black
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.event.post(pygame.event.Event(pygame.QUIT))
            elif event.key == pygame.K_RETURN:
                map_editor()
            elif event.key == pygame.K_BACK:
                menu()
    pygame.display.flip()
'''
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
    liste = [] 
    while running:
        # run game with 30 frames
        clock.tick(10)
        # screen surface black
        screen.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    sys.exit()
                elif event.key == pygame.K_a:
                    if level < 9:
                        level = level + 1
                    else:
                        pass
                elif event.key == pygame.K_z:
                    if level > 1:
                        level = level - 1
                    else:
                        pass
                elif event.key == pygame.K_UP:
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
                elif event.key == pygame.K_ENTER:
                    
        map = room.load(os.path.join("data", "level" + str(level) + ".txt"))
        map.draw(screen)
        curser = pygame.image.load(os.path.join(os.path.join("tiles"), "marker.png")).convert_alpha()
        screen.blit(curser,curser_position)
        pygame.display.flip()
map_editor()