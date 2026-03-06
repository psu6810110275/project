def gridChallenge(grid: list) -> str:
    sorted_grid = ["".join(sorted(row)) for row in grid]
    
    rows = len(sorted_grid)
    cols = len(sorted_grid[0]) if rows > 0 else 0
    
    for col in range(cols):
        for row in range(1, rows):
            if sorted_grid[row][col] < sorted_grid[row-1][col]:
                return "NO"
                
    return "YES"
