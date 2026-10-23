class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l, r = 0, len(nums) -1
        res = [0] * (r+1)

        while l <= r:
            left = nums[l]*nums[l]
            right = nums[r]* nums[r]
            if left < right:
                res[r-l] = right
                r -= 1
            else:
                res[r-l] = left
                l += 1
        return res