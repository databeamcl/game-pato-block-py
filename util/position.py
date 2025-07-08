class Position:
    """
    Clase para gestionar posiciones en la pantalla
    Convierte coordenadas de matriz a coordenadas de pantalla
    """
    # Constantes para el cálculo de posiciones
    BLOCK_SIZE = 32
    BASE_X = 320
    BASE_Y = 600
    
    @staticmethod
    def cal_pos_x(x):
        """
        Calcula la posición X en la pantalla a partir de la coordenada de matriz
        
        Args:
            x: Coordenada X en la matriz
            
        Returns:
            int: Posición X en píxeles
        """
        return (Position.BASE_X + (x * Position.BLOCK_SIZE))

    @staticmethod
    def cal_pos_y(y):
        """
        Calcula la posición Y en la pantalla a partir de la coordenada de matriz
        
        Args:
            y: Coordenada Y en la matriz
            
        Returns:
            int: Posición Y en píxeles
        """
        return (Position.BASE_Y - (y * Position.BLOCK_SIZE))
        
    @staticmethod
    def get_matrix_position(screen_x, screen_y):
        """
        Convierte coordenadas de pantalla a coordenadas de matriz
        Útil para detección de clics en la matriz
        
        Args:
            screen_x: Posición X en la pantalla
            screen_y: Posición Y en la pantalla
            
        Returns:
            tuple: (x, y) posición en la matriz o None si está fuera de la matriz
        """
        # Calcular la posición en la matriz
        matrix_x = (screen_x - Position.BASE_X) // Position.BLOCK_SIZE
        matrix_y = (Position.BASE_Y - screen_y) // Position.BLOCK_SIZE
        
        # Verificar si está dentro de los límites
        if 0 <= matrix_x < 19 and 0 <= matrix_y < 18:
            return (matrix_x, matrix_y)
        return None