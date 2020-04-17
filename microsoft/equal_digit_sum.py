"""

Given an array A consisting of N integers
Return the maximum sum of two numbers whose digits add up to an equal sum

If there are no two numbers whose digits have an equal sum, the function should return -1

Ex. A = [51, 71, 17, 42]
Return = 93 (51, 42)

Ex. A = [42, 33, 60]
Return = 102

We can do something interesting here and do a pass through of A
Creating a hashmap with equal sum values

Ex. 6: 51, 42
    8: 71, 17
    . Ignore all keys that have only one entry
    .



"""

from collections import defaultdict


def sum_digits(n):
    s = 0
    while n:
        s += n % 10
        n //= 10
    return s

def max_equal_digit_sum(nums: list) -> int:
    if len(nums) <= 1:
        return -1

    # an default dict would be interesting to try
    # also consider duplicates
    sum_digit_map = defaultdict(list)
    max_val = -1

    for num in nums:
        digit_sum = sum_digits(num) # maybe memoize this w/e
        
        # only ever keep two entries in here at all times
        if digit_sum in sum_digit_map:
            if len(sum_digit_map[digit_sum]) == 2:
                nums_added = sum_digit_map[digit_sum]

                old_val = max(nums_added)
                if (old_val + num) > max_val:
                    max_val = old_val + num
                    sum_digit_map[digit_sum] = [max_val + num]
            else:
                num_added = sum_digit_map[digit_sum][0]
                if (num_added + num) > max_val:
                    max_val = num_added + num
                sum_digit_map[digit_sum].append(num)
        else:
            sum_digit_map[digit_sum].append(num)

    print(sum_digit_map)

    return max_val


if __name__ == "__main__":
    nums = [51, 32, 39]
    return_value = max_equal_digit_sum(nums)