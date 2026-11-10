# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def helper(p,q):
            if p is None and q is None:
                return True
            elif p is None or q is None:
                return False
            state = helper(p.left, q.left) and helper(p.right, q.right)
            if state:
                if p.val == q.val:
                    state = True
                else:
                    state = False
            return state
        return helper(p, q)