"""
Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output: [1,2,3,6,9,8,7,4,5]

I don't know why this question is tripping me up so much

First row, then last column, then last row, then first column
Repear process moving inwards, ok!


"""

def one_spiral(matrix: list) -> list:
    matrix_len = len(matrix)
    num_cols = len(matrix[0])

    if matrix_len == 1 and num_cols == 1:
        return [matrix[0][0]]
    elif matrix_len == 1:
        return matrix[0]
    elif num_cols == 1:
        return [matrix[i][0] for i in range(matrix_len)]

    first_row = matrix[0]
    last_column = [matrix[i][num_cols-1] for i in range(1, matrix_len - 1)]
    last_row = matrix[matrix_len-1][::-1]
    first_column = [matrix[i][0] for i in range(1, matrix_len - 1)][::-1]

    return first_row + last_column + last_row + first_column

def spiral_order(matrix: list) -> list:
    
    matrix_len = len(matrix)
    # We'll consider other base cases later once we have the spiral functionality working
    if matrix_len < 2:
        return matrix[0]

    spiral_output = []

    # We should call a function that does this
    spiral_matrix = [row[::] for row in matrix]
    while True:
        spiral = one_spiral(spiral_matrix)
        spiral_output += spiral

        num_cols = len(spiral_matrix[0])
        num_rows = len(spiral_matrix)
        spiral_matrix = [row[1: num_cols-1] for row in spiral_matrix][1: num_rows - 1]

        if len(spiral_matrix) < 1 or num_cols - 2 <= 0:
            break

    return spiral_output


if __name__ == "__main__":
    input = [[1,11],[2,12],[3,13],[4,14],[5,15],[6,16],[7,17],[8,18],[9,19],[10,20]]

    spiral_output = spiral_order(input)
