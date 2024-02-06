import pygame

class Checkbox:
    checkboxes = []

    def __init__(self, surface, x, y, caption="", font_size=22, font_color=(0, 0, 0), text_offset=(28, 1), checked=False):
        self.surface = surface
        self.x = x
        self.y = y
        self.caption = caption
        self.font_size = font_size
        self.font_color = font_color
        self.text_offset = text_offset
        self.checkbox_obj = pygame.Rect(self.x, self.y, 12, 12)
        self.checked = checked
        Checkbox.checkboxes.append(self)

    def _draw_button_text(self):
        font = pygame.font.Font(None, self.font_size)
        font_surf = font.render(self.caption, True, self.font_color)
        font_pos = (self.x + self.text_offset[0], 
                    self.y + 12 / 2 - font_surf.get_height() / 2 + self.text_offset[1])
        self.surface.blit(font_surf, font_pos)

    def render_checkbox(self):
        pygame.draw.rect(self.surface, (230, 230, 230), self.checkbox_obj)
        pygame.draw.rect(self.surface, (0, 0, 0), self.checkbox_obj, 1)
        if self.checked:
            pygame.draw.circle(self.surface, (0, 0, 0), (self.x + 6, self.y + 6), 4)
        self._draw_button_text()

    def update_checkbox(self, event_object):
        if event_object.type == pygame.MOUSEBUTTONDOWN:
            if self.checkbox_obj.collidepoint(event_object.pos):
                for checkbox in Checkbox.checkboxes:
                    checkbox.checked = False
                self.checked = True

    def is_checked(self):
        return self.checked
