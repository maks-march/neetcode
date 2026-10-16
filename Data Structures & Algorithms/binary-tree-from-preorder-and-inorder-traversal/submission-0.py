# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.ind = 0

    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
               
        indices = dict()
        for i, x in enumerate(inorder):
            indices[x] = i

        def build(l, r):
            if l > r: return None
            root_val = preorder[self.ind]
            self.ind += 1
            root = TreeNode(root_val)
            mid = indices[root_val]
            root.left = build(l, mid-1)
            root.right = build(mid+1, r)
            
            return root

        return build(0, len(preorder) - 1)