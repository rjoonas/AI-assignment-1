# encoding=UTF-8

import numpy as np
import scipy.spatial as spatial
from collections import namedtuple
from hashlib import sha1

import rules as rules

# Decorate coordinate tuples to make code more readable.
# (y, x) order was chosen to match numpy's array indexing style.
Coord = namedtuple("Coord", "y x")

# An immutable sliding puzzle board with (y, x) coordinate system.
# Its state consists of a numpy array of tiles and a moves count.
class Board:

  def __init__(self, tiles, moves = 0):
    # Stores tiles in numpy array with type int8 (byte, -128 to 127).
    self.tiles = np.array(tiles, dtype=np.int8) 
    self.moves = moves
    # Enforce immutability to avoid bugs.
    self.tiles.flags.writeable = False 
  
  # Returns Coord for given tile number.
  def find_tile(self, tile_id):
    return Coord._make(
      np.concatenate(np.where(self.tiles == tile_id)))

  def count_misplaced(self):
    return np.count_nonzero(self.tiles != rules.goal_tiles())

  def find_empty(self): return self.find_tile(0)
  def is_goal(self): return self.count_misplaced() == 0 
  
  def height(self): return self.tiles.shape[0] 
  def width(self):  return self.tiles.shape[1]

  def coord_valid(self, coord):
    return (coord.y >= 0 and coord.x >= 0 and
            coord.y < self.height() and coord.x < self.width())

  # Returns a new board with 0-tile swapped with given target.
  def move_empty_to(self, coord):
    old_empty = self.find_empty()
    swapped_tiles = np.copy(self.tiles)
    
    # Replace empty tile with target tile.
    swapped_tiles[old_empty.y][old_empty.x] = self.tiles[coord.y][coord.x]
    # Replace target tile with empty tile.
    swapped_tiles[coord.y][coord.x] = 0

    return Board(swapped_tiles, self.moves + 1)

  def find_neighbors(self, coord):
    def delta_to_coord(delta):
      return Coord(coord.y + delta[0], coord.x + delta[1]) 
    
    return set(filter(self.coord_valid,
      map(delta_to_coord, [(0,1), (1,0), (0,-1), (-1,0)])))

  def legal_moves(self):
    return self.find_neighbors(self.find_empty())

  # Successor function: list of board states that can be obtained by legal moves.
  def children(self):
    return map(self.move_empty_to, self.legal_moves())

  # SHA1 hashcode for comparing tiles, doesn't check move count.
  # Not called __hash__ as this does not ensure deep equality.
  def tilehash(self):
    return sha1(self.tiles).hexdigest()

  # Manhattan distance to goal for a single tile number.
  def manhattan_to_goal(self, tile_id):
    return spatial.distance.cityblock(      
      rules.goal_coord(tile_id), self.find_tile(tile_id))  

  # Sum of manhattan distances to goal for all tiles.
  def manhattan_distances_sum(self):
    return sum(map(
      lambda tile_id: self.manhattan_to_goal(tile_id),
      np.nditer(self.tiles)))
