import math
from labs.lab_5.Functions.class_structure import Shape3D

class Sphere(Shape3D):
    def get_points(self):
        points = []
        for theta in range(0, 360, 30):
            for phi in range(-90, 90, 30):
                x = int(self.size * math.cos(math.radians(phi)) * math.cos(math.radians(theta)) / 2)
                y = int(self.size * math.cos(math.radians(phi)) * math.sin(math.radians(theta)) / 2)
                z = int(self.size * math.sin(math.radians(phi)) / 2)
                points.append((x, y, z))
        return points