class Solution:
    def maxArea(self, height: List[int]) -> int:
        i=0
        j=len(height)-1
        mx=float('-inf')
        while(i<j):
            wt=(j-i)*min(height[i],height[j])
            mx=max(wt,mx)
            if height[i]<height[j]:
                i+=1
            else:
                j-=1
        return mx
#TLE
class Solution1:
    def maxArea(self, height: List[int]) -> int:
        n=len(height)
        max1=0
        for i in range(n):
            for j in range(n):
                if i!=j:
                    if max1<((j-i)*min(height[i],height[j])):
                        max1=(j-i)*min(height[i],height[j])
        return max1

        