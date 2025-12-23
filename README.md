# The Palpatine Algorithm ϟ

> *"The Dark Side of the Pathfinding is a pathway to many abilities some consider to be unnatural..."*

## Overview

standard pathfinding algorithms (like A* or BFS) view walls as absolute boundaries. they will search infinitely for a way *around* an obstacle,

**The Palpatine Algorithm** views walls merely as suggestions. it calculates the most efficient path to a target, weighing the cost of walking normally versus the energy cost of **destroying the wall** and walking through the rubble.

## How it works

the algorithm treats the map as a weighted graph:
1.  **Empty Space (`.`):** Traversal Cost = `1`
2.  **Wall (`#`):** Traversal Cost = `1 + wall_cost`

it utilizes a Priority Queue (similar to Dijkstra's algorithm) to minimize the total energy expenditure.
- if `wall_cost` is high, the algorithm behaves like a standard pathfinder
- if `wall_cost` is low (or the detour is too long), the algorithm chooses violence

## Usage

```python
from palpatine import PalpatinePathfinder

grid = [
    ['.', '#', '.'],
    ['.', '#', '.'],
    ['.', '.', '.']
]

# initialize (wall_cost determines how reluctant he is to use force lightning)
solver = PalpatinePathfinder(grid, wall_cost=5)

# find path from (0,0) to (0,2)
# returns a dictionary with path coordinates and stats
result = solver.execute_order_66(start=(0,0), end=(0,2))

# Visualize
solver.visualize(result)
```

## Output Legend

- `•`: Standard movement
- `ϟ`: **UNLIMITED POWERRRR**
- `##`: Undestroyed Wall

## Note

This is the final version btw, i dont think this needs updates in the future unless its optimization or sum like that

## License

[Zlib](LICENSE) License
