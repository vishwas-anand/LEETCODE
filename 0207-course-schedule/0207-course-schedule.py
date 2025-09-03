class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        def dfs(node):
            if visi[node]!=0:
                return visi[node]==2
            visi[node]=1
            for ngh in adj[node]:
                if visi[ngh]==1 or not dfs(ngh):
                    return False
            visi[node]=2
            return True
        adj=[[] for i in range(numCourses)]
        for u,v in prerequisites:
            adj[v].append(u)
        visi=[0]*numCourses
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True
        