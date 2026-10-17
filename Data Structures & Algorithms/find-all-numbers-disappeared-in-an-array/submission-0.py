class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        v = set(nums)
        return [x for x in range(1, len(nums)+1) if x not in v]