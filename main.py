import pygame

pygame.init()

icon = pygame.image.load("./resources/icon.png")
background = pygame.image.load("./resources/fondoarcade.png")
backblock = pygame.image.load("./resources/back.png")
pygame.display.set_icon(icon)
pygame.display.set_caption("PatoBlock Game (c)")

block = pygame.image.load("./resources/block.png")

screen = pygame.display.set_mode((1261, 663))
# screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

screen.fill((255, 255, 255))  # Blanco

clock = pygame.time.Clock()
running = True

# cargar un mid
pygame.mixer.music.load("./resources/musica.mid")

# cambair el volumen
pygame.mixer.music.set_volume(0.5)

# reproducir el mid una vez
pygame.mixer.music.play(1)
#pygame.mixer.music.play(-1)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # screen.fill("blue")
    screen.blit(background, (0, 0))
    screen.blit(backblock, (320, 30))
    # screen.blit(block, (400, 60))
    # texto en amarillo tañamo grande
    font = pygame.font.Font(None, 50)
    txtstart = font.render("1 - Jugar", True, (255, 255, 0))
    txtexit = font.render("2 - Salir", True, (255, 0, 255))
    screen.blit(txtstart, (550, 150))
    screen.blit(txtexit, (550, 190))
    pygame.display.flip() # actualiza la pantalla
    clock.tick(30) # limita a 30 fps
    # print(clock.get_fps()) # imprime los fps

pygame.quit()


