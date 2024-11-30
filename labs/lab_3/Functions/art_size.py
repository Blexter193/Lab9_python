import pyfiglet
from labs.lab_3.Functions.user_input import text

width = int(input("Введіть бажану ширину: "))
ascii_art = pyfiglet.figlet_format(text, width=width)
print(ascii_art)
