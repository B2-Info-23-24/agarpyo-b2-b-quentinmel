import sys
import pygame

width = 1280
height = 720

class Player:
    def __init__(self, x, y, radius, color):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.velocity_keyboard = 5
        self.velocity_mouse = 2

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)

    def move(self, keys, mouse_pos, mode):
        if mode == "Keyboard":
            if keys[pygame.K_q]:
                self.x -= self.velocity_keyboard
            if keys[pygame.K_d]:
                self.x += self.velocity_keyboard
            if keys[pygame.K_z]:
                self.y -= self.velocity_keyboard
            if keys[pygame.K_s]:
                self.y += self.velocity_keyboard
        elif mode == "Mouse":
            target_x, target_y = mouse_pos
            dx = target_x - self.x
            dy = target_y - self.y
            distance = max(abs(dx), abs(dy))
            if distance != 0:
                self.x += dx / distance * self.velocity_mouse
                self.y += dy / distance * self.velocity_mouse
    

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
                sys.exit()
                
            player.move(keys, mouse_pos, mode)
        
        pygame.display.update()