class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        while l < r:
            m = (l+r+1)//2
            mid = nums[m]
            if mid <= target:
                l = m
            else:
                r = m - 1
        return l if nums[l] == target else -1