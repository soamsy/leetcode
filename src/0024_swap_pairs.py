from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def swapPairs(head: Optional[ListNode]) -> Optional[ListNode]:
    a, b = head, (head.next if head else None)
    final_head = b if b else a
    prev = None
    while a and b:
        rest = b.next
        b.next = a
        a.next = rest
        if prev:
            prev.next = b
        prev = a
        a = rest
        b = rest.next if rest else None
        
    return final_head