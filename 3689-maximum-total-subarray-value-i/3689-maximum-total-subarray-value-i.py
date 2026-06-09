class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        a=min(nums)
        b=max(nums)
        return (b-a)*k