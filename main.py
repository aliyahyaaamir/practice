"""

Zombie matrix problem


One approach to this problem could be to
initialize the queue to all the zombies and keep track of hour 0
and every time we make new zombies
add to the queue with a new hour

no matter what will need to iterate through all
elements and initialize and find the zombies

the condition to prevent scenarios where human survives
would be captured by making sure that it does not take longer
than num_rows * num_cols in hours (technically less than this
since you can exclude the initial zombie count)

Keep track of population as well

"""

def number_hours_to_infect_all(grid: list) -> int:

    _num_hours = 0
    
    num_rows = len(grid)
    num_cols = len(grid[0])

    copy_state = [[col for col in grid[i]] for i in range(num_rows)]
    visited = [[False] * num_cols for i in range(num_rows)]
    # seems like a bfs algorithm may work nicely here
    # dfs would be a little pointless since it would only check 4 directions

    queue = []

    for i in range(num_rows): 
        for j in range(num_cols):
            if grid[i][j] == 1:
                queue.append((i, j, 0))


    visited[0][0] = True

    while queue:
        i, j, num_hours = queue.pop(0)
        _num_hours = max(num_hours, _num_hours)

        # keep track of noninfected population, and decrement from there!

        # one strategy is to literally just queue up the 1's!!
        # cause that is all that we care

        # look up, down, right, left
        if i - 1 > 0 and grid[i - 1][j] == 0:
            grid[i - 1][j] = 1
            visited[i - 1][j] = True
            queue.append((i - 1, j, num_hours + 1))

        if j - 1 > 0 and grid[i][j - 1] == 0:
            grid[i][j - 1] = 1
            visited[i][j - 1] = True
            queue.append((i, j - 1, num_hours + 1))

        if i + 1 < num_rows and grid[i + 1][j] == 0:
            grid[i + 1][j] = 1
            visited[i + 1][j] = True
            queue.append((i + 1, j, num_hours + 1))

        if j + 1 < num_cols and grid[i][j + 1] == 0:
            grid[i][j + 1] = 1
            visited[i][j + 1] = True
            queue.append((i, j + 1, num_hours + 1))

        # visited = [[False] * num_cols for i in range(num_rows)]

    return _num_hours

if __name__ == "__main__":

    initial_state = [
        [0, 1, 1, 0, 1],
        [0, 1, 0, 1, 0],
        [0, 0, 0, 0, 1],
        [0, 1, 0, 0, 0]
    ]

    num_hours = number_hours_to_infect_all(initial_state)
    print(num_hours)
    assert num_hours == 2

