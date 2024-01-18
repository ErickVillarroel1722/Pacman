# sounds.py
import pygame
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
sound_folder = os.path.join(current_dir, 'assets', 'sounds')

def play_eating_sound():
    eating_sound = pygame.mixer.Sound(os.path.join(sound_folder, 'eating.wav'))
    eating_sound.play()
