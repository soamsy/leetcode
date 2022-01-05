from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeNthFromEnd(head: Optional[ListNode], n: int) -> Optional[ListNode]:
    curr = head
    size = 0
    while curr:
        curr = curr.next
        size += 1
    
    loc = size - n
    if loc == 0:
        return head.next
    
    counter = 1
    curr = head
    while counter < loc:
        curr = curr.next
        counter += 1
    
    curr.next = curr.next.next
    return head

# head = ListNode(0, ListNode(1, ListNode(2, None)))
# result = removeNthFromEnd(head, 3)
# print(result.val)

