"""
Merge intervals

Input: [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]

Basically you can only merge intervals if the lowest
number is less than the next lowest number

We can sort on the first index?

if i1 <= i2 => overlap?
then max(j1, j2) assuming j2 > i2 (otherwise this collapses)

Consider
[0, 4] [1, 3]  = 0, 4
i1 j1  i2  j2

i2 needs to be <= i1


"""
def merge(intervals: list) -> list:

    if len(intervals) <= 1:
        return intervals

    sorted_intervals = sorted(intervals, key=lambda x: x[0])
    merged_intervals = []

    print(sorted_intervals)

    last_interval = sorted_intervals[0]

    for interval in sorted_intervals[1:]:
        i1, j1 = last_interval
        i2, j2 = interval

        # [0, 5], [0, 3], [0,2], [3, 4]
        # 
        if i1 <= i2 and j1 >= i2:
            j = max(j1, j2)

            last_interval = [i1, j]
        else:
            merged_intervals.append(last_interval)
            last_interval = interval
        
    
    merged_intervals.append(last_interval)

    return merged_intervals

if __name__ == "__main__":
    input = [[2,6], [1, 3],[8,10],[15,18]]
    # input = [[1,4],[4,5]]
    # input = [[1,4],[0,4]]
    # input = [[1,4],[2,3]]
    input = [[1,4],[0,2],[3,5]] # 0, 4
    output = merge(input)