from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    def toNum(l):
        digits = []
        base = 1
        while l:
            digits.append((l.val, base))
            base *= 10
            l = l.next
        return sum([val*b for (val,b) in digits])
    
    total = toNum(l1) + toNum(l2)
    total_digits = [int(x) for x in str(total)]
    new_list = None
    for i in total_digits:
        new_list = ListNode(i, new_list)
        
    return new_list