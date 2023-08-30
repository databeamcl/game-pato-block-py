import pygame
from util.sound import Sound
import random

pygame.init()

# -----------------------------------------------------------------------------------------
# load resources
# -----------------------------------------------------------------------------------------

icon = pygame.image.load("./resources/icon.png")
background = pygame.image.load("./resources/fondoarcade.png")
backblock = pygame.image.load("./resources/back.png")
block = pygame.image.load("./resources/block_red.png")

# -----------------------------------------------------------------------------------------
# set up
# -----------------------------------------------------------------------------------------

pygame.display.set_icon(icon)
pygame.display.set_caption("PatoBlock Game")
clock = pygame.time.Clock()
running = True
screen = pygame.display.set_mode((1261, 663))
# screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
# set size of blocks
blocks_size = 5
blocks_size_init = 5
blocks_diff = 0
# set menu initial
menu = 0
# set matrix of blocks
block_matrix_main = [[random.randint(0, 1) for x in range(19)] for y in range(18)]
# crear matriz de bloques game con 0
block_matrix_game = [[0 for x in range(19)] for y in range(18)]

position = 0
floor = 0
velocity = 100
i = 0

# -----------------------------------------------------------------------------------------
# Utils
# -----------------------------------------------------------------------------------------

def cal_pos_x(x):
    x = 320 + (x * 32)
    return x

def cal_pos_y(y):
    y = 600 - (y * 32)
    return y

                
# -----------------------------------------------------------------------------------------
# Menu 0
# -----------------------------------------------------------------------------------------

def scene_main(): # menu 0
    global block_matrix_main
    screen.blit(background, (0, 0))
    screen.blit(backblock, (318, 54))
    block_matrix_main = [[random.randint(0, 1) for x in range(19)] for y in range(18)]
    draw_blocks_matrix_main()
    font = pygame.font.Font(None, 50)
    txtstart = font.render("1 - Star Game", True, (255, 255, 0))
    txtexit = font.render("2 - Exit", True, (255, 0, 255))
    screen.blit(txtstart, (550, 150))
    screen.blit(txtexit, (550, 190))    

# -----------------------------------------------------------------------------------------
# Menu 1
# -----------------------------------------------------------------------------------------

def move_blocks_matrix():
    global block_matrix_game
    global position
    global blocks_size
    global velocity

    if velocity < 0 and floor < 18:
        if blocks_size > 0:
            block_matrix_game[floor][position] = 1
            position += 1
            blocks_size -= 1
        elif position < 19:
            block_matrix_game[floor][position] = 1
            block_matrix_game[floor][position - blocks_size_init] = 0
            position += 1
        elif position < 19 + blocks_size_init:
            block_matrix_game[floor][position - blocks_size_init] = 0
            position += 1
        elif position == 19 + blocks_size_init:
            position = 0
            blocks_size = blocks_size_init
        velocity = 100 - (i * 6)
    else:
        velocity -= 10

def button_return():
    global floor
    global position
    global i
    check_blocks()
    position = 0
    floor+=1
    i += 1

def check_blocks():
    global blocks_size_init
    global menu
    if floor > 0:
        for x in range(0, 18):
            if block_matrix_game[floor][x] == 1:
                if block_matrix_game[floor][x] !=  block_matrix_game[floor-1][x]:
                    blocks_size_init -= 1
    if blocks_size_init == 0:
        menu = 2

def draw_blocks_matrix_main():
    for x in range(0, 18):
        for y in range(0, 19):
            if block_matrix_main[x][y] == 1:
                screen.blit(block, (cal_pos_x(y), cal_pos_y(x)))

def draw_blocks_matrix_game():
    for x in range(0, 18):
        for y in range(0, 19):
            if block_matrix_game[x][y] == 1:
                screen.blit(block, (cal_pos_x(y), cal_pos_y(x)))

def clean_blocks_matrix():
    global block_matrix_game
    block_matrix_game = [[0 for x in range(19)] for y in range(18)]

def scene_game(): # menu 1
    screen.blit(backblock, (318, 54))
    move_blocks_matrix()
    draw_blocks_matrix_game() 

# -----------------------------------------------------------------------------------------
# Menu 1
# -----------------------------------------------------------------------------------------

def scene_game_over(): # menu 2
    font = pygame.font.Font(None, 100)
    txtgameover = font.render("Game Over", True, (255, 255, 0))
    screen.blit(txtgameover, (450, 300))

# -----------------------------------------------------------------------------------------
# Render
# -----------------------------------------------------------------------------------------

def keyboardcontroller():
    global running
    global menu

    # get events of keyboard
    for event in pygame.event.get():
        # when close window
        if event.type == pygame.QUIT:
            running = False
        # when key is pressed
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_2:
                running = False
            elif event.key == pygame.K_1:
                menu = 1
            elif event.key == pygame.K_ESCAPE:
                menu = 0
            elif event.key == pygame.K_RETURN:
                button_return()

def render():
    if menu == 0:
        scene_main()
    elif menu == 1:
        scene_game()
    elif menu == 2:
        scene_game_over()
    # update display
    pygame.display.flip()

# -------------------------------------------- start game

while running:
    keyboardcontroller()
    render()

# -------------------------------------------- stop game

pygame.quit()