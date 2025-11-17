"""
Life Game implementation in terminal
"""
import os
import random
import time


class LifeGame:
    def __init__(self, width=40, height=20):
        self.width = width
        self.height = height
        self.grid = [[0 for _ in range(width)] for _ in range(height)]

    def set_random_state(self):
        """Set random initial state"""
        for y in range(self.height):
            for x in range(self.width):
                self.grid[y][x] = random.choice([0, 1])

    def _count_neighbors(self, y, x):
        neighbors = 0
        for dy in (-1, 0, 1):
            for dx in (-1, 0, 1):
                if dy == 0 and dx == 0:
                    continue
                ny, nx = (y + dy) % self.height, (x + dx) % self.width
                neighbors += self.grid[ny][nx]
        return neighbors

    def step(self):
        new_grid = [[0 for _ in range(self.width)] for _ in range(self.height)]
        for y in range(self.height):
            for x in range(self.width):
                neighbors = self._count_neighbors(y, x)
                if self.grid[y][x] == 1 and neighbors in (2, 3):
                    new_grid[y][x] = 1
                elif self.grid[y][x] == 0 and neighbors == 3:
                    new_grid[y][x] = 1
        self.grid = new_grid

    def display(self):
        os.system("cls" if os.name == "nt" else "clear")
        print("Life Game - Press Ctrl+C to exit")
        for row in self.grid:
            print("".join("█" if cell else " " for cell in row))

    def run(self, delay=0.2):
        while True:
            self.display()
            self.step()
            time.sleep(delay)


if __name__ == "__main__":
    game = LifeGame()
    game.set_random_state()
    try:
        game.run()
    except KeyboardInterrupt:
        pass
