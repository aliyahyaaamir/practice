"""
Classic depth first search problem

"""
def max_area_of_island(grid: list) -> int:

    if len(grid) == 0:
        return 0

    num_rows = len(grid)
    num_cols = len(grid[0])
    max_area = 0
    visited_grid = [[False] * num_cols for _ in range(num_rows)]

    for i in range(num_rows):
        for j in range(num_cols):
            if not visited_grid[i][j] and grid[i][j] == 1:
                area = dfs_island(i, j,  grid, visited_grid, num_rows, num_cols)
                max_area = max(area, max_area)

    return max_area

def dfs_island(i, j, grid, visited_grid, num_rows, num_cols):
    
    if i < 0 or j < 0 or i > num_rows - 1 or j > num_cols -1 or visited_grid[i][j]\
        or grid[i][j] == 0:
        return 0

    area = 1
    visited_grid[i][j] = True
    area += dfs_island(i + 1, j, grid, visited_grid, num_rows, num_cols)
    area += dfs_island(i, j + 1, grid, visited_grid, num_rows, num_cols)
    area += dfs_island(i - 1, j, grid, visited_grid, num_rows, num_cols)
    area += dfs_island(i, j - 1, grid, visited_grid, num_rows, num_cols)

    return area


if __name__ == "__main__":
    input = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]

    max_area = max_area_of_island(input)
