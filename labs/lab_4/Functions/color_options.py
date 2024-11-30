def apply_color(art, color_choice):
    if color_choice == 'black_white':
        return art
    elif color_choice == 'grayscale':
        gray_scale_art = art.replace('@', '\033[90m@\033[0m').replace('#', '\033[37m#\033[0m')
        return gray_scale_art
