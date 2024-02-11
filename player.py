import pygame
import math
import random
from circle import Circle

class Player(Circle):
    def __init__(self, x, y, radius, color, obstacle_rects, food_rects, screen):
        Circle.__init__(self, x, y, radius, color)
        self.speed = 100
        self.radius = radius
        valid_position = False
        self.score = 0
        self.update_rect()
        self.screen = screen
        while not valid_position:
            if self.rect.collidelist(obstacle_rects) == -1 and self.rect.collidelist(food_rects) == -1:
                valid_position = True
            else:
                x = random.randint(0, 1200)
                y = random.randint(0, 680)
                self.update_rect(x, y)
        
    def move_keyboard(self, keys, fps):
        if keys[pygame.K_q]:
            self.rect.x -= self.speed / fps
            if self.rect.right < 0:
                self.rect.x = self.screen.get_width()
        if keys[pygame.K_d]:
            self.rect.x += self.speed / fps
            if self.rect.left > self.screen.get_width():
                self.rect.x = -self.rect.width
        if keys[pygame.K_z]:
            self.rect.y -= self.speed / fps
            if self.rect.bottom < 0:
                self.rect.y = self.screen.get_height()
        if keys[pygame.K_s]:
            self.rect.y += self.speed / fps
            if self.rect.top > self.screen.get_height():
                self.rect.y = -self.rect.height
                
    def move_mouse(self, mouse_pos, fps):
        target_x, target_y = mouse_pos
        dx = target_x - self.rect.centerx
        dy = target_y - self.rect.centery
        distance = math.sqrt(dx ** 2 + dy ** 2)
        
        if distance != 0:
            direction_x = dx / distance
            direction_y = dy / distance
        else:
            direction_x, direction_y = 0, 0

        if self.rect.left < 0:
            self.rect.right = self.screen.get_width()
        elif self.rect.right > self.screen.get_width():
            self.rect.left = 0
        if self.rect.top < 0:
            self.rect.bottom = self.screen.get_height()
        elif self.rect.bottom > self.screen.get_height():
            self.rect.top = 0

        self.rect.x += direction_x * self.speed / fps
        self.rect.y += direction_y * self.speed / fps


    def move(self, keys, mouse_pos, mode, fps):
        if mode == "Keyboard":
            self.move_keyboard(keys, fps)
        elif mode == "Mouse":
            self.move_mouse(mouse_pos, fps)

    def draw(self, screen):
            pygame.draw.circle(screen, self.color, self.rect.center, self.radius)
        
    def increase_speed(self, amount):
        if self.speed <= 500:
            self.speed += amount
    
    def update_rect(self, x=None, y=None):
        if x is None:
            x = self.rect.x
        if y is None:
            y = self.rect.y
        self.rect = pygame.Rect(x - self.radius, y - self.radius, self.radius * 2, self.radius * 2)

    def increase_size(self, amount):
        if self.radius <= 200:
            self.radius += amount
            old_center = self.rect.center
            self.update_rect()
            self.rect.center = old_center
    
    def decrease_size_and_speed(self, difficulty, obstacle_radius):
        if obstacle_radius < self.radius:
            if difficulty == "Facile":
                factor = 2
            elif difficulty == "Normal":
                factor = 3
            elif difficulty == "Difficile":
                factor = 4
                
            self.radius //= factor
            self.speed //= factor
            self.update_rect()
