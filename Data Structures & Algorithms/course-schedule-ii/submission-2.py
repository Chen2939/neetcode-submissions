class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        hmap = {i:[] for i in range(numCourses)}
        for i, v in prerequisites:
            hmap[i].append(v)
        
        res = []
        visit, cycle = set(), set()

        def dfs(node):
            if node in cycle: return False
            if node in visit: return True

            cycle.add(node)
            for pre in hmap[node]:
                if dfs(pre) == False:
                    return False
            cycle.remove(node)

            visit.add(node)
            res.append(node)
            return True
        
        for i in range(numCourses):
            if not dfs(i): return []
        return res
