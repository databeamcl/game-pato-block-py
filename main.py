import pygame
from util.sound import Sound
import random

pygame.init()

# -------------------------------------------- load resources

icon = pygame.image.load("./resources/icon.png")
background = pygame.image.load("./resources/fondoarcade.png")
backblock = pygame.image.load("./resources/back.png")
block = pygame.image.load("./resources/block_red.png")

# -------------------------------------------- set up

pygame.display.set_icon(icon)
pygame.display.set_caption("PatoBlock Game")
clock = pygame.time.Clock()
running = True
screen = pygame.display.set_mode((1261, 663))
# screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
# set size of blocks
blocks_size = 5
# set menu initial
menu = 0
# set matrix of blocks
block_matrix_main = [[random.randint(0, 1) for x in range(19)] for y in range(18)]
# crear matriz de bloques game con 0
block_matrix_game = [[0 for x in range(19)] for y in range(18)]

position = 0

# -------------------------------------------- screen stage

def cal_pos_x(x):
    x = 320 + (x * 32)
    return x

def cal_pos_y(y):
    y = 600 - (y * 32)
    return y

def screen_main():
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

def move_blocks_matrix():
    global block_matrix_game
    global position
    if position < 19:
        block_matrix_game[0][position] = 1
        position += 1


def screen_game():
    screen.blit(backblock, (318, 54))
    move_blocks_matrix()
    draw_blocks_matrix_game() 


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

# -------------------------------------------- render stage

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

def update():
    pass

def render():
    if menu == 0:
        screen_main()
    elif menu == 1:
        screen_game()
    # update display
    # pygame.time.delay(10)
    clock.tick(60)
    #print(clock.get_fps())
    pygame.display.flip()

# -------------------------------------------- start game

while running:
    keyboardcontroller()
    update()
    render()

# -------------------------------------------- stop game

pygame.quit()