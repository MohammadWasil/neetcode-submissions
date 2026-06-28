class LRUCache:

    def __init__(self, capacity: int):
        """
        {
            1: 10,
        
        }
        
        """
        self.capacity = capacity
        self.lru_cache = {}

    def get(self, key: int) -> int:
        if key not in self.lru_cache:
            return -1
        
        value = self.lru_cache.pop(key)
        self.lru_cache = {key: value, **self.lru_cache}
        return self.lru_cache[key]
        
    def put(self, key: int, value: int) -> None:

        #self.lru_cache[key] = value
        if key in self.lru_cache:
            old_value = self.lru_cache.pop(key)
        self.lru_cache = {key: value, **self.lru_cache}

        if len(self.lru_cache) > self.capacity:
            # emove the last elemt from dict
            self.lru_cache.popitem()


        
