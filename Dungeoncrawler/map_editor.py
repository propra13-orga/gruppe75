import pygame
import graphics
import room
import tile

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
screen1 = screen[]
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
