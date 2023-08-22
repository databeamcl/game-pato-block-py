import pygame
from util.sonido import Sonido
import random

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

blocks_size = 5

# menu
menu = 0

# crear una matriz de 19 x 19 con valor 0  
block_matrix = [[random.randint(0, 1) for x in range(19)] for y in range(18)]


def menu_main():
    # Sonido.main_sound(pygame)
    pygame.display.set_icon(icon)
    pygame.display.set_caption("PatoBlock Game (c)")
    screen.blit(background, (0, 0))
    font = pygame.font.Font(None, 50)
    txtstart = font.render("1 - Star Game", True, (255, 255, 0))
    txtexit = font.render("2 - Exit", True, (255, 0, 255))
    screen.blit(txtstart, (550, 150))
    screen.blit(txtexit, (550, 190))

def menu_game():
    # Sonido.game_sound(pygame)
    screen.blit(backblock, (318, 54))

def update():
    # sleep x seconds
    pygame.time.delay(100)
    #pass

def render():
    if menu == 0:
        menu_main()
    elif menu == 1:
        menu_game()
        draw_blocks_matrix()
    # actualiza la pantalla
    pygame.display.flip()
    # screen.blit(backblock, (318, 54))

def keyboardcontroller(running):
    global menu
    if menu == 0:
        menu_main()
    elif menu == 1:
        menu_game()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_2:
                # running = False
                menu = 0
            elif event.key == pygame.K_1:
                menu = 1
            elif event.key == pygame.K_ESCAPE:
                menu = 0
    return running

def draw_blocks_matrix():
    block_matrix = [[random.randint(0, 1) for x in range(19)] for y in range(18)]
    for x in range(0, 18):
        for y in range(0, 19):
            if block_matrix[x][y] == 1:
                screen.blit(block, (cal_pos_x(y), cal_pos_y(x)))

def move_blocks():
    global block_cursor
    blocks[block_cursor] = 1
    block_cursor += 1

def move_blocks_right():
    pass

def move_blocks_left():
    pass

def cal_pos_x(x):
    x = 320 + (x * 32)
    return x

def cal_pos_y(y):
    y = 600 - (y * 32)
    return y

menu_main()

while running:
    running = keyboardcontroller(running)
    update()
    render()

pygame.quit()