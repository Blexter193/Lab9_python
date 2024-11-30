def save_to_file(self, filename):
    with open(filename, 'w') as f:
        for row in self.projected_2d:
            f.write("".join(row) + "\n")