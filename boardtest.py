# encoding=UTF-8
# Usage: python boardtest.py

import unittest
from board import Board, Coord

# Test data: example boards
b1 = Board([[0,1,2],
            [3,4,5],
            [6,7,8]])

b2 = Board([[1,2,3],
            [4,5,6],
            [7,0,8]])

b3 = Board([[1,2,3],
            [4,5,0]])

# Unit tests for board.py
class BoardTest(unittest.TestCase):

  def test_goal(self):
    self.assertTrue(b1.is_goal())
    self.assertFalse(b2.is_goal())

  def test_coords(self):
    self.assertEqual(b1.find_tile(1), Coord(0,1))
    self.assertEqual(b1.find_empty(), Coord(0,0))
    self.assertEqual(b2.find_empty(), Coord(2,1))

    self.assertTrue(b1.coord_valid(Coord(0,0)))
    self.assertTrue(b1.coord_valid(Coord(2,1)))
    self.assertFalse(b1.coord_valid(Coord(-1,-1)))
    self.assertFalse(b3.coord_valid(Coord(2,1)))

  def test_manhattan_to_goal(self):
    for i in range(8):
      self.assertEqual(b1.manhattan_to_goal(i), 0)
    self.assertEqual(b1.manhattan_distances_sum(), 0)

    b2_distances = { 0:3, 1:1, 2:1, 3:3, 4:1, 5:1, 6:3, 7:1, 8:0 }
   
    for tile_id in b2_distances:
      self.assertEqual(b2.manhattan_to_goal(tile_id), b2_distances[tile_id])

    self.assertEqual(b2.manhattan_to_goal(1), 1)
    self.assertEqual(b2.manhattan_to_goal(0), 3)

  def test_count_misplaced(self):
    self.assertEqual(b1.count_misplaced(), 0)
    self.assertEqual(b2.count_misplaced(), 8)

  def test_size(self):
    self.assertEqual(b3.width(), 3)
    self.assertEqual(b3.height(), 2)

  def test_neighbors(self):
    self.assertEqual(
      b1.find_neighbors(Coord(1,1)),
      set([(1,0), (2,1), (1,2), (0,1)]))

    self.assertEqual(
      b1.find_neighbors(Coord(0,0)),
      set([(1,0), (0,1)]))

  def test_moves(self):
    self.assertEqual(b3.legal_moves(), set([Coord(1,1),Coord(0,2)]))
    self.assertEqual(len(b3.children()), 2)

    self.assertEqual(
      b3.move_empty_to(Coord(1,1)).tiles.tolist(),
      [[1,2,3],[4,0,5]])

if __name__ == "__main__":
  unittest.main()
