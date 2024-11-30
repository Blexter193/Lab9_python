from labs.lab_5.Functions.class_structure import Shape3D

class Cube(Shape3D):
    def get_points(self):
        d = self.size // 2
        back_face = [
            (-d, -d, -d), (-d, d, -d),
            (d, -d, -d), (d, d, -d)
        ]
        front_face = [
            (-d, -d, d), (-d, d, d),
            (d, -d, d), (d, d, d)
        ]
        return back_face + front_face
