# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_val = 0
        def helper(root):
            if root is None:
                return 0
            left = helper(root.left)
            right = helper(root.right)
            count = max(left,right) + 1
            nonlocal max_val
            max_val = max(left + right, count - 1, max_val)
            print(max_val)
            return count
        helper(root)
        return max_val