class Sonido:

    def main_sound(pygame):
        # cargar un mid
        pygame.mixer.music.load("./resources/musica.mid")
        # cambair el volumen
        pygame.mixer.music.set_volume(0.5)
        # reproducir el mid una vez
        pygame.mixer.music.play(1)
        #pygame.mixer.music.play(-1)
        
    def game_sound(pygame):
        # cargar un mid
        pygame.mixer.music.load("./resources/playing.mid")
        # cambair el volumen
        pygame.mixer.music.set_volume(0.5)
        # reproducir el mid una vez
        pygame.mixer.music.play(1)
        #pygame.mixer.music.play(-1)