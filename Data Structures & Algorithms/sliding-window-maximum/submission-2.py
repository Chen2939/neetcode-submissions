class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        l = r = 0
        q = collections.deque() # Contains indices instead of number

        while r < len(nums):
            # Pop smaller values from the queue
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            # If out of bound, then remove left from window
            # e.g. [2, 1, 3], k = 2
            # window is at 2nd and 3rd, so we don't care the 1st
            if l > q[0]:
                q.popleft()
            
            # Edge case: check our window is at least size k
            if (r + 1) >= k:
                output.append(nums[q[0]])
                l += 1

            r += 1
        return output
