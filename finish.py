import pygame
from button import Button

class Finish:
    def __init__(self, screen, score, difficulty, player):
        self.screen = screen
        self.score = score
        self.difficulty = difficulty
        self.player = player
        self.width = 1280
        self.height = 720
        self.game_started = True
        self.background = pygame.image.load("assets/bg.jpg")
        self.buttons = [
            Button(450, 500, 400, 80, 'Return to Menu', self.return_to_menu),
            Button(450, 600, 400, 80, 'Quit', self.quit_function)
        ]

    def process_buttons(self):
        mouse_pos = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        for button in self.buttons:
            button.handle_event(pygame.event.Event(pygame.MOUSEMOTION, {'pos': mouse_pos}))
            if click[0]:
                button.handle_event(pygame.event.Event(pygame.MOUSEBUTTONDOWN, {'button': 1, 'pos': mouse_pos}))
            button.render(self.screen)

    def run(self):
        while self.game_started:
            self.screen.blit(self.background, (0, 0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            self.process_buttons()
            font = pygame.font.SysFont(None, 36)
            stats_text = f"Score: {self.score} | Difficulty: {self.difficulty}"
            stats_surface = font.render(stats_text, True, (255, 255, 255))
            stats_rect = stats_surface.get_rect(center=(self.width // 2, self.height // 2))
            self.screen.blit(stats_surface, stats_rect)
            pygame.display.update()

    def return_to_menu(self):
        self.game_started = False

    pygame.quit()

    def quit_function(self):
        pygame.quit()
        quit()
