from labs.lab_3.Functions.art_generator import ascii_art

symbol = input("Оберіть символ для створення арту: ")
ascii_art = ascii_art.replace("#", symbol)
print(ascii_art)
