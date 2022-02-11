from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
    def rev(node, prev):
        if not node:
            return prev
        toReverse = node.next
        node.next = prev
        return rev(toReverse, node)
    return rev(head, None)