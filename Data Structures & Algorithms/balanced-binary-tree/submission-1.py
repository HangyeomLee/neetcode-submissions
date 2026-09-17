# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root):
        self.balanced = True      # 처음엔 균형이라고 가정

        def helper(node):               # 반환값: node 아래의 높이
            if node is None:
                return 0
            left = helper(node.left)
            right = helper(node.right)
            if abs(left - right) > 1:
                self.balanced = False
            return max(left,right) + 1               # 부모에게 올려줄 높이

        helper(root)
        return self.balanced
            