class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        n = len(nums)
        answer = []
        def calculate_x_sum(subarray):
            count = Counter(subarray)
            sorted_elements = sorted(count.items(), key=lambda item: (-item[1], -item[0]))
            top_x_elements = sorted_elements[:x] 
            x_sum = sum(value * count[value] for value, _ in top_x_elements)
            return x_sum
        for i in range(n - k + 1):
            subarray = nums[i:i + k]
            answer.append(calculate_x_sum(subarray))
        
        return answer
