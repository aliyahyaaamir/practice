"""

It wants a runtime complexity of O(logn)
`This means we can just sort and go from there`
This is definitely a variant of binary search


How does the existing binary search algorithm work?
1. Get midpoint
2. go left or right depending on value


Recursive is the way to go
"""

def binary_search(nums: list, target: int, l_index: int, r_index: int):

    if l_index <= r_index:
        mid_point = l_index + (r_index - l_index)//2

        if target == nums[mid_point]:
            return mid_point
        elif nums[mid_point] >= nums[l_index]: # normal

            if target >= nums[l_index] and target < nums[mid_point]:
                return binary_search(nums, target, l_index, mid_point - 1)
            else:
                return binary_search(nums, target, mid_point + 1, r_index)
        else:

            if target > nums[mid_point] and target <= nums[r_index]:
                return binary_search(nums, target, mid_point + 1, r_index)
            else:
                return binary_search(nums, target, l_index, mid_point - 1)

    return -1


def search(nums: list, target: int) -> int:
    return binary_search(nums, target, 0, len(nums) - 1)


if __name__ == "__main__":
    nums = [3, 5, 1]
    target = 3
    output = search(nums, target)
    print(output)
    assert output == 0, 'first case'

    nums = [4,5,6,7,0,1,2]
    target = 0
    output = search(nums, target)
    print(output)
    assert output == 4, 'second case'
