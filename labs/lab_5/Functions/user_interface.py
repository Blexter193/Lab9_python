class DisplayInterface:
    @staticmethod
    def get_user_input():
        shape_type = input("Виберіть фігуру (Cube, Sphere): ")
        size = int(input("Вкажіть розмір фігури: "))
        color = input("Вкажіть колір (наприклад, 'red', 'blue'): ")
        return shape_type, size, color
