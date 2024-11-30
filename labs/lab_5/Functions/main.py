from labs.lab_5.Functions.cube import Cube
from labs.lab_5.Functions.sphere import Sphere
from labs.lab_5.Functions.display_ascii_art import AsciiArtGenerator
from labs.lab_5.Functions.user_interface import DisplayInterface

class DisplayInterface:
    @staticmethod
    def main():
        shape_type, size, color = DisplayInterface.get_user_input()
        shape = None

        if shape_type.lower() == "cube":
            shape = Cube(size, color)
        elif shape_type.lower() == "sphere":
            shape = Sphere(size, color)
        else:
            print("Невідома фігура!")
            return

        generator = AsciiArtGenerator(shape)
        generator.project_to_2d()
        generator.display_ascii_art()

        save = input("Бажаєте зберегти результат? (y/n): ")
        if save.lower() == "y":
            filename = input("Введіть ім'я файлу для збереження: ")
            generator.save_to_file(filename)
            print(f"Результат збережено у файл {filename}")


def main():
    return None