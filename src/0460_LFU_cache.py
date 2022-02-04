import collections

class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.counts = {}
        self.frequencies = []
        self.qs = []
        self.m = {}
        
    def updateFrequency(self, key: int):
        loc = self.counts.get(key, -1)
        new_loc = loc + 1
        self.counts[key] = new_loc
        if new_loc >= len(self.frequencies):
            self.frequencies.append(set())
            self.qs.append(collections.deque())
        self.frequencies[new_loc].add(key)
        self.qs[new_loc].appendleft(key)
        
        if loc != -1:
            self.frequencies[loc].remove(key)
    
    def removeLowest(self):
        lowest_freq = 0
        while lowest_freq < len(self.frequencies) and len(self.frequencies[lowest_freq]) == 0:
            lowest_freq += 1
        nums = self.frequencies[lowest_freq]
        q = self.qs[lowest_freq]
        while q[-1] not in nums:
            q.pop()
        to_remove = q.pop()
        nums.remove(to_remove)
        del self.counts[to_remove]
        del self.m[to_remove]
        
    def get(self, key: int) -> int:
        if self.capacity == 0:
            return -1
        val = self.m.get(key, -1)
        if val != -1:
            self.updateFrequency(key)
        return self.m.get(key, -1)

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return
        self.m[key] = value
        if len(self.m) > self.capacity:
            self.removeLowest()
        self.updateFrequency(key)


# def fn(actions, arglist):
#     cache = None
#     result = []
#     for action, args in zip(actions, arglist):
#         if action == "LFUCache":
#             cache = LFUCache(*args)
#             result.append(None)
#         elif action == "put":
#             cache.put(*args)
#             result.append(None)
#         elif action == "get":
#             result.append(cache.get(*args))

#     print(result)
        


# fn(
# ["LFUCache","put","put","get","put","get","get","put","get","get","get"],
# [[2],[1,1],[2,2],[1],[3,3],[2],[3],[4,4],[1],[3],[4]]
# )

# fn(
# ["LFUCache","put","put","get","get","get","put","put","get","get","get","get"],
# [[3],[2,2],[1,1],[2],[1],[2],[3,3],[4,4],[3],[2],[1],[4]]
# )

# fn(
# ["LFUCache","put","get"],
# [[0],[0,0],[0]]
# )
