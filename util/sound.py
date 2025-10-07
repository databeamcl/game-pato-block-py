class Sound:
    """
    Clase para gestionar la reproducción de sonidos en el juego
    """
    # Variables de estado para el control de sonido
    current_music = None
    muted = False
    volume = 1.0

    @staticmethod
    def main_sound(pygame):
        """
        Reproduce la música del menú principal
        
        Args:
            pygame: Instancia de pygame para acceder a las funciones de sonido
        """
        # Evitar reproducir la misma música repetidamente
        if Sound.current_music == "main":
            return
            
        try:
            pygame.mixer.music.fadeout(500)  # Fade out de música anterior
            pygame.mixer.music.load("./resources/musica.mid")
            pygame.mixer.music.set_volume(Sound.volume)
            pygame.mixer.music.play(-1)  # Reproducir en bucle
            Sound.current_music = "main"
        except Exception as e:
            print(f"Error al reproducir sonido del menú: {e}")
        
    @staticmethod
    def game_sound(pygame):
        """
        Reproduce la música durante el juego
        
        Args:
            pygame: Instancia de pygame para acceder a las funciones de sonido
        """
        # Evitar reproducir la misma música repetidamente
        if Sound.current_music == "game":
            return
            
        try:
            pygame.mixer.music.fadeout(500)  # Fade out de música anterior
            pygame.mixer.music.load("./resources/dk-island-swing.mid")
            pygame.mixer.music.set_volume(Sound.volume)
            pygame.mixer.music.play(-1)  # Reproducir en bucle
            Sound.current_music = "game"
        except Exception as e:
            print(f"Error al reproducir sonido del juego: {e}")
            
    @staticmethod
    def game_over_sound(pygame):
        """
        Reproduce sonido para la pantalla de game over
        
        Args:
            pygame: Instancia de pygame para acceder a las funciones de sonido
        """
        if Sound.current_music == "gameover":
            return
            
        try:
            pygame.mixer.music.fadeout(500)  # Fade out de música anterior
            pygame.mixer.music.load("./resources/playing.mid")
            pygame.mixer.music.set_volume(Sound.volume)
            pygame.mixer.music.play(1)  # Reproducir una vez
            Sound.current_music = "gameover"
        except Exception as e:
            print(f"Error al reproducir sonido de game over: {e}")
    
    @staticmethod
    def toggle_mute(pygame):
        """
        Activa o desactiva el sonido
        
        Args:
            pygame: Instancia de pygame para acceder a las funciones de sonido
        """
        Sound.muted = not Sound.muted
        if Sound.muted:
            pygame.mixer.music.set_volume(0.0)
        else:
            pygame.mixer.music.set_volume(Sound.volume)
            
    @staticmethod
    def set_volume(pygame, volume):
        """
        Establece el volumen de la música
        
        Args:
            pygame: Instancia de pygame para acceder a las funciones de sonido
            volume: Nivel de volumen (0.0 a 1.0)
        """
        Sound.volume = max(0.0, min(1.0, volume))  # Limitar entre 0 y 1
        if not Sound.muted:
            pygame.mixer.music.set_volume(Sound.volume)