pass

class Grid:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.cells = [[False for x in range(width)] for y in range(height)]
