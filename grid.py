class Grid:
    """
    A 2D grid data structure with width, height and cells
    """

    def __init__(self, width: int, height: int):
        """
        Initialize a new grid with given dimensions

        Args:
            width (int): Width of the grid
            height (int): Height of the grid
        """
        if width <= 0 or height <= 0:
            raise ValueError("Width and height must be positive")

        self.width = width
        self.height = height
        self.cells = [[None for _ in range(width)] for _ in range(height)]

    def __str__(self) -> str:
        """
        Return string representation of the grid
        """
        rows = []
        for y in range(self.height):
            row = []
            for x in range(self.width):
                cell = self.cells[y][x]
                if cell is None:
                    row.append('.')
                else:
                    row.append(str(cell))
            rows.append(''.join(row))
        return '\n'.join(rows)
