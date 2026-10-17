class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        n = dict()
        for i, x in enumerate(nums):
            y = target - x
            if x in n:
                return [n[x], i]
            else:
                n[y] = i
        return []