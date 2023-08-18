import pygame
from util.sonido import Sonido

pygame.init()

# load resources
icon = pygame.image.load("./resources/icon.png")
background = pygame.image.load("./resources/fondoarcade.png")
backblock = pygame.image.load("./resources/back.png")
block = pygame.image.load("./resources/block.png")

# set up
clock = pygame.time.Clock()
running = True
screen = pygame.display.set_mode((1261, 663))
# screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

def menu_main():
    Sonido.main_sound(pygame)
    pygame.display.set_icon(icon)
    pygame.display.set_caption("PatoBlock Game (c)")
    screen.blit(background, (0, 0))
    font = pygame.font.Font(None, 50)
    txtstart = font.render("1 - Jugar", True, (255, 255, 0))
    txtexit = font.render("2 - Salir", True, (255, 0, 255))
    screen.blit(txtstart, (550, 150))
    screen.blit(txtexit, (550, 190))

def menu_game():
    Sonido.game_sound(pygame)
    screen.blit(backblock, (320, 30))

def update():
    pass

def render():
    pygame.display.flip() # actualiza la pantalla
    clock.tick(30) # limita a 30 fps

def keyboardcontroller(running):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_2:
                running = False
            elif event.key == pygame.K_1:
                menu_game()
            elif event.key == pygame.K_ESCAPE:
                menu_main()
    return running

menu_main()

while running:
    running = keyboardcontroller(running)
    update()
    render()

pygame.quit()