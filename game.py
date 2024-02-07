import pygame
from player import Player

width = 1280
height = 720
    
clock = pygame.time.Clock()

player = Player(50, 50, 25, (255, 0, 0))

def PlayGame(mode):
    new_screen = pygame.display.set_mode((width, height))
    new_game_started = True
    
    while new_game_started:
        new_screen.fill((255, 255, 255))
        player.draw(new_screen)
        pygame.display.update()
        
        mouse_pos = pygame.mouse.get_pos()
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_ESCAPE]:
                    new_game_started = False
                    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                
            player.move(keys, mouse_pos, mode)
        
        pygame.display.update()