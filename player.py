import pygame

class Player:
    def __init__(self, x, y, radius, color):
        self.rect = pygame.Rect(x - radius, y - radius, radius * 2, radius * 2)
        self.color = color
        self.velocity_keyboard = 5
        self.velocity_mouse = 2

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, self.rect.center, self.rect.width // 2)
        
    def move_keyboard(self, keys):
        if keys[pygame.K_q]:
            self.rect.x -= self.velocity_keyboard
        if keys[pygame.K_d]:
            self.rect.x += self.velocity_keyboard
        if keys[pygame.K_z]:
            self.rect.y -= self.velocity_keyboard
        if keys[pygame.K_s]:
            self.rect.y += self.velocity_keyboard
    
    def move_mouse(self, mouse_pos):
        target_x, target_y = mouse_pos
        dx = target_x - self.rect.centerx
        dy = target_y - self.rect.centery
        distance = max(abs(dx), abs(dy))
        if distance != 0:
            self.rect.x += dx / distance * self.velocity_mouse
            self.rect.y += dy / distance * self.velocity_mouse

    def move(self, keys, mouse_pos, mode):
        if mode == "Keyboard":
            self.move_keyboard(keys)
        elif mode == "Mouse":
            self.move_mouse(mouse_pos)
