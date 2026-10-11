class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        products = []
        preproduct = 1
        isZero = False
        isSecondZero = False
        for x in nums:
            preproduct *= x if x != 0 else 1
            isSecondZero = (isZero and x == 0) or isSecondZero
            isZero = x == 0 or isZero
        for x in nums:
            if (x == 0):
                products.append(0 if isSecondZero else preproduct)
            else:
                products.append(preproduct // x if not isZero else 0)
        return products