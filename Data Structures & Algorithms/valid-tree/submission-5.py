class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        hmap = defaultdict(list)
        visit = set()
        for v1, v2 in edges:
            hmap[v1].append(v2)
            hmap[v2].append(v1)
        
        def dfs(node, prevNode):
            if node in visit: return False
            visit.add(node)
            for nei in hmap[node]:
                if nei is prevNode: continue
                if not dfs(nei, node): return False
            return True
        
        return dfs(0, -1) and len(visit) == n