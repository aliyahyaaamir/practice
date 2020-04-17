"""
First Missing Positive

Need to solve in O(n) time

hmmmmm

Intuition is to figure out the increment in the sequence
but why
Cause then after you do an initial pass, you can go through again and find the number you're missing

But we also are not guaranteed that it is a sequence at all

What about making a pass through and finding the min, and then doing another pass and finding the next min
    This would collapse if the 

Looks like we can pre-generate a number list of minimums and simply iterate through eliminating candidates
And just take the first number remaining in that list


You can iterate through and see if you recognize any difference greater than one between the current and previous
(with the exception of negative values) and return that

If you do not find anything, then that the max value + 1

Boom bam
Nope

"""

def find_min(nums: list) -> int:
    
    min = nums[0]

    for num in nums:
        if num < min:
            min = num
    
    return min

def find_max(nums: list) -> int:
    
    max = nums[0]

    for num in nums:
        if num > max:
            max = num
    
    return max

def first_missing_positive(nums: list) -> int:
    nums_length = len(nums)

    # Base Case
    if 1 not in nums:
        return 1

    # First stage, just filter out the negative values
    # Second stage get rid of duplicates
    for index in range(nums_length):
        if nums[index] <= 0:
            nums[index] = 1

    # Check for in between
    for index in range(nums_length):

        if abs(nums[index]) == nums_length:
            nums[0] = -abs(nums[0])
        elif abs(nums[index]) < nums_length:
            nums[abs(nums[index])] = -abs(nums[abs(nums[index])])
    
    for index in range(1, nums_length):
        if nums[index] > 0:
            return index
    
    if nums[0] > 0:
        return nums_length

    return nums_length + 1


if __name__ == "__main__":
    nums = [1, 2, 0, -1]
    # nums = [3, 4, 1]
    # nums = [1, 4, 3, 4, 7, 8, 9, 11, 12]
    nums = [1, 2]
    nums = [2]
    nums = [1, 1000]
    nums = [1, 2, 7, 3]
    first_missing_positive = first_missing_positive(nums)