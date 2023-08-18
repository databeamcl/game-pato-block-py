import pygame

pygame.init()

icon = pygame.image.load("./resources/icon.png")
background = pygame.image.load("./resources/fondoarcade.png")
backblock = pygame.image.load("./resources/back.png")
pygame.display.set_icon(icon)
pygame.display.set_caption("Pato Block Game")


screen = pygame.display.set_mode((1261, 663))
# screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

screen.fill((255, 255, 255))  # Blanco

clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # screen.fill("blue")
    screen.blit(background, (0, 0))
    screen.blit(backblock, (320, 30))
    pygame.display.flip()
    clock.tick(60) 

pygame.quit()


