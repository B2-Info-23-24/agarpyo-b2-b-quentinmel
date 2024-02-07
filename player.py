import pygame

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
        
    def move_keyboard(self, keys):
        if keys[pygame.K_q]:
            self.x -= self.velocity_keyboard
        if keys[pygame.K_d]:
            self.x += self.velocity_keyboard
        if keys[pygame.K_z]:
            self.y -= self.velocity_keyboard
        if keys[pygame.K_s]:
            self.y += self.velocity_keyboard
    
    def move_mouse(self, mouse_pos):
        target_x, target_y = mouse_pos
        dx = target_x - self.x
        dy = target_y - self.y
        distance = max(abs(dx), abs(dy))
        if distance != 0:
            self.x += dx / distance * self.velocity_mouse
            self.y += dy / distance * self.velocity_mouse

    def move(self, keys, mouse_pos, mode):
        if mode == "Keyboard":
            self.move_keyboard(keys)
        elif mode == "Mouse":
            self.move_mouse(mouse_pos)