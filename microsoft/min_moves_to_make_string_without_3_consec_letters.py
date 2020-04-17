"""
You are given a string S consisting of N letters of 'a' and/or 'b'.
In one move, you can swap one letter for the other ('a' for 'b' or 'b' for 'a')


Given S = 'baaaaa'
Min moves = 1

Result = 'baabaa'

Intuition is to know about all parts in the string that represent the same 3 consecutive letters


'aaabbaa'

Split string into consecutive substrings
And insert different letter in the middle for every 3

aababa

"""

def min_moves(S: str) -> int:
    similar_chunks = []

    last_letter = ''
    chunk = ''

    for letter in S:
        if last_letter == letter or last_letter == '':
            chunk += letter
        else:
            if len(chunk) >= 3:
                similar_chunks.append(chunk)
            chunk = letter
        last_letter = letter
    
    if len(chunk) >= 3:
        similar_chunks.append(chunk)

    min_moves = 0
    print(similar_chunks)
    for chunk in similar_chunks:
        num_moves = len(chunk)//3
        min_moves += num_moves if num_moves > 0 else 1

    return min_moves


if __name__ == "__main__":
    S = 'baaaaa'
    S = 'baaabbaabbba'
    S = 'baabab'
    S = 'baaaaab'
    min_moves = min_moves(S)