"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # Initialize a hashmap of old node : new node
        # Insert None: None for null node as default
        hm = {None: None}

        # First pass: create node, map old node to new node
        curr = head
        while curr:
            node = Node(curr.val)
            hm[curr] = node
            curr = curr.next

        # Second pass: connect pointers
        curr = head
        while curr:
            copy = hm[curr]
            copy.next = hm[curr.next]
            copy.random = hm[curr.random]
            curr = curr.next
            
        return hm[head]
