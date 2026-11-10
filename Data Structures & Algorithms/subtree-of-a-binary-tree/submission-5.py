# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root is None:
            return False
        state = False
        def helper(root, subroot):
            if root is None and subroot is None:
                return True
            elif root is None or subroot is None:
                return False
            left = helper(root.left, subroot.left)
            right = helper(root.right, subroot.right)
            nonlocal state
            state = left and right
            if state:
                if root.val != subroot.val:
                    state = False
            return state
        check_state = helper(root, subRoot)
        if check_state:
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        