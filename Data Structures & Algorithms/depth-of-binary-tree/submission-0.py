# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode | None) -> int:
        stack = [(root, 1)]
        result = 0
        if root == None:
            return 0
        while len(stack) > 0:
            x, depth = stack.pop()
            result = max(depth, result)
            if x.left:
                stack.append((x.left, depth + 1))
            if x.right:
                stack.append((x.right, depth + 1))
        return result
