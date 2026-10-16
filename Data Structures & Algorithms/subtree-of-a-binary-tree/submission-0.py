# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        stack = [root]
        result = root == None and subRoot == None

        while len(stack):
            x = stack.pop()
            if x == None:
                continue
            

            if x.val == subRoot.val:
                result = result or self.isEqual(x, subRoot)

            stack.append(x.left)
            stack.append(x.right)
        return result

    def isEqual(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        stack = [(p, q)]
        while len(stack):
            first, second = stack.pop()
            if not first and not second:
                continue

            if not first or not second or first.val != second.val:
                return False
            stack.append((first.left, second.left))
            stack.append((first.right, second.right))
        return True;












