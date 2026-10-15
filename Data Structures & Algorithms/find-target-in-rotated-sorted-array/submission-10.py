class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) -1
        while nums[l] != target and l < r:
            find = (r-l)//2 + l
            finded = nums[find]
            left = nums[l]
            right = nums[r]
            if finded == target:
                return find
            if left <= finded:
                # разрыв справа
                if target >= left and target < finded:
                    r = find - 1
                else:
                    l = find + 1
            else:
                # разрыв слева
                if target <= right and target > finded:
                    l = find + 1
                else:
                    r = find - 1

        return l if nums[l] == target else -1
