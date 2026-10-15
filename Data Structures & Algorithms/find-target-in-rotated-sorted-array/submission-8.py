class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) -1
        indexes = dict()
        for i, x in enumerate(nums):
            indexes[x] = i
        return indexes.get(target, -1)
        nums_sorted = sorted(nums)
        print(nums_sorted)
        while l < r or nums_sorted[l] == target:
            find = (r-l)//2 + l
            finded = nums_sorted[find]
            print(f"{finded} {l} {r}")
            if finded > target:
                r = find-1
            else:
                l = find

        return indexes[l]
