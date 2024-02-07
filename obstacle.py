import pygame

class Obstacle(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([radius*2, radius*2])
        self.image.fill((0, 0, 0, 0))
        pygame.draw.circle(self.image, (0, 0, 0), (radius, radius), radius)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.radius = radius

    def draw(self, screen):
        screen.blit(self.image, self.rect)
        
    def collide(self, sprite):
        return pygame.sprite.collide_circle(self, sprite)
