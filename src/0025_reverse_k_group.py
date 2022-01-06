from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseKGroup(head: Optional[ListNode], k: int) -> Optional[ListNode]:
    def recur(node):
        if not node:
            return None
        
        nodes = []
        curr = node
        i = 0
        while curr and i < k:
            nodes.append(curr)
            i += 1
            curr = curr.next
            
            
        if len(nodes) < k:
            return node
        
        rest = nodes[-1].next
        r_nodes = nodes[::-1]
        for i in range(len(r_nodes) - 1):
            r_nodes[i].next = r_nodes[i + 1]
        r_nodes[-1].next = recur(rest)
        
        return r_nodes[0]
    return recur(head)