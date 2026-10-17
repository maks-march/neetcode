class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        nums.sort()
        for i, v in enumerate(nums):
            if i != v:
                return i
            if i == len(nums) - 1:
                return i+1
            
            
