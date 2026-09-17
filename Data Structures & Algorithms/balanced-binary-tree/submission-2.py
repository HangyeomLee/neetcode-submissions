# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root):
        self.balanced = True
        self.high_score = 0
        def helper(node):
            if node == None:
                return 0
            left = helper(node.left)
            right = helper(node.right)
            s = left + right
            if abs(right - left) > 1:
                self.balanced = False
                return False
            return max(left,right) + 1
        helper(root)
        return self.balanced
            