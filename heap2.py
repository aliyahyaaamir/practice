"""
Let's design a heap
Key methods we need to consider
Insert
Extract
Parent(index) -> (index-1)//2
child(index)

left_child -> 2i + 1
right_child -> 2i + 2


Heap is represented by an array

2 1 5 6
0 1 2 3

        2
    1       5
6


"""

"""
Let's make this a max heap

"""

class Heap:

    def __init__(self):
        self.arr = []

    def insert(self, value: int) -> None:
        
        self.arr.append(value)
        last_index = len(self.arr) - 1

        parent_index = self.parent(last_index)
        while True:
            if self.arr[parent_index] < value:
                # swap
                self.arr[last_index] = self.arr[parent_index]
                self.arr[parent_index] = value
                last_index = parent_index
                parent_index = self.parent(parent_index)
            else:
                break

    def extract_max(self) -> int:

        last_element = self.arr.pop()
        max = self.arr[0]
        self.arr[0] = last_element

        self.heapify()

        return max

    def heapify(self) -> None:

        heap_size = len(self.arr)
        left_child_i = self.left_child(0)
        right_child_i = self.right_child(0)

        i = 0
        while True:

            if left_child_i < heap_size and right_child_i < heap_size:
                # Left is greater than right
                if self.arr[left_child_i] < self.arr[right_child_i]:
                    left_child = self.arr[left_child_i]
                    self.arr[left_child_i] = self.arr[i]
                    self.arr[i] = left_child
                    i = left_child_i
                    left_child_i = self.left_child(left_child_i)
                    right_child_i = self.right_child(right_child_i)
                else:
                    right_child = self.arr[right_child_i]
                    self.arr[right_child_i] = self.arr[i]
                    self.arr[i] = right_child
                    i = right_child_i
                    left_child_i = self.left_child(right_child_i)
                    right_child_i = self.right_child(right_child_i)
                continue
            
            if left_child_i < heap_size and self.arr[left_child_i] > self.arr[i]:
                pass
            elif right_child_i < heap_size and self.arr[right_child_i] > self.arr[i]:
                pass
            else:
                break

        

    def parent(self, index: int) -> int:
        return (index - 1)//2

    def left_child(self, index: int) -> int:
        return 2 * index + 1
    
    def right_child(self, index: int) -> int:
        return 2 * index + 2

    




if __name__ == "__main__":
    pass