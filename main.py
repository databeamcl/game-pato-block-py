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

blocks_size = 5
blocks = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

# crear una matriz de 19 x 19 con valor 0  
block_matrix = [[1 for x in range(19)] for y in range(10)]

print(block_matrix)


block_start = 0
block_end = 18
block_cursor = 0

def menu_main():
    # Sonido.main_sound(pygame)
    pygame.display.set_icon(icon)
    pygame.display.set_caption("PatoBlock Game (c)")
    screen.blit(background, (0, 0))
    font = pygame.font.Font(None, 50)
    txtstart = font.render("1 - Jugar", True, (255, 255, 0))
    txtexit = font.render("2 - Salir", True, (255, 0, 255))
    screen.blit(txtstart, (550, 150))
    screen.blit(txtexit, (550, 190))

def menu_game():
    # Sonido.game_sound(pygame)
    screen.blit(backblock, (320, 30))

def update():
    # sleep 1 second
    # move_blocks()
    pygame.time.delay(500)

def render():
    draw_blocks_matrix()
    # draw_blocks()
    pygame.display.flip() # actualiza la pantalla
    # clock.tick(60) # limita a 30 fps

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

def draw_blocks():
    for i in range(0, 19): # 0 - 18
      if blocks[i] == 1:
            screen.blit(block, (320 + (i * 32), 600))

def draw_blocks_matrix():
    # for row in range(len(blocks)):
    #     for col in range(len(blocks[row])):
    #         if blocks[row][col] == 1:
    #             screen.blit(block, (320 + (col * 32), 600 + (row * 32)))
    # for i in range(len(blocks_matrix)) :
    #     if blocks[i] == 1:
    #         screen.blit(block, (320 + (i * 32), 600))
    pass

def move_blocks():
    global block_cursor
    blocks[block_cursor] = 1
    block_cursor += 1
    print(blocks)

def move_blocks_right():
    pass

def move_blocks_left():
    pass

menu_main()

while running:
    running = keyboardcontroller(running)
    update()
    render()

pygame.quit()