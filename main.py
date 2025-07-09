import pygame
from util.sound import Sound
from util.position import Position
import random
import datetime
import time

pygame.init()

# -----------------------------------------------------------------------------------------
# load resources
# -----------------------------------------------------------------------------------------

icon = pygame.image.load("./resources/icon.png")
background = pygame.image.load("./resources/fondoarcade.png")
backblock = pygame.image.load("./resources/back.png")
# Cargar diferentes bloques de colores
block_red = pygame.image.load("./resources/block_red.png")
block_blue = pygame.image.load("./resources/block_blue.png")
block_yellow = pygame.image.load("./resources/block_yellow.png")
# Lista de bloques para fácil acceso
block_colors = [block_red, block_blue, block_yellow]

# -----------------------------------------------------------------------------------------
# set up display
# -----------------------------------------------------------------------------------------

pygame.display.set_icon(icon)
pygame.display.set_caption("PatoBlock Game")
clock = pygame.time.Clock()
screen = pygame.display.set_mode((1261, 663))

# -----------------------------------------------------------------------------------------
# set up game
# -----------------------------------------------------------------------------------------

class GameState:
    """
    Clase para manejar el estado del juego.
    Centraliza las variables de estado en lugar de usar variables globales dispersas.
    """
    def __init__(self):
        self.running = True
        # Set size of blocks
        self.blocks_size = 5
        self.blocks_size_init = 5
        # Set menu initial (0=main, 1=game, 2=game over)
        self.menu = 0
        # Position and movement
        self.position = 0
        self.floor = 0
        self.velocity = 100
        self.i = 0
        # Game state
        self.game_over = False
        self.game_init = False
        # Time management
        self.time_now = datetime.datetime.now()
        self.time_game_over = datetime.datetime.now()
        # Player stats
        self.coins = 0
        # Set matrix of blocks
        self.block_matrix_main = [[random.randint(0, 1) for x in range(19)] for y in range(18)]
        # Create empty game matrix
        self.block_matrix_game = [[0 for x in range(19)] for y in range(18)]
        # Sound state
        self.current_music = None

# Crear instancia del estado del juego
game_state = GameState()

# Variables globales compatibles con el código existente
# Esto facilitará la transición gradual hacia el uso de game_state
running = game_state.running
blocks_size = game_state.blocks_size
blocks_size_init = game_state.blocks_size_init
menu = game_state.menu
block_matrix_main = game_state.block_matrix_main
block_matrix_game = game_state.block_matrix_game
position = game_state.position
floor = game_state.floor
velocity = game_state.velocity
i = game_state.i
game_over = game_state.game_over
time_now = game_state.time_now
time_game_over = game_state.time_game_over
coins = game_state.coins
game_init = game_state.game_init

               
# -----------------------------------------------------------------------------------------
# Menu 0 - main
# -----------------------------------------------------------------------------------------

def scene_main_keyboard():
    """
    Maneja los eventos de teclado en la pantalla principal
    """
    global running, menu, game_over, time_now, time_game_over, coins, game_init, game_state

    # get events of keyboard
    for event in pygame.event.get():
        # when close window
        if event.type == pygame.QUIT:
            running = False
            game_state.running = False
        # when key is pressed
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_2:
                running = False
                game_state.running = False
            elif event.key == pygame.K_1:
                if coins > 0 or game_state.coins > 0:
                    menu = 1
                    game_state.menu = 1
            elif event.key == pygame.K_i:
                coins += 1
                game_state.coins += 1
            elif event.key == pygame.K_3:
                # Mostrar créditos o información del juego
                pass

def draw_scene_main():
    global block_matrix_main, game_over, coins

    screen.blit(background, (0, 0))
    screen.blit(backblock, (318, 54))
    block_matrix_main = [[random.randint(0, 1) for x in range(19)] for y in range(18)]
    draw_blocks_matrix_main()
    font = pygame.font.Font(None, 50)
    txtstart = font.render("1 - Play", True, (255, 255, 0))
    txtexit = font.render("2 - Exit", True, (255, 0, 255))
    txtcredits = font.render("3 - Credits: " + str(coins), True, (0, 0, 255))
    txtinsertcoin = font.render("Insert Coin (Press i)", True, (255, 255, 255))
    screen.blit(txtstart, (550, 150))
    screen.blit(txtexit, (550, 190))
    screen.blit(txtcredits, (550, 230))
    screen.blit(txtinsertcoin, (470, 400))

def reset_game():
    """
    Reinicia todas las variables del juego a sus valores iniciales
    """
    global position, floor, velocity, i, blocks_size, blocks_size_init, game_over

    position = 0
    floor = 0
    velocity = 100
    i = 0
    blocks_size = 5
    blocks_size_init = 5
    game_over = False
    clean_blocks_matrix()

