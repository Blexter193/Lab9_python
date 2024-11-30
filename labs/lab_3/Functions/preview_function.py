from labs.lab_3.Functions.art_generator import ascii_art

preview = input("Бажаєте побачити попередній перегляд? (так/ні): ")
if preview.lower() == 'так':
    print(ascii_art)
