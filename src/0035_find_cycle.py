from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def detectCycle(head: Optional[ListNode]) -> Optional[ListNode]:
    nodes = set()
    curr = head
    while curr:
        if curr in nodes:
            return curr
        nodes.add(curr)
        curr = curr.next
    return None