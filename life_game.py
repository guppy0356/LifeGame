"""
Life Game implementation in terminal
"""
import random
import time
import os

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

if __name__ == "__main__":
    game = LifeGame()
    game.set_random_state()

diff --git a/tests/test_life_game.py b/tests/test_life_game.py
