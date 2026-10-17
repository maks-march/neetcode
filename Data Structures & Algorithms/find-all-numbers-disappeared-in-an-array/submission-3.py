class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        for i in range(len(nums)):
            t = abs(nums[i]) - 1
            if nums[t] > 0:
                nums[t] *= -1
        
        return [i + 1 for i, x in enumerate(nums) if x > 0]