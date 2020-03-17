"""
        0
    1           2
3       4    5      6


[0, 1, 2, 3, 4, 5, 6]

"""

class Heap:

    def __init__(self):
        pass

    def insert(self, val: int) -> None:
        """
        Bubble up operation

        1. Add element to the bottom level of the heap
        2. Compare it with it's parent
        3. Swap if applicable (varies if min vs max heap)

        """
        pass

    def extract(self) -> int:
        """
        Bubble down operation

        1. Replace the root with the last element of the last level
        2. Compare the root with its children; if in correct order stop
        3. Swap

        """
        pass

    def heap_sort(self):
        pass

    def left_index(self, i: int) -> int:
        return 2 * i + 1

    def right_index(self, i: int) -> int:
        return 2 * i + 2

    def parent_index(self, i: int) -> int:
        return floor((i - 1)/2)
        


if __name__ == "__main__":
    pass