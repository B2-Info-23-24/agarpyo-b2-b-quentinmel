import pygame
from player import Player
from obstacle import Obstacle
from food import Food

class Game:
    def __init__(self, screen, mode, difficulty):
        pygame.init()
        self.screen = screen
        self.mode = mode
        self.difficulty = difficulty
        self.width = 1280
        self.height = 720
        self.clock = pygame.time.Clock()
        food_rects = []
        self.obstacle = Obstacle(0, 0, 0, food_rects)
        self.obstacle.createObstacle(self.difficulty, food_rects)
        obstacle_rects = self.obstacle.get_obstacle_rects()
        self.food = Food(0, 0, 0, obstacle_rects)
        self.food.createFood(self.difficulty, obstacle_rects)
        food_rects = self.food.get_food_rects()
        self.player = Player(50, 50, 25, (255, 0, 0), obstacle_rects, food_rects)

    def run(self):
        pygame.display.set_mode((self.width, self.height))
        new_game_started = True
        FPS = 60

        while new_game_started:
            self.screen.fill((255, 255, 255))
            self.player.draw(self.screen)
            for obs in self.obstacle.obstacles:
                obs.draw(self.screen)
            for food in self.food.foods:
                food.draw(self.screen)
            pygame.display.update()

            keys = pygame.key.get_pressed()
            if keys[pygame.K_ESCAPE]:
                new_game_started = False

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

            if self.obstacle.collide(self.player, self.food.foods):
                print("Collision Obstacle")
            if self.food.collide(self.player, self.obstacle.obstacles):
                print("Food Collision")

            self.player.move(keys, pygame.mouse.get_pos(), self.mode, fps=FPS)
            self.clock.tick(FPS)
            pygame.display.update()
