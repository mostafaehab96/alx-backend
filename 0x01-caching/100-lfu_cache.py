#!/usr/bin/env python3
"""
LRU Cache module
"""

BaseCaching = __import__("base_caching").BaseCaching


class LFUCache(BaseCaching):
    """ LRUCache implements:
    put and get methods in BaseCaching class
    """
    LRU_KEYS = []
    LFU_DICT = {}

    def get_lfu_keys(self):
        """Returns the least frequently used keys"""
        lfu_count = min(sorted(LFUCache.LFU_DICT.values()))
        return [key for key, count in LFUCache.LFU_DICT.items() if
                count == lfu_count]

    def put(self, key, item):
        """Assign the value of item in key in the dictionary
        cache_data
         """
        if key is None or item is None:
            return

        if (len(self.cache_data) == BaseCaching.MAX_ITEMS and
                self.cache_data.get(key) is
                None):
            lfu_keys = self.get_lfu_keys()
            if len(lfu_keys) > 1:
                last_key = LFUCache.LRU_KEYS[-1]
                del self.cache_data[last_key]
                LFUCache.LRU_KEYS.pop()
                print("DISCARD: {}".format(last_key))
            else:
                lfu_key = lfu_keys[0]
                del self.cache_data[lfu_key]
                del LFUCache.LFU_DICT[lfu_key]
                print("DISCARD: {}".format(lfu_key))
                LFUCache.LRU_KEYS.pop()

        if self.get(key) is not None:
            LFUCache.LRU_KEYS.remove(key)
            LFUCache.LRU_KEYS.insert(0, key)
        else:
            LFUCache.LRU_KEYS.insert(0, key)

        LFUCache.LFU_DICT[key] = LFUCache.LFU_DICT.get(key, 0) + 1

        self.cache_data[key] = item

    def get(self, key):
        """return the value in cache_data linked to key."""
        LFUCache.LFU_DICT[key] = LFUCache.LFU_DICT.get(key, 0) + 1
        if self.cache_data.get(key) is not None:
            LFUCache.LRU_KEYS.remove(key)
            LFUCache.LRU_KEYS.insert(0, key)
        return self.cache_data.get(key, None)
