from collections import OrderedDict

"""
General idea is to have O(1) lookup and put

Need a hashmap to enable key-indexed lookup
During put operation we simply need to add key-val
    if capacity is met, evict the least recently used entry
    if we got recently, we need to update it's position in the cache


"""


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.num_items = 0
        self.cache = OrderedDict()

    def get(self, key: int) -> int:
        return self.cache[key] if key in self.cache else -1

    def put(self, key: int, value: int) -> None:
        

if __name__ == "__main__":
    cache = LRUCache(2)
    cache_value = cache.get(5)
    cache.put(1, 1)