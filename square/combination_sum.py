"""

Find all unique combinations in candidates
where the candidate numbers sum to target

The twist: The same repeated number may be chosen from candidates
unlimited times

This screams backtracking
Or maybe not

For you to know whether a number fits in a target, does it need to be divisible?
No, just for the case where it adds up to target repeatedly

You know nothing there

Let's try backtracking

"""

def backtracker(candidates: list, target: int, temp_list: list, combination_list: list, start_index: int):
    if target == 0:
        combination_list.append(temp_list)

    for i in range(start_index, len(candidates)):
        num = candidates[i]
        if target - num == 0:
            combination_list.append(temp_list + [num])
        elif target - num > 0:
            backtracker(candidates, target - num, temp_list + [num], combination_list, i)

def combination_sum(candidates: list, target: int) -> list:
    
    combination_list = []
    backtracker(candidates, target, [], combination_list, 0)
    
    return combination_list


if __name__ == "__main__":
    candidates = [2, 3, 6, 7]
    target = 7

    output = combination_sum(candidates, target)