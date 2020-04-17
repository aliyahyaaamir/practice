"""
I think there are a few steps to take
1. check the sign of N
2. If positive go from left to right (checking that 5 is the max placement)
3. If negative go from right to left (checking that hmmmm)

-100015
vs.
-100051

"""

from functools import reduce

def get_digit():
    pass

def max_possible_value(N: int) -> int:
    
    if N >= 0:
        digit_arr = [int(digit) for digit in str(N)]

        for index, digit in enumerate(digit_arr):
            if 5 > digit:
                # shift everything to right
                digit_arr.insert(index, 5)
                break
        return int(reduce(lambda x, y: str(x) + str(y), digit_arr))
    else:
        N *= -1
        digit_arr = [int(digit) for digit in str(N)]

        for index, digit in enumerate(digit_arr):
            if 5 < digit:
                digit_arr.insert(index, 5)
                break
        return int(reduce(lambda x, y: str(x) + str(y), digit_arr))*-1

if __name__ == "__main__":
    max_value = max_possible_value(-999)