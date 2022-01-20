from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def middleNode(head: Optional[ListNode]) -> Optional[ListNode]:
    count = 0
    curr = head
    while curr:
        curr = curr.next
        count += 1
        
    curr = head
    i = 0
    while curr and i < count // 2:
        curr = curr.next
        i += 1
    
    return curr