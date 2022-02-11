from typing import Optional
import heapq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeKLists(lists: list[Optional[ListNode]]) -> Optional[ListNode]:
    h = [(n.val, i, n) for i, n in enumerate(lists) if n]
    heapq.heapify(h)
    
    result = None
    last = None
    def push(node):
        nonlocal result, last
        if not result:
            result = node
            last = result
        else:
            last.next = node
            last = node
            last.next = None
    
    
    while h:
        val, i, node = heapq.heappop(h)
        if node.next:
            heapq.heappush(h, (node.next.val, i, node.next))
        push(node)
        
    return result
