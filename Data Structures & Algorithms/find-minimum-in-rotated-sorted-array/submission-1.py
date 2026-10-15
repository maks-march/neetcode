class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)-1

        while l < r:
            center = (r-l)//2 + l
            target = nums[center]
            if l == r - 1:
                return nums[l] if nums[l] < nums[r] else nums[r]
                    
            if nums[l] < target and target > nums[r]:
                l = center
            else:
                r = center
        return nums[l] if nums[l] < nums[r] else nums[r]