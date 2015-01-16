Assignment 1.1: Search algorithms
=================

This is an assignment submission for Dr. K. P. Chan's course **CSIS0270 Artificial intelligence**  (University of Hong Kong, 2014).

My solution is a sliding tile puzzle solver written in Python 2.7. It solves the 8-puzzle position given in the assignment paper using breadth-first search (BFS), iterative deepening depth first search (IDDFS) and A* search. Some performance statistics are also provided to aid in comparing the algorithms.

Example output
==============

```
CSIS0270 Artificial intelligence (Dr. K. P. Chan, University of Hong Kong)
Assignment 1.1 by Joonas Rouhiainen, 3035133686, joonas@hku.hk

  a) Uninformed breadth-first search..................... ✓
    * Execution time:      0:00:38.157394
    * Path cost to goal:   26 moves
    * Iterations:          431366
    * Queue size at goal:  43269

  b) Iterative deepening depth-first search........................................................................................ ✓
    * Execution time:      0:02:15.790547
    * Path cost to goal:   26 moves
    * Iterations:          1778123
    * Queue size at goal:  12

  c I) A* search using number of misplaced tiles heuristic.. ✓
    * Execution time:      0:00:10.448667
    * Path cost to goal:   26 moves
    * Iterations:          51959
    * Queue size at goal:  23472

  c II) A* search using sum of manhattan distances heuristic ✓
    * Execution time:      0:00:02.321234
    * Path cost to goal:   26 moves
    * Iterations:          3381
    * Queue size at goal:  1996

```

Running
=======

1. Run unit tests with `python boardtest.py`
2. Run the puzzle solver with `python ai1.py`

Modules
=======

File           | Description
--------------:|:-------------------------------------------------------------------------------
   `search.py` | My algorithm implementations.
      `ai1.py` | Main module: runs timed searches against the initial board state.
    `board.py` | Board class: a sliding puzzle board with immutable state.
    `rules.py` | Static rules of the sliding puzzle game.
`boardtest.py` | Unit tests for board logic.