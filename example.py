from palpatine import PalpatinePathfinder

grid_map = [
    ['.', '.', '.', '.', '.', '.', '.'],
    ['.', '#', '#', '#', '#', '#', '.'],
    ['.', '#', '.', '.', '.', '#', '.'],
    ['.', '#', '.', '#', '.', '#', '.'],
    ['.', '#', '.', '.', '.', '#', '.'],
    ['.', '#', '#', '#', '#', '#', '.'],
    ['.', '.', '.', '.', '.', '.', '.'],
]

start_pos = (3, 2)
end_pos = (3, 4)

print("Attempt 1: High Wall Cost (Conservative)")
# If cost is 20 he'll likely walk around because breaking is too expensive
solver_safe = PalpatinePathfinder(grid_map, wall_cost=20)
result_safe = solver_safe.execute_order_66(start_pos, end_pos)
solver_safe.visualize(result_safe)

print("\n" + "="*40 + "\n")

print("Attempt 2: Low Wall Cost (Unlimited Power)")
# if cost is 2 he will blast through the wall because 2 < walking around
solver_aggressive = PalpatinePathfinder(grid_map, wall_cost=2)
result_aggressive = solver_aggressive.execute_order_66(start_pos, end_pos)
solver_aggressive.visualize(result_aggressive)
