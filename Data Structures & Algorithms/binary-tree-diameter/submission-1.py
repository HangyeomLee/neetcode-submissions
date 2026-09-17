# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.high_score = 0
        def helper(node):
            self.high_score
            if node == None:
                return 0
            left = helper(node.left)
            right = helper(node.right)
            s = left + right
            self.high_score = max(self.high_score, s)
            return max(left, right) + 1
        helper(root)
        return self.high_score
