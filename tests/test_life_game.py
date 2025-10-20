import unittest
from life_game import LifeGame

class TestLifeGame(unittest.TestCase):
    def setUp(self):
        self.game = LifeGame()

    def test_grid_initialization(self):
        """Test grid is initialized with correct dimensions"""
        self.assertEqual(len(self.game.grid), 20)  # height
        self.assertEqual(len(self.game.grid[0]), 40)  # width

    def test_random_state(self):
        """Test random state generation contains valid values"""
        self.game.set_random_state()
        all_values = [cell for row in self.game.grid for cell in row]
        self.assertTrue(all(v in [0, 1] for v in all_values))

if __name__ == '__main__':
    unittest.main()
