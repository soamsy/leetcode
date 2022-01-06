from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeKLists(lists: list[Optional[ListNode]]) -> Optional[ListNode]:
    vec = []
    for n in lists:
        curr = n
        while curr:
            vec.append(curr.val)
            curr = curr.next
    
    vec.sort()
    top = None
    curr = None
    for n in vec:
        if not top:
            top = ListNode(n)
            curr = top
            continue
        curr.next = ListNode(n)
        curr = curr.next
        
    return top
