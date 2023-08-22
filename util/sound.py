class Sound:

    def main_sound(pygame):
        # load mid
        pygame.mixer.music.load("./resources/musica.mid")
        # change volume
        pygame.mixer.music.set_volume(1.0)
        # play mid once
        pygame.mixer.music.play(1)
        #pygame.mixer.music.play(-1)
        
    def game_sound(pygame):
        # load mid
        pygame.mixer.music.load("./resources/dk-island-swing.mid")
        # change volume
        pygame.mixer.music.set_volume(1.0)
        # play mid once
        pygame.mixer.music.play(1)
        #pygame.mixer.music.play(-1)