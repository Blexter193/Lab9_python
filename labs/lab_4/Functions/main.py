from labs.lab_4.Functions.user_input import get_user_input
from labs.lab_4.Functions.art_dimensions import get_dimensions
from labs.lab_4.Functions.generation_function import generate_ascii_art
from labs.lab_4.Functions.align_text import align_text
from labs.lab_4.Functions.color_options import apply_color
from labs.lab_4.Functions.preview_function import preview_art
from labs.lab_4.SaveToFile.save_to_file import save_to_file

def main():
    text = get_user_input()
    width, height = get_dimensions()
    alignment = input("Choose alignment (left, center, right): ")
    color_choice = input("Choose color (black_white, grayscale): ")

    art = generate_ascii_art(text, width, height)
    art = align_text(art, alignment, width)
    art = apply_color(art, color_choice)

    preview_art(art)

    if input("Do you want to save the art? (y/n): ").lower() == 'y':
            save_to_file(art)
