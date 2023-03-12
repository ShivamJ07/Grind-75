import unittest
from flood_fill import floodFill

class TestFloodFill(unittest.TestCase):
    def test_floodFill(self):
        self.assertCountEqual(floodFill([[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, color = 2), [[2,2,2],[2,2,0],[2,0,1]])
        self.assertCountEqual(floodFill(image = [[0,0,0],[0,0,0]], sr = 0, sc = 0, color = 0), [[0,0,0],[0,0,0]])

if __name__ == '__main__':
    unittest.main()