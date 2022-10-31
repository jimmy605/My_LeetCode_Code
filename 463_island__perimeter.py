class Solution:
    def islandPerimeter(self, grid):
        n_rows = len(grid)
        n_cols = len(grid[0])
        
        result = 0
        
        for r in range(n_rows):
            for c in range(n_cols):
                if grid[r][c] == 1:
                    result += 4
                    
                    if r > 0 and grid[r - 1][c] == 1:
                        result -= 2
                    
                    if c > 0 and grid[r][c - 1] == 1:
                        result -= 2
        
        return result