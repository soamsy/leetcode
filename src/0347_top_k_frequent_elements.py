import heapq
import collections
def topKFrequent(nums: list[int], k: int) -> list[int]:
    h = [(~count, v) for v, count in collections.Counter(nums).items()]
    heapq.heapify(h)
    return [heapq.heappop(h)[1] for _ in range(k)]