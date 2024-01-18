# levels.py
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
level_folder = os.path.join(current_dir, 'levels')

def load_level(level_number):
    level_file_path = os.path.join(level_folder, f'level{level_number}.txt')

    try:
        with open(level_file_path, 'r') as file:
            level_data = [line.strip() for line in file]

        return level_data
    except FileNotFoundError:
        print(f"Error: Level file '{level_file_path}' not found.")
        return None
