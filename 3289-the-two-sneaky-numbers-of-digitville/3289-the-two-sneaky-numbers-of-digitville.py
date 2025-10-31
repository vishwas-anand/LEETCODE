class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        list1=list()
        nums_counter=Counter(nums)
        for key,value in nums_counter.items():
            if value==2:
                list1.append(key)
        return list1