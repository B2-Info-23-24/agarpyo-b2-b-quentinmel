import pygame
import sys
from background import Background
from checkbox import Checkbox
from button import Button

pygame.init()

width = 1280
height = 720
game_started = True

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Agarpyo")
background = Background("assets/bg.jpg", [0,0])
font = pygame.font.SysFont('Arial', 40)

def PlayGame(mode):
    new_screen = pygame.display.set_mode((width, height))
    new_game_started = True
    
    while new_game_started:
        new_screen.fill((255, 255, 255))
        pygame.display.update()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
            if mode == "Keyboard" and event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    print("Key q has been pressed")
                elif event.key == pygame.K_z:
                    print("Key z has been pressed")
                elif event.key == pygame.K_s:
                    print("Key s has been pressed")
                elif event.key == pygame.K_d:
                    print("Key d has been pressed")
                    
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            new_game_started = False
            
        if mode == "Mouse":
            mouse_pos = pygame.mouse.get_pos()
            print(mouse_pos)
        
        pygame.display.update()
                            
def my_function():
    global game_started
    game_started = False

checkbox1 = Checkbox(screen, 500, 100, caption="Facile", checked=True)
checkbox2 = Checkbox(screen, 600, 100, caption="Normale")
checkbox3 = Checkbox(screen, 700, 100, caption="Difficile")

checkboxes = [checkbox1, checkbox2, checkbox3]

buttons = [
    Button(450, 200, 400, 80, 'Play With KeyBoard', lambda: PlayGame("Keyboard")),
    Button(450, 300, 400, 80, 'Play With Mouse', lambda: PlayGame("Mouse")),
    Button(450, 600, 400, 80, 'Quit', my_function)
]

def get_selected_checkbox():
    for checkbox in checkboxes:
        if checkbox.is_checked():
            return checkbox
    return None

def process_buttons():
    mouse_pos = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    checkbox1.render_checkbox()
    checkbox2.render_checkbox()
    checkbox3.render_checkbox()

    for button in buttons:
        button.handle_event(pygame.event.Event(pygame.MOUSEMOTION, {'pos': mouse_pos}))
        if click[0]:
            button.handle_event(pygame.event.Event(pygame.MOUSEBUTTONDOWN, {'button': 1, 'pos': mouse_pos}))
        button.render(screen)

    selected_checkbox = get_selected_checkbox()
    if selected_checkbox:
        print("Checkbox sélectionnée:", selected_checkbox.caption)

def main_menu():
    while game_started:
        screen.fill((255, 255, 255))
        screen.blit(background.image, background.rect)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    print("Key p has been pressed")
                if event.key == pygame.K_q:
                    print("Key q has been pressed")
            checkbox1.update_checkbox(event)
            checkbox2.update_checkbox(event)
            checkbox3.update_checkbox(event)

        process_buttons()

        pygame.display.update()

main_menu()

