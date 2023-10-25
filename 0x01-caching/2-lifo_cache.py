#!/usr/bin/env python3
"""
LIFO Cache module
"""

BaseCaching = __import__("base_caching").BaseCaching


class LIFOCache(BaseCaching):
    """ LIFOCache implements:
    put and get methods in BaseCaching class
    """
    SORTED_KEYS = []

    def put(self, key, item):
        """Assign the value of item in key in the dictionary
        cache_data
         """
        if key is None or item is None:
            return

        if (len(self.cache_data) == BaseCaching.MAX_ITEMS and self.get(key) is
                None):
            last_key = LIFOCache.SORTED_KEYS[0]
            del self.cache_data[last_key]
            print("DISCARD: {}".format(last_key))

        self.cache_data[key] = item
        LIFOCache.SORTED_KEYS.insert(0, key)

    def get(self, key):
        """return the value in cache_data linked to key."""

        return self.cache_data.get(key, None)
