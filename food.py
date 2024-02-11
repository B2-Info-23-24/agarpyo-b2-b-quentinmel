import pygame
from circle import Circle
import random

class Food(Circle):
    def __init__(self, x, y, radius, obstacle_rects):
        Circle.__init__(self, x, y, radius, (0, 255, 0))
        self.foods = []
        valid_position = False
        while not valid_position:
            self.rect = pygame.Rect(x - radius, y - radius, radius * 2, radius * 2)
            if self.rect.collidelist(obstacle_rects) == -1:
                valid_position = True
            else:
                x = random.randint(0, 1280)
                y = random.randint(0, 720)
        
    def create_food(self, difficulty, obstacle_rects):
        self.foods.clear()
        
        if difficulty == "Easy":
            for i in range(5):
                x = random.randint(0, 1280)
                y = random.randint(0, 720)
                radius = random.randint(10, 20)
                new_food = Food(x, y, radius, obstacle_rects)
                self.foods.append(new_food)
        elif difficulty == "Normal":
            for i in range(3):
                x = random.randint(0, 1280)
                y = random.randint(0, 720)
                radius = random.randint(10, 20)
                new_food = Food(x, y, radius, obstacle_rects)
                self.foods.append(new_food)
        elif difficulty == "Hard":
            for i in range(2):
                x = random.randint(0, 1280)
                y = random.randint(0, 720)
                radius = random.randint(10, 20)
                new_food = Food(x, y, radius, obstacle_rects)
                self.foods.append(new_food)
    
    def get_food_rects(self):
        rects = []
        for food in self.foods:
            rects.append(food.rect)
        return rects

    def collide(self, player, obstacle_rects):
        for food in self.foods:
            if food.rect.colliderect(player.rect):
                self.foods.remove(food)
                self.add_new_food(obstacle_rects)
                return True
        return False

    def add_new_food(self, obstacle_rects):
        valid_position = False
        while not valid_position: 
            x = random.randint(0, 1280)
            y = random.randint(0, 720)
            radius = random.randint(10, 20)
            new_food_rect = pygame.Rect(x - radius, y - radius, radius * 2, radius * 2)
            overlap = False
            for obs in obstacle_rects:
                if new_food_rect.colliderect(obs.rect):
                    overlap = True
                    break
            if not overlap:
                for obstacle_rect in obstacle_rects:
                    if new_food_rect.colliderect(obstacle_rect):
                        overlap = True
                        break
            if not overlap:
                valid_position = True
        new_food = Food(x, y, radius, obstacle_rects)
        self.foods.append(new_food)
            
        
