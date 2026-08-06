class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        result = []

        for x, y in points:
            minHeap.append([-(x**2+y**2), x, y])
        
        heapq.heapify(minHeap)
        print(minHeap)

        while len(minHeap) > k:
            heapq.heappop(minHeap)
        
        print(minHeap)

        for d, x, y in minHeap:
            result.append([x, y])
        
        return result
        