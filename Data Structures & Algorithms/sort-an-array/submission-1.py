class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def sift_down(start, end):
            root = start
            while True:
                child = 2 * root + 1
                if child > end:
                    break
                if child + 1 <= end and nums[child+1] > nums[child]:
                    child += 1
                if nums[root] < nums[child]:
                    nums[root], nums[child] = nums[child], nums[root]
                    root = child
                else: break
        n = len(nums)
        for i in range(n//2, -1, -1):
            sift_down(i, n-1)
        for i in range(n-1, 0, -1):
            nums[i], nums[0] = nums[0], nums[i]
            sift_down(0, i-1)
        return nums