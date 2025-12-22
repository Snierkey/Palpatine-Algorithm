import heapq
from typing import List, Tuple, Dict, Set

class PalpatinePathfinder:
    def __init__(self, grid: List[List[str]], wall_cost: int = 10):
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0])
        self.wall_cost = wall_cost
        
        self.directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def _is_valid(self, r: int, c: int) -> bool:
        return 0 <= r < self.rows and 0 <= c < self.cols

    def execute_order_66(self, start: Tuple[int, int], end: Tuple[int, int]) -> Dict:
        pq = [(0, start[0], start[1])]
        
        costs = {start: 0}
        
        came_from = {start: None}
        
        nodes_visited = 0

        while pq:
            current_cost, r, c = heapq.heappop(pq)
            nodes_visited += 1

            # if we found the rebel base / end
            if (r, c) == end:
                return self._reconstruct_path(came_from, current_cost, nodes_visited, start, end)

            # skip if found a path that is already more expensive than a known one
            if current_cost > costs.get((r, c), float('inf')):
                continue

            for dr, dc in self.directions:
                nr, nc = r + dr, c + dc

                if self._is_valid(nr, nc):
                    cell_content = self.grid[nr][nc]
                    
                    step_cost = 1
                    if cell_content == '#':
                        step_cost += self.wall_cost

                    new_cost = current_cost + step_cost

                    if new_cost < costs.get((nr, nc), float('inf')):
                        costs[(nr, nc)] = new_cost
                        heapq.heappush(pq, (new_cost, nr, nc))
                        came_from[(nr, nc)] = (r, c)

        return None

    def _reconstruct_path(self, came_from, total_cost, visited_count, start, end):
        path = []
        current = end
        walls_destroyed = 0
        
        while current:
            path.append(current)
            r, c = current
            if self.grid[r][c] == '#' and current != start and current != end:
                walls_destroyed += 1
            current = came_from[current]
            
        path.reverse()
        
        return {
            "path": path,
            "total_cost": total_cost,
            "walls_destroyed": walls_destroyed,
            "nodes_visited": visited_count
        }

    def visualize(self, path_data: Dict):
        if not path_data:
            print("The rebels escaped. No path found.")
            return

        path_set = set(path_data['path'])
        output = []

        print(f"\n--- PALPATINE ALGORITHM RESULTS ---")
        print(f"Total Energy Cost: {path_data['total_cost']}")
        print(f"Walls Destroyed:   {path_data['walls_destroyed']}")
        print(f"Nodes Analyzed:    {path_data['nodes_visited']}")
        print(f"-----------------------------------\n")

        for r in range(self.rows):
            line = ""
            for c in range(self.cols):
                if (r, c) in path_set:
                    if self.grid[r][c] == '#':
                        line += "ϟ"
                    else:
                        line += "• "
                elif self.grid[r][c] == '#':
                    line += "##"
                else:
                    line += "  "
            output.append(line)
        
        print("\n".join(output))
