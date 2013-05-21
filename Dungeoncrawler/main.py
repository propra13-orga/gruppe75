import pygame
import graphics
import room
import tile
import os

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
                    
        
        # draw map on screen
        map.draw(screen)
        
        pygame.display.flip()
        
# call main method
if __name__ == "__main__":
    main()