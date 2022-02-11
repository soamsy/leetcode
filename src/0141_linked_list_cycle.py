from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def hasCycle(head: Optional[ListNode]) -> bool:
    if not head:
        return False
    
    oneStep = head
    twoStep = head.next
    while oneStep and twoStep:
        if oneStep == twoStep:
            return True
        oneStep = oneStep.next
        twoStep = twoStep.next
        if twoStep:
            twoStep = twoStep.next
    
    return False