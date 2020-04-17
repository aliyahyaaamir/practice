"""


Okay we know it's a permutation => 1....nums.length
Need to know how many flips to get it in sorted order

Idea is to at every step find the max and get it to the last index
And then consider an array[0....nums.length - 1], subtracting one constantly

Do this N times and we should have a sorted array



"""

def pancake_sort(nums: list) -> list:

    nums_length = len(nums)
    # maybe consider a base case of two, idk we will see
    # Consider [1, 2, 4, 3]

    count = nums_length
    flips = []
    while count > 0:

        # Find the number 4
        max_index = nums.index(count)
        if count == max_index:
            # no need to flip?
            continue

        # want to swap so we get this to the end
        # consider from beginning to that index
        # need to make sure we reconstruct the nums list at the end of every iteration
        flips.extend([max_index + 1, len(nums)])

        nums = nums[:max_index+1][::-1] + nums[max_index+1:]
        nums = nums[::-1][:len(nums) - 1]
        count -= 1

    return flips


if __name__ == "__main__":
    pancakes = [3, 2, 4, 1]
    # pancakes = [1,2,4,3]
    flips = pancake_sort(pancakes)