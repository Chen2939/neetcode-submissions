class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visit = set()
        hmap = {i: [] for i in range(numCourses)}
        
        for i, v in prerequisites:
            hmap[i].append(v)
        
        def dfs(node):
            if node in visit: return False
            if hmap[node] == []: return True

            visit.add(node)
            for v in hmap[node]:
                if dfs(v) == False:
                    return False 
            visit.remove(node)

            hmap[node] = []
        
            return True
        
        for i in range(numCourses):
            if not dfs(i): return False
        return True
