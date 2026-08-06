class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i: [] for i in range(numCourses)}

        # Map each course to prereq list
        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        # visitSet = all courses along the curr DFS
        visitedSet = set()
        def dfs(crs):
            # Cycle
            if crs in visitedSet:
                return False
            if preMap[crs] == []:
                return True

            visitedSet.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre): return False
            visitedSet.remove(crs)
            preMap[crs] = []

            return True
        
        for crs in range(numCourses):
            if not dfs(crs): return False
        return True