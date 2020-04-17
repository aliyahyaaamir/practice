
def fair_indexes(A: list, B: list) -> int:

    # Find the number of fair indexes
    num_fair_indexes = 0
    arr_length = len(A)

    for i in range(1, arr_length):
        if sum(A[0:i]) == sum(A[i:]) == sum(B[0:i]) == sum(B[i:]):
            num_fair_indexes += 1


    return num_fair_indexes

if __name__ == "__main__":
    """
    k = 2, 3
    A[0] -> A[k-1] A[k] -> A[N-1]
    """

    A = [4, -1, 0, 3]
    B = [-2, 5, 0, 3]

    A = [2, -2, -3, 3]
    B = [0, 0, 4, -4]

    A = [4, -1, 0, 3]
    B = [-2, 6, 0, 4]

    A = [3, 2, 6]
    B = [4, 1, 6]

    A = [1, 4, 2, -2, 5]
    B = [7, -2, -2, 2, 5]

    k = fair_indexes(A, B)