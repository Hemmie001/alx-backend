#!/usr/bin/env python3

"" "Task 0: Basic dictionary """


from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    This class called `BasicCache` is a caching system which
    inherits from `BaseCaching`
    """

    def put(self, key, item):
        """
        This function updates/adds to the dictionary called
        `self.cache_data`
        the 'key' is the key under which the item will be
        stored.
        while 'item' the value to be stored in the dictionary
        under the specified 'key'
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """
        return the value in `self.cache_data` linked to `key`
        """

        return self.cache_data.get(key, None)
