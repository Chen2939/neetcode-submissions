class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0: return False 

        counter = {}
        for n in hand:
            counter[n] = 1 + counter.get(n, 0)
        minH = list(counter.keys())
        heapq.heapify(minH)

        while minH:
            first = minH[0]

            for i in range(first, first + groupSize):
                if i not in counter:
                    return False
                counter[i] -= 1
                if counter[i] == 0:
                    heapq.heappop(minH)
        return True
                
            
            

    