def check_game_over():
    global game_over

    if game_over == True:
        reset_game()

def scene_main(): # menu 0
    """
    Maneja la escena del menú principal
    """
    global game_state
    
    # Reproducir música del menú principal si no está sonando ya
    if game_state.current_music != "main":
        Sound.main_sound(pygame)
        game_state.current_music = "main"
    
    check_game_over()
    scene_main_keyboard()
    draw_scene_main()

# -----------------------------------------------------------------------------------------
# Menu 1 playing game
# -----------------------------------------------------------------------------------------

def move_blocks_matrix():
    """
    Maneja el movimiento de los bloques en la matriz del juego
    Controla la velocidad y posición de los bloques
    """
    global block_matrix_game, position, blocks_size, velocity, game_state, floor, i, blocks_size_init

    # Protección contra índices fuera de rango
    if floor >= 18:
        return
    
    if velocity < 0 and floor < 18:
        if blocks_size > 0:
            # Colocar un nuevo bloque
            block_matrix_game[floor][position] = 1
            game_state.block_matrix_game[floor][position] = 1
            position += 1
            game_state.position += 1
            blocks_size -= 1
            game_state.blocks_size -= 1
        elif position < 19:
            # Mover el bloque horizontalmente
            block_matrix_game[floor][position] = 1
            game_state.block_matrix_game[floor][position] = 1
            
            # Protección contra índices negativos
            if position - blocks_size_init >= 0:
                block_matrix_game[floor][position - blocks_size_init] = 0
                game_state.block_matrix_game[floor][position - blocks_size_init] = 0
                
            position += 1
            game_state.position += 1
        elif position < 19 + blocks_size_init:
            # Borrar bloques al final de la fila
            if position - blocks_size_init >= 0 and position - blocks_size_init < 19:
                block_matrix_game[floor][position - blocks_size_init] = 0
                game_state.block_matrix_game[floor][position - blocks_size_init] = 0
                
            position += 1
            game_state.position += 1
        elif position >= 19 + blocks_size_init:
            # Reiniciar para la siguiente fila
            position = 0
            game_state.position = 0
            blocks_size = blocks_size_init
            game_state.blocks_size = blocks_size_init
            
        # Ajustar la velocidad según el nivel
        velocity = 100 - (i * 6)
        game_state.velocity = velocity
    else:
        velocity -= 10
        game_state.velocity -= 10

def button_return():
    global floor, position, i

    check_blocks()
    position = 0
    floor+=1
    i += 1

def check_blocks():
    """
    Comprueba la alineación de los bloques y actualiza el tamaño de los bloques
    Verifica si el juego ha terminado por no tener más bloques disponibles
    """
    global blocks_size_init, menu, game_over, coins, game_init, game_state, floor

    # Mostrar el tamaño actual de bloques (para depuración)
    font = pygame.font.Font(None, 30)
    txt_blocks = font.render(f"Bloques: {blocks_size_init}", True, (255, 255, 255))
    screen.blit(txt_blocks, (550, 100))
    
    # Verificar la alineación de bloques solo si estamos por encima de la primera fila
    if floor > 0:
        for x in range(0, 19):  # Ajustado el rango a 19 para cubrir toda la matriz
            # Protección contra índices fuera de rango
            if x < len(block_matrix_game[floor]) and x < len(block_matrix_game[floor-1]):
                if block_matrix_game[floor][x] == 1:
                    # Si el bloque no está alineado con un bloque en la fila anterior
                    if block_matrix_game[floor-1][x] != 1:
                        blocks_size_init -= 1
                        game_state.blocks_size_init -= 1
    
    # Verificar si se acabaron los bloques
    if blocks_size_init <= 0:
        blocks_size_init = 0  # Evitar valores negativos
        game_state.blocks_size_init = 0
        game_init = False
        game_state.game_init = False
        game_over = True
        game_state.game_over = True
        menu = 2
        game_state.menu = 2
        if coins > 0:
            coins -= 1
            game_state.coins -= 1


def draw_blocks_matrix_main():
    
    for x in range(0, 18):
        for y in range(0, 19):
            if block_matrix_main[x][y] == 1:
                # Seleccionar un color aleatorio para los bloques en la pantalla principal
                color_index = random.randint(0, len(block_colors) - 1)
                screen.blit(block_colors[color_index], (Position.cal_pos_x(y), Position.cal_pos_y(x)))

def draw_blocks_matrix_game():
    
    for x in range(0, 18):
        for y in range(0, 19):
            if block_matrix_game[x][y] == 1:
                # Siempre usar rojo para los bloques del juego por consistencia
                screen.blit(block_red, (Position.cal_pos_x(y), Position.cal_pos_y(x)))

def clean_blocks_matrix():
    global block_matrix_game

    block_matrix_game = [[0 for x in range(19)] for y in range(18)]


