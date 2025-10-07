# Changelog de PatoBlock Game

Todas las modificaciones notables a este proyecto serán documentadas en este archivo.

## [1.2.0] - 2025-10-07 [commit:15c55f6]

### Añadido
- Imagen del juego agregada al repositorio (image.png)
- Documentación CLAUDE.md para desarrollo con Claude Code

### Mejorado
- README.md actualizado con imagen del juego y mejor formateo
- Limpieza de archivos innecesarios del repositorio

## [1.1.1] - 2025-07-09 [commit:e74b9a2]

### Corregido
- Añadido el fondo principal durante el juego que no se estaba mostrando correctamente

## [1.1.0] - 2025-07-08 [commit:b48d7f1]

### Añadido
- Implementada clase `GameState` para centralizar las variables de estado del juego
- Añadidos bloques de diferentes colores en la pantalla principal
- Visualización de FPS para diagnóstico
- Sistema de colores dinámicos para el temporizador (parpadea en rojo cuando queda poco tiempo)
- Visualización del nivel actual durante el juego
- Visualización del número de bloques disponibles
- Manejo de excepciones para evitar cierres inesperados
- Documentación detallada con docstrings en todas las funciones principales
- Música diferente para cada escena del juego (menú, juego, game over)
- Métodos de conversión entre coordenadas de matriz y pantalla en la clase Position

### Mejorado
- Reestructuración del código para mejor organización y mantenibilidad
- Control de estado de juego más robusto
- Compatibilidad entre sistema antiguo (variables globales) y nuevo (clase GameState)
- Protección contra índices fuera de rango en operaciones con matrices
- Detección mejorada de bloques alineados
- Mejor manejo de recursos gráficos y sonoros
- README.md actualizado con instrucciones más completas
- Transiciones más suaves entre escenas del juego
- Sincronización entre variables globales y GameState para facilitar la transición

### Corregido
- Eliminada variable `blocks_diff` no definida
- Corregidos posibles accesos fuera de rango en las matrices
- Manejo mejorado del tiempo para evitar valores negativos
- Corrección en la reproducción de sonido para evitar superposiciones
- Problemas de visualización en pantallas de diferentes resoluciones

## [1.0.0] - 2025-07-01 [commit:a523c9d] - Versión Inicial

- Implementación básica del juego PatoBlock
- Sistema de bloques que caen y deben ser alineados
- Menú principal, pantalla de juego y pantalla de game over
- Sistema básico de monedas/créditos
