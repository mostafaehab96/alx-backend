#!/usr/bin/env python3
"""
MRU Cache module
"""

BaseCaching = __import__("base_caching").BaseCaching


class MRUCache(BaseCaching):
    """ LRUCache implements:
    put and get methods in BaseCaching class
    """
    MRU_KEYS = []

    def put(self, key, item):
        """Assign the value of item in key in the dictionary
        cache_data
         """
        if key is None or item is None:
            return

        if (len(self.cache_data) == BaseCaching.MAX_ITEMS and self.get(key) is
                None):
            recent_key = MRUCache.MRU_KEYS[0]
            del self.cache_data[recent_key]
            MRUCache.MRU_KEYS.pop(0)
            print("DISCARD: {}".format(recent_key))

        if self.get(key) is not None:
            MRUCache.MRU_KEYS.remove(key)
            MRUCache.MRU_KEYS.insert(0, key)
        else:
            MRUCache.MRU_KEYS.insert(0, key)

        self.cache_data[key] = item

    def get(self, key):
        """return the value in cache_data linked to key."""
        if self.cache_data.get(key) is not None:
            MRUCache.MRU_KEYS.remove(key)
            MRUCache.MRU_KEYS.insert(0, key)
        return self.cache_data.get(key, None)
