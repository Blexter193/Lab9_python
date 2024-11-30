import pyfiglet
from termcolor import colored
from labs.lab_3.SaveToFile.save_to_file import save_to_file

def main():
    text = input("Введіть слово або фразу для перетворення в ASCII-арт: ")
    fonts = pyfiglet.FigletFont.getFonts()
    print("Доступні шрифти:", fonts)
    chosen_font = input("Оберіть шрифт: ")
    color = input("Оберіть колір (red, green, blue): ")
    ascii_art = pyfiglet.figlet_format(text, font=chosen_font)
    colored_ascii_art = colored(ascii_art, color)
    print(colored_ascii_art)

    if input("Бажаєте зберегти у файл? (y/n): ").lower() == 'y':
            save_to_file(ascii_art)