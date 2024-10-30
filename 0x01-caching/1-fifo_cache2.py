#!/usr/bin/env python3

"""
This class is a caching system that inherits
from BaseCaching
"""

from collections import OrderedDict
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    This class called `FIFOCache` is a caching system
    that inherits from`BaseCaching`
    """

    def __init__(self):
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """
        assign to the dictionary `self.cache_data` the
        `item` value for the key `key`
        """

        if key is None or item is None:
            return

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            first_key, _ = self.cache_data.popitem(last=False)
            print(f"DISCARD: {first_key}")

        self.cache_data[key] = item

    def get(self, key):
        """
        This returns the value in `self.cache_data` linked to `key`
        """
        return self.cache_data.get(key, None)
