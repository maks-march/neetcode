class Solution(object):
    def pacificAtlantic(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: List[List[int]]
        """

        def dfs(i, j, visited):
            stack = [(i, j)]
            
            while len(stack):
                root_x, root_y = stack.pop()
                print(f"{root_x} {root_y}")
                neighbors = [(root_x + dx, root_y + dy) for dx, dy in directions 
                if (root_y + dy, root_x + dx) not in visited]
                for x, y in neighbors:
                    if x < 0 or y < 0 or x > n - 1 or y > m - 1:
                        continue
                    if heights[y][x] < heights[root_y][root_x]:
                        continue
                    visited.add((y, x))
                    stack.append((x, y))
        flow_points = []
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        pacific = set()
        atlantic = set()
        n, m = len(heights[0]), len(heights)
        for y in range(m):
            pacific.add((y, 0))
            atlantic.add((y, n-1))
            dfs(0, y, pacific)
            dfs(n - 1, y, atlantic)
            
        for x in range(n):
            pacific.add((0, x))
            atlantic.add((m-1, x))
            dfs(x, 0, pacific)
            dfs(x, m-1, atlantic)
        return sorted(list(pacific & atlantic))



