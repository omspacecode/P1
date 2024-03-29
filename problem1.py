import collections
class LRU_Cache(object):
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = collections.OrderedDict()

    def get(self, key):
        try:
            value = self.cache.pop(key)
            self.cache[key] = value
            return value
        except KeyError:
            return -1

    def set(self, key, value):
        try:
            self.cache.pop(key)
        except KeyError:
            if len(self.cache) >= self.capacity:
                self.cache.popitem(last=False)
        self.cache[key] = value

our_cache = LRU_Cache(5)

our_cache.set(1, 1)
our_cache.set(2, 2)
print(our_cache.get(1))       # returns 1
our_cache.get(2)       # returns 2
our_cache.get(3)       # return -1
