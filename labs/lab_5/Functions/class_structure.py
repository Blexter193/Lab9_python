class Shape3D:
    def __init__(self, size, color=None):
        self.size = size
        self.color = color

    def scale(self, factor):
        self.size = int(self.size * factor)

    def get_points(self):
        return []

