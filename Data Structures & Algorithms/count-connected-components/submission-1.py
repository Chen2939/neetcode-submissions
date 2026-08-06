class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        par = [i for i in range(n)]
        rank = [1] * n
        
        def find(node):
            res = node
            while par[res] != res:
                par[res] = par[par[res]]
                res = par[res]
            return res
        
        def union(n1, n2):
            f1, f2 = find(n1), find(n2)
            if par[f1] == par[f2]: return 0
            if rank[f1] < rank[f2]:
                par[f1] = f2
                rank[f2] += 1
            else:
                par[f2] = f1
                rank[f1] += 1
            return 1
        
        num = n
        for n1, n2 in edges:
            num -= union(n1, n2)
        return num
            

