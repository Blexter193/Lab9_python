from labs.lab_3.Functions.user_input import text

import pyfiglet

fonts = pyfiglet.FigletFont.getFonts()
print("Доступні шрифти:", fonts)
chosen_font = input("Оберіть шрифт: ")
ascii_art = pyfiglet.figlet_format(text, font=chosen_font)
print(ascii_art)
