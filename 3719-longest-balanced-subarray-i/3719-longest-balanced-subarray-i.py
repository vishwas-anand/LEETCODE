class Solution:
    def longestBalanced(self, nums):
        res=0
        for i in range(len(nums)):
            mp={}
            di_e=0
            di_o=0
            for j in range(i, len(nums)):
                x=nums[j]
                if x not in mp:
                    mp[x]=1
                    if x%2==0:
                        di_e+=1
                    else:
                        di_o+=1
                else:
                    mp[x]+=1
                if di_e==di_o:
                    res=max(res,j-i+1)
        return res
       