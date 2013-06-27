import pygame
import graphics
import room
import tile
import os
import time
import sys
import player
import animation
from player import*
from item import*

# define colors
white = 255,255,255
black = 0,0,0

#  start screen
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


def main():
    pygame.init()
    pygame.display.set_mode(graphics.screen_size)
    pygame.display.set_caption("Dungeon Crawler")
    pygame.mouse.set_visible(1)
    pygame.key.set_repeat(1, 30)
    
    clock = pygame.time.Clock()
    
    player = animation.Animation((32, 32))
  #  player1 = player.Player("player1",fist,none,100,50,1000,[])
    
    
    tile.init()
    map = room.load(os.path.join("data", "level.txt"))
    screen = pygame.display.get_surface()
    
    running = True
    while running:
    
        clock.tick(30)
        screen.fill((0, 0, 0))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
               
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.event.post(pygame.event.Event(pygame.QUIT))
                    
        
        
        map.draw(screen)
        player.handle_event(event)  
        screen.blit(player.image, player.rect)
        
        pygame.display.flip()
        clock.tick(30)
      
if __name__ == "__main__":
    main()
