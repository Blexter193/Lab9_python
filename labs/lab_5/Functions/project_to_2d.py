class AsciiArtGenerator:
    def project_to_2d(self):
        points = self.shape.get_points()
        min_x, min_y, max_x, max_y = -self.shape.size, -self.shape.size, self.shape.size, self.shape.size
        width, height = max_x - min_x + 1, max_y - min_y + 1
        canvas = [[" " for _ in range(width)] for _ in range(height)]

        for x, y, z in points:
            proj_x = x + width // 2
            proj_y = y + height // 2
            canvas[proj_y][proj_x] = "#"  # Символ для фігури

        self.projected_2d = canvas
