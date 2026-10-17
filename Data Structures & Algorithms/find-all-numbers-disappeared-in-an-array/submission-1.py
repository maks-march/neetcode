class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        for i in range(len(nums)):
            t = abs(nums[i]) - 1
            if nums[t] > 0:
                nums[t] *= -1
        
        r = []
        for i, x in enumerate(nums):
            if x > 0:
                r.append(i+1)
        return r