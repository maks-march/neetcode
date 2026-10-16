# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: TreeNode | None) -> list[list[int]]:
        result = []
        

        def search(root, depth):
            if root == None:
                return
            if len(result) - 1 < depth:
                result.append([])
            result[depth].append(root.val) 
            search(root.left, depth + 1)
            search(root.right, depth + 1)
        
        search(root, 0)
        return result