"""
N different songs
L songs in a playlist (not necessarily different)
A song can only be played again if K other songs have been played


"""

def helper(N, L, K):

    if L == 0:
        return 

    for i in range(1, N + 1):
        helper(i, )
    


def numMusicPlaylists(N: int, L: int, K: int) -> int:
    helper(N, L, K)


if __name__ == "__main__":
    numMusicPlaylists(3, 3, 1)