class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        N = len(points)
        adj_list = {i:[] for i in range(N)} # i: [cost, node]
        for i in range(N):
            x1, y1 = points[i]
            for j in range(i+1, N):
                x2, y2 = points[j]
                dist = abs(x2-x1) + abs(y2-y1)
                adj_list[i].append([dist, j])
                adj_list[j].append([dist, i])
        
        # Prim's
        res = 0
        visit = set()
        minH = [[0, 0]] # cost, node
        while len(visit) < N:
            cost, node = heapq.heappop(minH)
            if node in visit: continue
            res += cost
            visit.add(node)

            for c, n in adj_list[node]:
                if n not in visit:
                    heapq.heappush(minH, [c, n])
        return res
            
                         