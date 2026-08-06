class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        diff = [gas[i] - cost[i] for i in range(len(gas))]
        res = float('inf')
        for i in range(len(diff)):
            if diff[i] < 0: continue
            stations = diff[i : len(diff)] + diff[0 : i]
            oil = 0
            for c in stations:
                oil += c
                if oil < 0: break
            if oil >= 0:
                res = i
        return res if res != float('inf') else -1     