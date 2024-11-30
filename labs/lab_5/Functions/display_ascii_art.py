from labs.lab_5.Functions.cube import Cube

class AsciiArtGenerator:
    def __init__(self, shape):
        self.shape = shape
        self.projected_2d = []

    def project_to_2d(self):
        points = self.shape.get_points()
        min_x, min_y, max_x, max_y = -self.shape.size, -self.shape.size, self.shape.size, self.shape.size
        width, height = max_x - min_x + 1, max_y - min_y + 1

        canvas = [[" " for _ in range(width)] for _ in range(height)]

        for i, (x, y, z) in enumerate(points):
            proj_x = x + width // 2
            proj_y = y + height // 2

            symbol = "#" if i < 4 else "@"
            canvas[proj_y][proj_x] = symbol

        if isinstance(self.shape, Cube):
            self.draw_lines(canvas, width, height)
        self.projected_2d = canvas

    def draw_lines(self, canvas, width, height):
        lines = [
            ((0, 1), "#"), ((0, 2), "#"), ((1, 3), "#"), ((2, 3), "#"),
            ((4, 5), "@"), ((4, 6), "@"), ((5, 7), "@"), ((6, 7), "@"),
            ((0, 4), "*"), ((1, 5), "*"), ((2, 6), "*"), ((3, 7), "*")
        ]

        for (start, end), symbol in lines:
            x1, y1, _ = self.shape.get_points()[start]
            x2, y2, _ = self.shape.get_points()[end]
            self.bresenham_line(canvas, x1 + width // 2, y1 + height // 2, x2 + width // 2, y2 + height // 2, symbol)

    def bresenham_line(self, canvas, x1, y1, x2, y2, symbol):
        dx = abs(x2 - x1)
        dy = abs(y2 - y1)
        sx = 1 if x1 < x2 else -1
        sy = 1 if y1 < y2 else -1
        err = dx - dy

        while True:
            if 0 <= y1 < len(canvas) and 0 <= x1 < len(canvas[0]):
                canvas[y1][x1] = symbol
            if x1 == x2 and y1 == y2:
                break
            e2 = err * 2
            if e2 > -dy:
                err -= dy
                x1 += sx
            if e2 < dx:
                err += dx
                y1 += sy

    def display_ascii_art(self):
        for row in self.projected_2d:
            print("".join(row))
