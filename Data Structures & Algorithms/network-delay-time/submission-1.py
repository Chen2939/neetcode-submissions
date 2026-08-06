class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edge_list = defaultdict(list)
        for u, v, w in times:
            edge_list[u].append((v, w))
        minH = [(0, k)]
        time = 0
        visit = set()

        while minH:
            w1, n1 = heapq.heappop(minH)
            if n1 in visit: continue
            visit.add(n1)
            time = max(time, w1)

            for nei, wei in edge_list[n1]:
                if nei not in visit:
                    heapq.heappush(minH, (wei+w1, nei))
        
        return time if len(visit) == n else -1

        