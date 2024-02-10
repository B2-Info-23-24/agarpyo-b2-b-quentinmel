import math
import pygame
import random
from circle import Circle

class Obstacle(Circle):
    def __init__(self, x, y, radius, food_rects):
        Circle.__init__(self, x, y, radius, (0, 0, 0))
        self.obstacles = []
        valid_position = False
        self.radius = radius
        while not valid_position:
            self.rect = pygame.Rect(x - radius, y - radius, radius * 2, radius * 2)
            if self.rect.collidelist(food_rects) == -1:
                valid_position = True
            else:
                x = random.randint(0, 1280)
                y = random.randint(0, 720)
        
    def createObstacle(self, difficulty, food_rects):
        self.obstacles.clear()
        
        if difficulty == "Facile":
            for i in range(2):
                x = random.randint(0, 1280)
                y = random.randint(0, 720)
                radius = random.randint(40, 150)
                new_obstacle = Obstacle(x, y, radius, food_rects)
                self.obstacles.append(new_obstacle)
        elif difficulty == "Normale":
            for i in range(3):
                x = random.randint(0, 1280)
                y = random.randint(0, 720)
                radius = random.randint(40, 150)
                new_obstacle = Obstacle(x, y, radius, food_rects)
                self.obstacles.append(new_obstacle)
        elif difficulty == "Difficile":
            for i in range(4):
                x = random.randint(0, 1280)
                y = random.randint(0, 720)
                radius = random.randint(40, 150)
                new_obstacle = Obstacle(x, y, radius, food_rects)
                self.obstacles.append(new_obstacle)
    
    def get_obstacle_rects(self):
        rects = []
        for obs in self.obstacles:
            rects.append(obs.rect)
        return rects
    
    def collide(self, player):
        for obs in self.obstacles:
            if obs.rect.colliderect(player.rect):
                return obs
        return None
    
    def add_new_obstacle(self, food_rects):
        valid_position = False
        while not valid_position:
            x = random.randint(0, 1280)
            y = random.randint(0, 720)
            radius = random.randint(40, 150)
            new_obstacle_rect = pygame.Rect(x - radius, y - radius, radius * 2, radius * 2)
            overlap = False
            for obs in self.obstacles:
                if new_obstacle_rect.colliderect(obs.rect):
                    overlap = True
                    break
            if not overlap:
                for food_rect in food_rects:
                    if new_obstacle_rect.colliderect(food_rect):
                        overlap = True
                        break
            if not overlap:
                valid_position = True
        new_obstacle = Obstacle(x, y, radius, food_rects)
        self.obstacles.append(new_obstacle)
    
    def get_obstacle_touche(self, player, player_radius):
            for obs in self.obstacles:
                if obs.rect.colliderect(player.rect) and player_radius > self.radius:
                    return True
            return False
    
    def update_obstacle(self, food_rects):
        for obs in self.obstacles:
            if obs.rect.collidelist(food_rects) != -1:
                self.obstacles.remove(obs)
                self.add_new_obstacle(food_rects)
    
    def get_distance_to_player(self, player):
        distance = math.sqrt((self.rect.centerx - player.rect.centerx)**2 + (self.rect.centery - player.rect.centery)**2)
        return distance