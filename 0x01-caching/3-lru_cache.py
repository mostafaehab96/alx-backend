#!/usr/bin/env python3
"""
LRU Cache module
"""

BaseCaching = __import__("base_caching").BaseCaching


class LRUCache(BaseCaching):
    """ LRUCache implements:
    put and get methods in BaseCaching class
    """
    LRU_KEYS = []

    def put(self, key, item):
        """Assign the value of item in key in the dictionary
        cache_data
         """
        if key is None or item is None:
            return

        if (len(self.cache_data) == BaseCaching.MAX_ITEMS and self.get(key) is
                None):
            last_key = LRUCache.LRU_KEYS[-1]
            del self.cache_data[last_key]
            LRUCache.LRU_KEYS.pop()
            print("DISCARD: {}".format(last_key))

        if self.get(key) is not None:
            LRUCache.LRU_KEYS.remove(key)
            LRUCache.LRU_KEYS.insert(0, key)
        else:
            LRUCache.LRU_KEYS.insert(0, key)

        self.cache_data[key] = item

    def get(self, key):
        """return the value in cache_data linked to key."""
        if self.cache_data.get(key) is not None:
            LRUCache.LRU_KEYS.remove(key)
            LRUCache.LRU_KEYS.insert(0, key)
        return self.cache_data.get(key, None)
