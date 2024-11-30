def align_text(art, alignment, width):
    aligned_art = []
    for line in art.split('\n'):
        if alignment == 'left':
            aligned_art.append(line.ljust(width))
        elif alignment == 'center':
            aligned_art.append(line.center(width))
        elif alignment == 'right':
            aligned_art.append(line.rjust(width))
    return '\n'.join(aligned_art)
