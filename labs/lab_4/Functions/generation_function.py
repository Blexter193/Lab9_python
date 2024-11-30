from labs.lab_4.Functions.symbol_set import CHAR_SET
import random

import random
def generate_ascii_art(text, width, height):
    art = []
    for _ in range(height):
        line = ''.join(random.choice(CHAR_SET) for _ in range(width))
        art.append(line)
    return '\n'.join(art)


