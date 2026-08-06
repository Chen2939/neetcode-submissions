# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Step 1: Split list in half
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Step 2: Reverse second list
        sec = slow.next
        prev = None
        # also need to cut between first list and second list
        slow.next = None
        while sec:
            tmp = sec.next
            sec.next = prev
            prev = sec
            sec = tmp
        
        # Step 3: Merge two list
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2
        
        

