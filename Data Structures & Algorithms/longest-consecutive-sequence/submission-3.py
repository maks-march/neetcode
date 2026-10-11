class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_sorted = sorted(list(set(nums)))
        max_len = 0 if len(nums) == 0 else 1
        current_len = 1
        print(nums_sorted)
        for i in range(1, len(nums_sorted)):
            first = nums_sorted[i-1]
            second = nums_sorted[i]
            if first + 1 == second:
                current_len += 1
                max_len = max(max_len, current_len)
            else:
                current_len = 1
        return max_len