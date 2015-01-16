# encoding=UTF-8

import numpy as np

# Goal state: numbers 0–8 in a 3x3 array. 0 is used as a magic 
# number for representing the empty tile.
def goal_tiles():
  return np.arange(9).reshape(3,3)

# Goal coordinates for a single tile.
def goal_coord(tile_id):
 return np.where(goal_tiles() == tile_id)
