import pygame
from checkbox import Checkbox
from button import Button
from game import Game

class Menu:
    def __init__(self, screen):
        self.screen = screen
        self.game_started = True
        self.background = pygame.image.load("assets/bg.jpg")
        self.font = pygame.font.SysFont('Arial', 40)

        self.checkbox1 = Checkbox(self.screen, 500, 100, caption="Facile", checked=True)
        self.checkbox2 = Checkbox(self.screen, 600, 100, caption="Normale")
        self.checkbox3 = Checkbox(self.screen, 700, 100, caption="Difficile")
        self.checkboxes = [self.checkbox1, self.checkbox2, self.checkbox3]

        self.buttons = [
            Button(450, 200, 400, 80, 'Play With KeyBoard', self.play_game_keyboard),
            Button(450, 300, 400, 80, 'Play With Mouse', self.play_game_mouse),
            Button(450, 600, 400, 80, 'Quit', self.quit_game)
        ]

    def play_game_keyboard(self):
        selected_checkbox = self.get_selected_checkbox()
        if selected_checkbox:
            difficulty = selected_checkbox.caption
            game = Game(self.screen, "Keyboard", difficulty)
            game.run()

    def play_game_mouse(self):
        selected_checkbox = self.get_selected_checkbox()
        if selected_checkbox:
            difficulty = selected_checkbox.caption
            game = Game(self.screen, "Mouse", difficulty)
            game.run()

    def quit_game(self):
        self.game_started = False

    def get_selected_checkbox(self):
        for checkbox in self.checkboxes:
            if checkbox.is_checked():
                return checkbox
        return None

    def process_buttons(self):
        mouse_pos = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        for checkbox in self.checkboxes:
            checkbox.render_checkbox()

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
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p:
                        self.play_game_keyboard()
                    if event.key == pygame.K_q:
                        self.quit_game()
                for checkbox in self.checkboxes:
                    checkbox.update_checkbox(event)

            self.process_buttons()
            pygame.display.update()

