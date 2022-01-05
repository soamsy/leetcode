from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    def merge(a, b):
        if not a:
            return b
        if not b:
            return a
        
        if a.val <= b.val:
            seq = merge(a.next, b)
            a.next = seq
            return a
        else:
            return merge(b, a)
        
    return merge(list1, list2)