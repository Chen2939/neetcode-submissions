# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Initialize dummy node point to head
        dummy = ListNode(0, head)
        l = dummy
        r = head
        
        # get right pointer by shifting n steps
        for _ in range(n):
            r = r.next
        
        # shift left and right until right hit null
        while r:
            l = l.next
            r = r.next
        
        l.next = l.next.next

        return dummy.next
        


