import pygame
from menu import Menu

def main():
    pygame.init()

    width = 1280
    height = 720

    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Agarpyo")

    menu = Menu(screen)
    menu.run()

    pygame.quit()

if __name__ == '__main__':
    main()
