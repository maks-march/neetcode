class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        def dfs(current, i, s = 0):
            for j, x in enumerate(nums[i:]):
                copied = current.copy()
                if x + s == target:
                    copied.append(x)
                    yield copied
                    continue
                if x + s < target:
                    copied.append(x)
                    for r in dfs(copied, i+j, x + s):
                        yield r
            


        setted = set(nums)
        result = []
        some = dfs([], 0, 0)
        for r in some:
            result.append(r)
        return result