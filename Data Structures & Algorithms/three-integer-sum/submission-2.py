class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums_settled = set(nums)
        nums.sort()
        result = []
        print(nums[:-2])
        for i, first in enumerate(nums[:-2]):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            target = -first
            j = i+1
            k = len(nums)-1
            while j < k:
                second = nums[j]
                third = nums[k]
                if second+third == target:
                    result.append([first, second, third])
                if second+third < target:
                    j += 1
                    while nums[j] == second and j < k:
                        j += 1
                else:
                    k -= 1
                    while nums[k] == third and j < k:
                        k -= 1
            
        return result
