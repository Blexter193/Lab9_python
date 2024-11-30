from labs.lab_3.Functions.art_generator import ascii_art
from termcolor import colored

color = input("Оберіть колір (red, green, blue): ")
colored_ascii_art = colored(ascii_art, color)
print(colored_ascii_art)
