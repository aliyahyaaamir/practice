"""
Seems like there are three critical things to do
1. If there are 3 or more candies horizontally or vertically crush (crush all that you see)
2. Reset Board (allow candies to drop)
3. Repeat process until no more need to reset (i.e. before board == after board or bool to let you know that something got crushed)

Intuition
Seems like we can iterate through the 2-d array and for every index we can perform a depth-first search (visited is important here)
Oh shit but that could just tell us the count, not whether to set to 0!!!!!! (Shit let's think)
    We can have every call to dfs return a count, so we know whether to reset or not
    Damn that is only effective for a count that INCLUDES BOTH vertical and horizontal
    We need to seperate those two out (should be no problem)


Reset Board after going through the board

O(M * N) is what I'm thinking since we need to iterate through the array
"""

# def dfs(prev_value: int, i: int, j: int, board: list, visited_board: list, num_rows: int, num_cols: int, vertical_count: int, horizontal_count, override = False) -> tuple:
    
#     if i < 0 or j < 0 or i + 1 > num_rows or j + 1 > num_cols or (visited_board[i][j] and not override) or prev_value != board[i][j] or board[i][j] == 0:
#         return (vertical_count, horizontal_count)
    
#     visited_board[i][j] = True

#     # Only considering four directions i.e. no diagonals
#     v_count1, h_count1 = dfs(prev_value, i + 1, j, board, visited_board, num_rows, num_cols, vertical_count + 1, 0)
#     v_count2, h_count2 = dfs(prev_value, i - 1, j, board, visited_board, num_rows, num_cols, max(v_count1, vertical_count + 1), 0)
#     v_count3, h_count3 = dfs(prev_value, i, j + 1, board, visited_board, num_rows, num_cols, 0, horizontal_count + 1)
#     v_count4, h_count4 = dfs(prev_value, i, j - 1, board, visited_board, num_rows, num_cols, 0, max(h_count3, horizontal_count + 1))
#     v_countx, h_countx = dfs(prev_value, i, j + 1, board, visited_board, num_rows, num_cols, 0, max(h_count4, horizontal_count + 1), True)

#     vertical_count = max(v_count1, v_count2, v_count3, v_count4)
#     horizontal_count = max(h_count1, h_count2, h_count3, h_count4)

#     print('here', (i, j), vertical_count, horizontal_count)

#     if vertical_count >= 3:
#         board[i][j] = 0
    
#     if horizontal_count >= 3:
#         board[i][j] = 0

#     return (vertical_count, horizontal_count)

def drop_candies(board: list, num_rows: int, num_cols: int) -> None:

    # print(sorted(set(total_indices), key=lambda x: (x[0], x[1])))
    """
    Group by like row index
    Group by like column index
    [5:10] = swap all elements from 0 - 5 to 5 - 10
    """

    for j in range(num_cols):
        # Two ptrs start here
        read = num_rows - 1
        write = num_rows - 1

        while read >= 0:
            if board[read][j] != 0:
                board[write][j] = board[read][j]
                write -= 1
            read -= 1
        while write >= 0:
            board[write][j] = 0
            write -= 1


def search_down(prev_value: int, i: int, j: int, board: list, visited_board: list, num_rows: int, num_cols: int, indices: list):
    if i + 1 > num_rows or visited_board[i][j] or prev_value != board[i][j] or board[i][j] == 0:
        return indices
    
    # Only considering vertical direction i.e. no diagonals, or horizontals
    # I think we only have to look down
    indices.append((i, j))
    search_down(prev_value, i + 1, j, board, visited_board, num_rows, num_cols, indices)

    # print(indices)
    return indices
    # vertical_dfs(prev_value, i + 1, j, board, visited_board, num_rows, num_cols, vertical_count + 1)

def search_right(prev_value: int, i: int, j: int, board: list, visited_board: list, num_rows: int, num_cols: int, indices: list):
    if j + 1 > num_cols or visited_board[i][j] or prev_value != board[i][j] or board[i][j] == 0:
        return indices
    
    # Only considering vertical direction i.e. no diagonals, or horizontals
    # I think we only have to look down
    indices.append((i, j))
    indices = search_right(prev_value, i, j + 1, board, visited_board, num_rows, num_cols, indices)

    return indices

def candy_crush(board: list) -> list:
    # Consider base cases at the end
    num_rows = len(board)
    num_cols = len(board[0])

    visited_board = [[False] * num_cols for _ in range(num_rows)]
    # later on change this to a set and see how this works
    total_indices = []

    while True:
        for i in range(num_rows):
            for j in range(num_cols):
                vertical_indices = search_down(board[i][j], i, j, board, visited_board, num_rows, num_cols, [])
                horizontal_indices = search_right(board[i][j], i, j, board, visited_board, num_rows, num_cols, [])
                if len(vertical_indices) >= 3:
                    total_indices += vertical_indices
                
                if len(horizontal_indices) >= 3:
                    total_indices += horizontal_indices
        
        if len(total_indices) == 0:
            break
        
        for i, j in total_indices:
            board[i][j] = 0

        drop_candies(board, num_rows, num_cols)
        total_indices = []
        break


    # print(total_indices)
    print(board)

if __name__ == "__main__":
    board = [[4,4,4,4], [1, 2, 9, 5], [6, 9, 9, 9]]
    candy_crush(board)

