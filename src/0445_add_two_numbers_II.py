
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    a = ""
    while l1:
        a += str(l1.val)
        l1 = l1.next
        
    b = ""
    while l2:
        b += str(l2.val)
        l2 = l2.next
    
    c = int(a) + int(b)
    
    result = None
    prev = None
    for i in reversed(str(c)):
        result = ListNode(int(i))
        result.next = prev
        prev = result
    
    return result