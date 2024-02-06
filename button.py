import pygame

class Button():
    buttons = []

    def __init__(self, x, y, width, height, buttonText='Button', onclickFunction=None, onePress=False):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.buttonText = buttonText
        self.onclickFunction = onclickFunction
        self.onePress = onePress
        self.alreadyPressed = False

        self.fillColors = {
            'normal': (255, 255, 255),
            'hover': (102, 102, 102),
            'pressed': (51, 51, 51),
        }
        self.state = 'normal'

        self.buttonSurface = pygame.Surface((self.width, self.height))
        self.buttonSurface.fill(self.fillColors[self.state])
        self.buttonRect = self.buttonSurface.get_rect(topleft=(self.x, self.y))

        self.font = pygame.font.SysFont(None, 24)
        self.textSurf = self.font.render(self.buttonText, True, (0, 0, 0))  # Noir

        Button.buttons.append(self)

    def render(self, screen):
        screen.blit(self.buttonSurface, self.buttonRect)
        text_rect = self.textSurf.get_rect(center=self.buttonRect.center)
        screen.blit(self.textSurf, text_rect)

    def handle_event(self, event):
        if event.type == pygame.MOUSEMOTION:
            self.handle_mouse_motion(event.pos)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                self.handle_mouse_click(event.pos)

    def handle_mouse_motion(self, mouse_pos):
        if self.buttonRect.collidepoint(mouse_pos):
            self.state = 'hover'
        else:
            self.state = 'normal'
        self.buttonSurface.fill(self.fillColors[self.state])

    def handle_mouse_click(self, mouse_pos):
        if self.buttonRect.collidepoint(mouse_pos):
            if self.onclickFunction:
                self.onclickFunction()
                if self.onePress:
                    self.alreadyPressed = True
