class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_settled = set(nums)
        if len(nums) == 0:
            return 0
        max_len = 1
        starts = [x for x in nums_settled if x-1 not in nums_settled]
        print(starts)
        for x in starts:
            end = x + 1
            current_len = 1
            while end in nums_settled:
                current_len += 1
                max_len = max(max_len, current_len)
                end += 1
        return max_len