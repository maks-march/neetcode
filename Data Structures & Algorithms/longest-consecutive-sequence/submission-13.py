class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_settled = set(nums)
        if len(nums) == 0:
            return 0
        max_len = 1
        for x in nums_settled:
            if x-1 in nums_settled:
                continue
            current_len = 1
            while x+current_len in nums_settled:
                current_len += 1
                max_len = max(max_len, current_len)
        return max_len