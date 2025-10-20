#!/usr/bin/env python3

# Grid size constants
GRID_WIDTH = 40
GRID_HEIGHT = 20

class Grid:
    def __init__(self, width=GRID_WIDTH, height=GRID_HEIGHT):
        """Initialize a new grid with the specified dimensions"""
        self.width = width
        self.height = height
        # Initialize empty grid (all cells dead)
        self.cells = [[0 for x in range(width)] for y in range(height)]

    def get_cell(self, x, y):
        """Get the state of a cell at the specified coordinates"""
        return self.cells[y][x]

    def set_cell(self, x, y, state):
        """Set the state of a cell at the specified coordinates"""
        self.cells[y][x] = state
