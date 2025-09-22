from collections import Counter
class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        a=Counter(nums)
        b=max(a.values())
        c=0
        for i in a.values():
            if i==b:
                c+=i
        return c