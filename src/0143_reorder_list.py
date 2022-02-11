from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reorderList(head: Optional[ListNode]) -> None:
    """
    Do not return anything, modify head in-place instead.
    """
    slow, fast = head, head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
    
    def rev(node, prev=None):
        if not node:
            return prev
        toReverse = node.next
        node.next = prev
        return rev(toReverse, node)
    
    inOrder = head
    revOrder = rev(slow.next)
    slow.next = None
    
    def merge(a, b, toggle=False):
        if not a:
            return b
        if not b:
            return a
        
        if toggle:
            return merge(b, a)
        else:
            a.next = merge(a.next, b, True)
            return a
    
    merge(inOrder, revOrder)