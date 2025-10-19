import unittest
from game_of_life.cell import CellState

class TestCell(unittest.TestCase):
    def test_cell_states(self):
        self.assertEqual(CellState.DEAD.value, 0)
        self.assertEqual(CellState.ALIVE.value, 1)
        self.assertNotEqual(CellState.DEAD, CellState.ALIVE)

if __name__ == '__main__':
