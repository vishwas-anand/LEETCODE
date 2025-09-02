class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        n = len(points)
        points.sort(key = lambda x: (x[0], -x[1]))
        res = 0

        for i in range(n):
            for j in range(i + 1, n):
                if points[i][1] >= points[j][1]:
                    flag = True
                    for k in range(i + 1, j):
                        if points[j][1] <= points[k][1] <= points[i][1]:
                            flag = False
                    
                    if flag:
                        res += 1
        
        return res