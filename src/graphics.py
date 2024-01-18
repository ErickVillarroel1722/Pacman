# graphics.py
import pygame
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
image_folder = os.path.join(current_dir, 'assets', 'images')

def draw_pacman(screen, x, y):
    pacman_image = pygame.image.load(os.path.join(image_folder, 'pacman.png'))
    screen.blit(pacman_image, (x, y))

def draw_ghost(screen, x, y):
    ghost_image = pygame.image.load(os.path.join(image_folder, 'ghost.png'))
    screen.blit(ghost_image, (x, y))
