class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        h = len(matrix) - 1
        w = len(matrix[0]) - 1
        total = (h+1) * (w+1)
        if h == 0 and w == 0:
            return [matrix[0][0]]
        res = []
        while len(res) < total:
            res += (matrix.pop(0))

            if matrix and matrix[0]:
                for row in matrix:
                    res.append(row.pop())
            
            if matrix:
                res += (matrix.pop()[::-1])

            if matrix and matrix[0]:
                for row in reversed(matrix):
                    res.append(row.pop(0))
        return res
