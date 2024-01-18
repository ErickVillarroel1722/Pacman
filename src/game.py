# game.py
import pygame
from graphics import draw_pacman
from levels import load_level

def main():
    pygame.init()

    level_number = 1
    level_data = load_level(level_number)

    # Configuración de la pantalla
    width, height = 800, 600
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Pac-Man Game")

    # Colores
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)

    # Pac-Man
    pacman_x, pacman_y = 1, 1
    pacman_speed = 5

    # Bucle principal del juego
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    pacman_x -= pacman_speed
                elif event.key == pygame.K_RIGHT:
                    pacman_x += pacman_speed
                elif event.key == pygame.K_UP:
                    pacman_y -= pacman_speed
                elif event.key == pygame.K_DOWN:
                    pacman_y += pacman_speed

        # Lógica del juego aquí

        # Dibujar el nivel en la pantalla
        screen.fill(BLACK)  # Limpiar la pantalla en cada iteración

        for y, row in enumerate(level_data):
            for x, char in enumerate(row):
                cell_width = width // len(row)
                cell_height = height // len(level_data)

                if char == '#':
                    # Dibujar pared
                    pygame.draw.rect(screen, WHITE, (x * cell_width, y * cell_height, cell_width, cell_height))
                elif char == 'P':
                    # Dibujar a Pac-Man
                    draw_pacman(screen, pacman_x, pacman_y)

        # Actualizar la pantalla
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
