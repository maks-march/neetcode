class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_volume = 0
        i = 0
        j = len(heights) - 1
        while i < j:
            left = heights[i]
            right = heights[j]

            volume = min(left, right) * (j-i)
            max_volume = max(max_volume, volume)
            if left < right:
                i += 1
            else:
                j -= 1
        return max_volume