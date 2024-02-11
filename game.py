import pygame
from player import Player
from obstacle import Obstacle
from food import Food
from finish import Finish

class Game:
    def __init__(self, screen, mode, difficulty):
        pygame.init()
        self.screen = screen
        self.mode = mode
        self.difficulty = difficulty
        self.width = 1280
        self.height = 720
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 36)
        self.start_time = pygame.time.get_ticks() // 1000
        self.timer = 5
        food_rects = []
        self.obstacle = Obstacle(0, 0, 0, food_rects)
        self.obstacle.createObstacle(self.difficulty, food_rects)
        obstacle_rects = self.obstacle.get_obstacle_rects()
        self.food = Food(0, 0, 0, obstacle_rects)
        self.food.createFood(self.difficulty, obstacle_rects)
        food_rects = self.food.get_food_rects()
        self.player = Player(100, 100, 40, (255, 0, 0), obstacle_rects, food_rects, screen)        

    def run(self):
        pygame.display.set_mode((self.width, self.height))
        new_game_started = True
        fps = 60
        remaining_time = 60

        while new_game_started:
            self.screen.fill((255, 255, 255))
            self.player.draw(self.screen)
            for obs in self.obstacle.obstacles:
                obs.draw(self.screen)
            for food in self.food.foods:
                food.draw(self.screen)
                
            text = f"Vitesse: {self.player.speed} | Score: {self.player.score} | Taille: {self.player.radius} | Difficulté: {self.difficulty}"
            text_surface = self.font.render(text, True, (0, 0, 0))
            text_rect = text_surface.get_rect(topleft=(11, 11))
            self.screen.blit(text_surface, text_rect)
            text_surface = self.font.render(text, True, (255, 255, 255))
            self.screen.blit(text_surface, text_rect.move(-2, -2)) 
            
            current_time = pygame.time.get_ticks() // 1000
            elapsed_time = current_time - self.start_time
            remaining_time = max(self.timer - elapsed_time, 0)
            timer_text = f"Temps: {remaining_time} s"
            timer_text_surface = self.font.render(timer_text, True, (0, 0, 0))
            timer_text_rect = timer_text_surface.get_rect(topright=(self.width - 11, 11))
            self.screen.blit(timer_text_surface, timer_text_rect)
            timer_text_surface = self.font.render(timer_text, True, (255, 255, 255))
            self.screen.blit(timer_text_surface, timer_text_rect.move(-1, -1))
            
            pygame.display.update()

            keys = pygame.key.get_pressed()
            if keys[pygame.K_ESCAPE]:
                new_game_started = False
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

            if self.obstacle.collide(self.player):
                obstacle_touche = self.obstacle.collide(self.player)
                if obstacle_touche:
                    if self.player.radius > obstacle_touche.radius:
                        distance = obstacle_touche.get_distance_to_player(self.player)
                        if distance <= self.player.radius + obstacle_touche.radius:
                            self.obstacle.obstacles.remove(obstacle_touche)
                            self.obstacle.add_new_obstacle(self.food.get_food_rects())
                            self.player.decrease_size_and_speed(self.difficulty, obstacle_touche.radius)

            if self.food.collide(self.player, self.obstacle.obstacles):
                self.player.increase_speed(5)
                self.player.increase_size(2)
                self.player.score += 1

            self.player.move(keys, pygame.mouse.get_pos(), self.mode, fps)
            self.clock.tick(fps)
            pygame.display.update()

            if remaining_time == 0:
                new_game_started = False
                finish = Finish(self.screen, self.player.score, self.difficulty, self.player)
                finish.run()              