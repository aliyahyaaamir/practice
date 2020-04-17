"""
We have 3 operations that we can perform
We want to find the minimum number of operations to convert word1 to word2

So the minimum number of operations eh

We have two ptrs i, j
comparing

word1[0] to word2[0] -> we see that to convert word1[0] to word2[0] we need to remove the letter and add r
So 2 operations, or rather simply replace the letter so 1 operation

word1[1] to word2[1] -> min_operations(i - 1, j - 1) + current_operation

Scenarios to consider: uneven length strings right

word[4] -> word2[2] 

min_operations(i, j) = min_operations(i, j) + current_num of operations

Seems straightforward

"""

# def min_distance(word1: str, word2: str) -> int:
    
#     w1 = len(word1)
#     w2 = len(word2)

#     if not w1:
#         return w2
    
#     if not w2:
#         return w1

#     dp = [[0] * (w2 + 1) for _ in range(w1 + 1)]

#     for i in range(1, w1 + 1):
#         print('here')
#         if i > w2:
#             dp[i][i] = dp[i-1][i-1]
#             continue
#         num_operations = 0
#         if word1[i-1] != word2[i-1]:
#             num_operations = 1
#         dp[i][i] = dp[i-1][i-1] + num_operations

#     # check if there is remaining length for w2
#     print(dp, dp[w1][w2])
#     if w2 - w1 > 0:
#         print('here', w2 - w1)
#         dp[w1][w2] += w2 - w1
#     elif w1 - w2 > 0:
#         dp[w1][w2] = (w1 - w2) + dp[w1-w2][w1-w2]

#     return dp[w1][w2]


def min_distance(word1: str, word2: str) -> int:
    
    w1 = len(word1)
    w2 = len(word2)

    if not w1:
        return w2
    
    if not w2:
        return w1

    dp = [[0] * (w2 + 1) for _ in range(w1 + 1)]

    for i in range(1, w1 + 1):
        for j in range(1, w2 + 1):
            num_operations = 0
            if i == j:
                if word1[i-1] != word2[j-1]:
                    num_operations = 1
                dp[i][j] = dp[i-1][j-1] + num_operations
            else:
                dp[i][j] = max(dp[i][j-1], dp[i-1][j])

    # check if there is remaining length for w2
    print(dp, dp[w1][w2])
    if w2 - w1 > 0:
        dp[w1][w2] += w2 - w1
    elif w1 - w2 > 0:
        dp[w1][w2] = (w1 - w2) + dp[w1-w2][w1-w2]

    return dp[w1][w2]


if __name__ == "__main__":
    word1 = 'horse'
    word2 = 'ros'

    word1 = 'intention'
    word2 = 'execution'

    word1 = 'a'
    word2 = 'bb'

    word1 = 'sea'
    word2 = 'eat'

    min_operations = min_distance(word1, word2)