#!/usr/bin/env python3
"""
Basic Cache module
"""

BaseCaching = __import__("base_caching").BaseCaching


class BasicCache(BaseCaching):
    """ BasicCaching implements:
    put and get methods in BaseCaching class
    """

    def put(self, key, item):
        """Assign the value of item in key in the dictionary
        cache_data
         """
        if key is None or item is None:
            return

        self.cache_data[key] = item

    def get(self, key):
        """return the value in cache_data linked to key."""

        return self.cache_data.get(key, None)
