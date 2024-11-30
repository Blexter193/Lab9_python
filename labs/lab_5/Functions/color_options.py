class AsciiArtGenerator:
    def colorize(self, symbol, color):
        colors = {"red": "\033[91m", "blue": "\033[94m"}
        return colors.get(color, "") + symbol + "\033[0m"
