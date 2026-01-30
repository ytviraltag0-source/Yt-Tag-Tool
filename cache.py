CACHE = {}

def cache_get(q):
    return CACHE.get(q)

def cache_set(q, data):
    CACHE[q] = data
