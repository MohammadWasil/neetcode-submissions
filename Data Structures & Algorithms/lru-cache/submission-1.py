class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.lru_cache = {}

    def get(self, key: int) -> int:
        # if key does nto exist in cache, return -1
        if key not in self.lru_cache:
            return -1
        
        # remove the key-value pair that we want to get,
        value = self.lru_cache.pop(key)
        # so that we can add it again n the begning of the dict
        # makin sure all the values in the begining, are most recently used.
        self.lru_cache = {key: value, **self.lru_cache}
        return self.lru_cache[key]
        
    def put(self, key: int, value: int) -> None:

        # check if the key exist in dict, before removing
        if key in self.lru_cache:
            old_value = self.lru_cache.pop(key)
        # place/update the new/old key with new value, ad put it in the begning of the dict
        self.lru_cache = {key: value, **self.lru_cache}

        if len(self.lru_cache) > self.capacity:
            # remove the last elemt from dict, thereby removing the lest receently used key
            self.lru_cache.popitem()


        
