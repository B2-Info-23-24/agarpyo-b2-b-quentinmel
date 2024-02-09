import pygame
import math
import random
from circle import Circle

class Player(Circle):
    def __init__(self, x, y, radius, color, obstacle_rects, food_rects):
        Circle.__init__(self, x, y, radius, color)
        valid_position = False
        while not valid_position:
            self.rect = pygame.Rect(x - radius, y - radius, radius * 2, radius * 2)
            if self.rect.collidelist(obstacle_rects) == -1 and self.rect.collidelist(food_rects) == -1:
                valid_position = True
            else:
                x = random.randint(0, 1280)
                y = random.randint(0, 720)
        
    def move_keyboard(self, keys, fps):
        if keys[pygame.K_q]:
            self.rect.x -= 200 / fps
        if keys[pygame.K_d]:
            self.rect.x += 200 / fps
        if keys[pygame.K_z]:
            self.rect.y -= 200 / fps
        if keys[pygame.K_s]:
            self.rect.y += 200 / fps
    
    def move_mouse(self, mouse_pos, fps):
        target_x, target_y = mouse_pos
        dx = target_x - self.rect.centerx
        dy = target_y - self.rect.centery
        distance = math.sqrt(dx ** 2 + dy ** 2)
        if distance != 0:
            speed_factor = min(distance, 200) / distance
            self.rect.x += dx * speed_factor / fps
            self.rect.y += dy * speed_factor / fps


    def move(self, keys, mouse_pos, mode, fps):
        if mode == "Keyboard":
            self.move_keyboard(keys, fps)
        elif mode == "Mouse":
            self.move_mouse(mouse_pos, fps)
