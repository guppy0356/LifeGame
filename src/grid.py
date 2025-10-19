class Grid:
    """A 2D grid representation using a nested list structure."""

    def __init__(self, rows, cols, default_value=None):
        """Initialize a 2D grid with given dimensions.

        Args:
            rows (int): Number of rows in the grid
            cols (int): Number of columns in the grid
            default_value: Initial value for all grid cells
        """
        self.rows = rows
        self.cols = cols
        self.grid = [[default_value for _ in range(cols)] for _ in range(rows)]

    def get(self, row, col):
        """Get value at specified position."""
        return self.grid[row][col]

    def set(self, row, col, value):
        """Set value at specified position."""
        self.grid[row][col] = value

    def is_valid_position(self, row, col):
        """Check if position is within grid bounds."""
        return 0 <= row < self.rows and 0 <= col < self.cols

    def __str__(self):
        """Return string representation of the grid."""
        return '\n'.join([' '.join(str(cell) for cell in row) for row in self.grid])

    def __repr__(self):
        """Return string representation of the grid object."""
        return f"Grid(rows={self.rows}, cols={self.cols})"
