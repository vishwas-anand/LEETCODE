class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        graph=defaultdict(list)
        occur=[0]*n
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
            occur[u]+=1
            occur[v]+=1
        #oneleaf
        leaves=deque()
        for i in range(n):
            if occur[i]==1:
                leaves.append(i)
        leftnodes=n
        while leftnodes>2:
            length=len(leaves)
            leftnodes-=length
            for i in range(length):
                leaf=leaves.popleft()
                for ngh in graph[leaf]:
                    occur[ngh]-=1
                    if occur[ngh]==1:
                        leaves.append(ngh)
        return list(leaves)

        