def scene_game_keyboard():
    global running, menu

    # get events of keyboard
    for event in pygame.event.get():
        # when close window
        if event.type == pygame.QUIT:
            running = False
        # when key is pressed
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                menu = 0
            elif event.key == pygame.K_RETURN:
                button_return()

def show_time_down():
    """
    Muestra y gestiona el tiempo restante de la partida
    Termina el juego cuando el tiempo llega a cero
    """
    global time_now, time_game_over, game_over, menu, coins, game_init, game_state

    current_time = datetime.datetime.now()
    time_left = (time_game_over - current_time).total_seconds()
    
    # Garantizar que el tiempo no sea negativo
    if time_left < 0:
        time_left = 0
    
    # Cambiar el color según el tiempo restante
    color = (255, 255, 0)  # Amarillo por defecto
    if time_left < 10:
        # Parpadear en rojo cuando quede poco tiempo
        if int(time_left * 2) % 2 == 0:
            color = (255, 0, 0)  # Rojo
    
    font = pygame.font.Font(None, 50)
    txttime = font.render(f"Tiempo: {int(time_left)}", True, color)
    screen.blit(txttime, (550, 60))
    
    # También mostrar la puntuación (basada en el piso alcanzado)
    txtscore = font.render(f"Nivel: {floor}", True, (0, 255, 0))
    screen.blit(txtscore, (550, 20))
    
    if int(time_left) <= 0:
        menu = 2
        game_state.menu = 2
        game_over = True
        game_state.game_over = True
        game_init = False
        game_state.game_init = False
        if coins > 0:
            coins -= 1
            game_state.coins -= 1

def set_times():
    global time_now, time_game_over, game_init

    if game_init == False:
        time_now = datetime.datetime.now()
        time_game_over = time_now + datetime.timedelta(seconds=51)
        game_init = True

def scene_game(): # menu 1
    """
    Maneja la escena del juego en curso
    """
    global game_state
    
    # Reproducir música del juego si no está sonando ya
    if game_state.current_music != "game":
        Sound.game_sound(pygame)
        game_state.current_music = "game"
    
    # Dibujar primero el fondo principal
    screen.blit(background, (0, 0))
    # Luego dibujar el fondo de los bloques
    screen.blit(backblock, (318, 54))
    set_times()
    move_blocks_matrix()
    draw_blocks_matrix_game()
    scene_game_keyboard()
    show_time_down()
    

# -----------------------------------------------------------------------------------------
# Menu 2 Game Over
# -----------------------------------------------------------------------------------------

def scene_game_over_keyboard():
    global running, menu

    # get events of keyboard
    for event in pygame.event.get():
        # when close window
        if event.type == pygame.QUIT:
            running = False
        # when key is pressed
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                menu = 0

def draw_scene_game_over():
    global game_over

    font = pygame.font.Font(None, 100)
    txtgameover = font.render("Game Over", True, (255, 255, 0))
    screen.blit(txtgameover, (450, 300))
    font = pygame.font.Font(None, 50)
    txtgoback = font.render("Press Esc to go back", True, (255, 255, 0))
    screen.blit(txtgoback, (450, 400))


def scene_game_over(): # menu 2
    """
    Maneja la escena de Game Over
    """
    global game_state
    
    # Reproducir música de game over si no está sonando ya
    if game_state.current_music != "gameover":
        Sound.game_over_sound(pygame)
        game_state.current_music = "gameover"
    
    draw_scene_game_over()
    scene_game_over_keyboard()

# -----------------------------------------------------------------------------------------
# Render
# -----------------------------------------------------------------------------------------
def render():
    """
    Función principal de renderizado que maneja la visualización de diferentes escenas
    según el estado del juego
    """
    global coins, menu, game_state

    # Limpiar pantalla
    screen.fill((0, 0, 0))
    
    # Renderizar la escena apropiada según el menú actual
    if menu == 0:
        scene_main()
    elif menu == 1:
        if coins > 0 or game_state.coins > 0:
            scene_game()
        else:
            menu = 0
            game_state.menu = 0
    elif menu == 2:
        scene_game_over()
    
    # Mostrar FPS para depuración
    fps = clock.get_fps()
    font_small = pygame.font.Font(None, 20)
    fps_text = font_small.render(f"FPS: {int(fps)}", True, (255, 255, 255))
    screen.blit(fps_text, (10, 10))
    
    # Limitar a 60 FPS para un rendimiento consistente
    clock.tick(60)
    
    # Actualizar la pantalla
    pygame.display.flip()

# -------------------------------------------- bucle principal del juego
try:
    while running and game_state.running:
        render()
except Exception as e:
    # Manejo de excepciones para evitar cierres inesperados
    print(f"Error en el juego: {e}")
finally:
    # Asegurar que pygame se cierre correctamente
    pygame.quit()