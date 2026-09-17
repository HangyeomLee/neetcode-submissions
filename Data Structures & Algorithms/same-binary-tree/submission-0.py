# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def helper(p, q):
            if p == None and q == None:# ① 둘 다 None
                return True
            elif p == None or q == None: 
                return False       # ② 한쪽만 None
                return False
            elif p.val != q.val:      # ③ 값이 다름
                return False
            return helper(p.left, q.left) and helper(p.right, q.right)           # ④ 자식 둘 다 확인
        return helper(p,q)