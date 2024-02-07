import sys
import pygame

width = 1280
height = 720

def PlayGame(mode):
    new_screen = pygame.display.set_mode((width, height))
    new_game_started = True
    
    while new_game_started:
        new_screen.fill((255, 255, 255))
        pygame.display.update()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
            if mode == "Keyboard" and event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    print("Key q has been pressed")
                elif event.key == pygame.K_z:
                    print("Key z has been pressed")
                elif event.key == pygame.K_s:
                    print("Key s has been pressed")
                elif event.key == pygame.K_d:
                    print("Key d has been pressed")
                    
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            new_game_started = False
            
        if mode == "Mouse":
            mouse_pos = pygame.mouse.get_pos()
            print(mouse_pos)
        
        pygame.display.update()