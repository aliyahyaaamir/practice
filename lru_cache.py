"""
What do we know
An LRU Cache is a least-recently used cache,
where cache entries that have not been used in a while
are the first ones to be evicted

If an entry is updated (put) or gotten (get) than that entry has now been recently used

We have an initial capacity of entries we can store

get(key) will return associated value if exists else -1
put(key, value) will set or insert the key if it does not exist


Let's aim for O(1) retrieval
Awesome, so I think we hit that using a list of tuples with timestamp and key pair

Assume capacity is not 0, otherwise this all collapses

Cool, now let's make this better
O(1) Retrieval
O(1) Insertion/Update


Idea is to maintain the hash map since retrieval requires us to have a quick lookup
Each entry in the hashmap points to Node


The LRUCache maintains the head of the list
"""

from collections import deque
import time

class Node:
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.head = None
        self.cache = {}
        self.current_capacity = 0
        self.capacity = capacity
        # Operates like a queue, first entry added is first entry evicted when capacity is hit
        # self.recently_used = {}

    def remove_node(self, node: Node) -> None:
        next_node = node.next
        prev_node = node.prev

        if prev_node:
            prev_node.next = next_node
            if next_node:
                next_node.prev = prev_node
        else:
            self.head = next_node

    def add_head(self, node: Node) -> None:
        if not self.head:
            print('here')
            self.head = node
        else:
            print('there')
            old_head = self.head
            self.head = node
            old_head.prev = node
            node.next = old_head.next

    def get(self, key: int) -> int:
        if key in self.cache:
            # some sort of marker to indicate that this was recently retrieved
            # hmmmmm
            # there is a problem here
            # it looks like it will keep duplicates, so need to check first
            # makes this
            # alternatively we can maintain counts of each key? with a hashing function
            # key % capacity ? hmmmm, and then update a count like that
            node = self.cache[key]
            self.remove_node(node)
            node = Node(key, node.value)
            self.add_head(node)
            # print(node.prev, node.next, node.key, node.value)
            # self.recently_used[key] = time.time()
            return node.value

        return -1

    def put(self, key: int, value: int) -> None:
        
        if key in self.cache:
            # self.recently_used[key] = time.time()
            node = self.cache[key]
            self.remove_node(node)
            node = Node(key, value)
            self.add_head(node)
            self.cache[key] = node
        else:
            # Check current capacity to see if we need to perform any evictions
            if self.current_capacity == self.capacity:
                # need to evict an entry
                self.current_capacity -= 1

                # Idea is that the first entry has not been used, but wait we keep appending
                # So will need to do a filter step to get rid of duplicates

                # iterate through all recently used entries
                # min_time = float('inf')
                # key_to_evict = -1
                # for _key in self.recently_used.keys():
                #     if self.recently_used[_key] < min_time:
                #         min_time = self.recently_used[_key]
                #         key_to_evict = _key
                node_to_evict = self.head
                self.remove_node(node_to_evict)
                print('evicting ' + str(node_to_evict.key))
                del self.cache[node_to_evict.key]
                # del self.recently_used[key_to_evict]

            node = Node(key, value)
            self.add_head(node)
            self.current_capacity += 1
            self.cache[key] = node
            # print(node.prev, node.next, node.key, node.value)

            # self.recently_used[key] = time.time()


if __name__ == "__main__":

    # Your LRUCache object will be instantiated and called as such:
    obj = LRUCache(3)
    param_1 = obj.get(5)
    obj.put(5,3)
    obj.put(4,2)
    obj.put(7,3)
    obj.get(5)
    obj.put(2,2)