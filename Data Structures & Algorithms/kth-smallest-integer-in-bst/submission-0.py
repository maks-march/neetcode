# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode | None, k: int) -> int:
        stack = []
        i = 0
        
        def go_left(root):
            go = root
            stack.append(go)
            while go.left:
                go = go.left
                stack.append(go)
        
        go_left(root)

        while len(stack):
            i += 1
            current = stack.pop()
            if i == k:
                return current.val
            if current.right:
                go_left(current.right)
        return -1

