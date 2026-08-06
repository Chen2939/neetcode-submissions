class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if not stones: return 0

        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            first, second = abs(heapq.heappop(stones)), abs(heapq.heappop(stones))
            diff = first - second
            if diff != 0:
                heapq.heappush(stones, -diff)
        
        return abs(stones[0]) if stones else 0