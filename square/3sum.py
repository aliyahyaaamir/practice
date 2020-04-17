"""
We know (a + b) = -c
Let's create a hash map of (a + b) entries
Hash[a+b] = [(index1, index2)]

Then iterate through the keys of the hash map
and find the negative complement

Corner case is all 0's of course
Make sure not to repeat same index

or the case of 1 + -1 = 0
and so is 0 + 0 = 0
"""

from collections import defaultdict

def threeSum(nums: list) -> list:
    nums_length = len(nums)
    if nums_length < 3:
        return []
    
    two_sum_map = defaultdict(list)

    # Generated the hash map for a + b
    for i in range(nums_length):
        for j in range(i + 1, nums_length):
            
            two_sum = nums[i] + nums[j]
            two_sum_map[two_sum].append([i, j])

    triplets = []
    triplets_set = set()

    # Generate the triplets
    for i in range(nums_length):
        index = -nums[i]
        if index in two_sum_map:
            values = two_sum_map[index]
            filtered_values = list(filter(lambda x: x[0] != i and x[1] != i, values))

            for index1, index2 in filtered_values:
                # convert to vlalues
                triplet = [nums[index1],  nums[index2], nums[i]]
                triplets.append(triplet)

    # Now only keep the uniques
    new_triplets = []
    for triplet in triplets:
        new_triplets.append(sorted(triplet))
    
    triplets_set = set()
    for triplet in new_triplets:
        triplets_set.add(tuple(triplet))

    triplets = [list(triplet) for triplet in triplets_set]

    return triplets

            
if __name__ == "__main__":
    nums = [-1, 0, 1, 2, -1, -4]
    nums = [1,2,-2,-1]
    triplets = threeSum(nums)