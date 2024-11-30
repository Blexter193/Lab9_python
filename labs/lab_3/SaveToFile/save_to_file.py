from labs.lab_3.Functions.art_generator import ascii_art

def save_to_file(ascii_art):
    filename = input("Введіть ім'я файлу для збереження: ")
    with open(f"{filename}.txt", "w") as file:
        file.write(ascii_art)
    print(f"ASCII-арт збережено у файл {filename}.txt")
