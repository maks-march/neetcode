class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        moves = ((0, 1),(0, -1),(1, 0),(-1, 0))
        h = len(board) - 1
        w = len(board[0]) - 1
        l = len(word)

        def dfs(x, y, current, visited):
            if current == l:
                return True
            result = False
            n = [(x+i,y+j) for i, j in moves 
                if x+i >= 0 and y+j >= 0 and x+i <= w and y+j <= h 
                and (x+i, y+j) not in visited]
            for i, j in n:
                if board[j][i] == word[current]:
                    v = visited.copy()
                    v.add((i, j))
                    result = result or dfs(i, j, current + 1, v)
            return result


        for j, y in enumerate(board):
            for i, x in enumerate(y):
                if x == word[0]:
                    if dfs(i, j, 1, {(i, j)}):
                        return True
        return False