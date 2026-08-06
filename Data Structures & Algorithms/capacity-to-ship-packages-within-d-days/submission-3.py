class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l, r = max(weights), sum(weights)
        res = r

        def canShip(capa):
            ships, currCapa = 1, capa
            for w in weights:
                if currCapa - w < 0:
                    ships += 1
                    currCapa = capa
                currCapa -= w
            if ships <= days:
                return True
            return False


        while l <= r:
            m = (l + r) // 2
            if canShip(m):
                res = min(res, m)
                r = m - 1
            else:
                l = m + 1
        return res