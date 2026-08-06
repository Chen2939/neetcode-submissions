class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights)-1
        max_area = 0

        while l < r:
            length = r - l
            height = min(heights[r], heights[l])
            area = length * height
            max_area = max(area, max_area)

            if heights[r] < heights[l]:
                r -= 1
            else: l += 1
        
        return max_area